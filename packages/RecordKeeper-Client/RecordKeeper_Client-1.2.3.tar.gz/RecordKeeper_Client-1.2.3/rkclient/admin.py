import ast
import json
import logging
from uuid import UUID
from typing import Tuple, List, Optional, Any, Callable, Dict

from requests.exceptions import RequestException

from rkclient.entities import Artifact, PEM
from rkclient.client import RKClient
from rkclient.serialization import ArtifactSerialization, PEMSerialization, _decode_from_base64

log = logging.getLogger("rkclient")


class RKAdmin(RKClient):
    """
    This class is not supposed to be used by normal RK user, but by RK administrator or in tests.
    """

    def clean_dbs(self) -> Tuple[str, bool]:
        """
        :return: first element: error message
                 second element: True for success, False for error
        """
        resp = self.session.post(url=self.receiver_url + "/clean", timeout=self.timeout_sec)
        if resp.status_code != 200:
            return f"Error occurred: {resp.status_code}, {resp.text}", False
        return '', True

    def get_pems(self,
                 page_index: int = -1,
                 page_size: int = -1,
                 sort_field: str = '',
                 sort_order: str = '',
                 filters: Optional[Dict] = None) -> Tuple[List[PEM], str, bool]:
        """
        :return: first element: list of pems (as json string) or error message
                 The artifacts lists in PEM will contain only artifact ID
                 second element: True for success, False for error
        """

        query_params: Dict[str, Any] = _parse_params(page_index, page_size, sort_field, sort_order, filters)

        def _get_pems() -> Tuple[List[Any], str, bool]:
            resp = self.session.get(url=self.receiver_url + "/pems", timeout=self.timeout_sec, params=query_params)
            if resp.status_code != 200:
                return [], f"Error occurred: {resp.status_code}", False
            pems = []
            pems_json = json.loads(resp.text)
            for p in pems_json:
                pems.append(PEMSerialization.from_dict(p, True))
            return pems, 'OK', True

        return _handle_request(_get_pems, "getting pems")

    def get_pems_count(self,
                       page_index: int = -1,
                       page_size: int = -1,
                       sort_field: str = '',
                       sort_order: str = '',
                       filters: Optional[Dict] = None) -> Tuple[int, str, bool]:

        query_params: Dict[str, Any] = _parse_params(page_index, page_size, sort_field, sort_order, filters)

        def _get_pems() -> Tuple[int, str, bool]:
            resp = self.session.get(url=self.receiver_url + "/pems_count", timeout=self.timeout_sec, params=query_params)
            if resp.status_code != 200:
                return -1, f"Error occurred: {resp.status_code}", False
            obj = json.loads(resp.text)
            return int(obj['pems_count']), 'OK', True

        return _handle_request(_get_pems, "getting pems count")

    def get_artifact(self, artifact_id: UUID, source: str = 'sqldb') -> Tuple[Optional[Artifact], bool]:
        # todo this could be improved by using different endpoint
        res, msg, ok = self.get_artifacts(source)
        if not ok:
            log.error(f"getting artifact error: {msg}")
            return None, False

        artifacts: List[Artifact] = res
        for a in artifacts:
            if a.ID == artifact_id:
                return a, True

        return None, False

    def get_taxonomy_file(self, taxonomy_id: UUID) -> Tuple[str, bool]:
        resp = self.session.get(url=self.receiver_url + f"/taxonomy/{taxonomy_id.hex}", timeout=self.timeout_sec)
        if resp.status_code != 200:
            return f"Error occurred: {resp.status_code}, {resp.text}", False
        return _decode_from_base64(resp.text), True

    def get_artifacts(self,
                      source: str = 'sqldb',
                      page_index: int = -1,
                      page_size: int = -1,
                      sort_field: str = '',
                      sort_order: str = '',
                      filters: Optional[Dict] = None ) -> Tuple[List[Artifact], str, bool]:
        """
        :param source: from which db to return artifacts, 'sqldb' or 'graphdb'
        :return: first element: list of artifact objs. Artifacts contain also the taxonomies ids and xml content.
                 second element: optional str error message
                 third element: True for success, False for error
        """

        query_params: Dict[str, Any] = _parse_params(page_index, page_size, sort_field, sort_order, filters)

        if source == 'sqldb':
            return self._get_artifacts_from_sql(query_params)
        elif source == 'graphdb':
            return self._get_artifacts_from_graph()
        else:
            return [], f"Didn't recognize source: {source}", False

    def get_artifacts_count(self,
                            source: str = 'sqldb',
                            page_index: int = -1,
                            page_size: int = -1,
                            sort_field: str = '',
                            sort_order: str = '',
                            filters: Optional[Dict] = None) -> Tuple[int, str, bool]:

        query_params: Dict[str, Any] = _parse_params(page_index, page_size, sort_field, sort_order, filters)

        def _get_artifacts_count_from_sql() -> Tuple[int, str, bool]:
            resp = self.session.get(url=self.receiver_url + "/artifacts_count", timeout=self.timeout_sec, params=query_params)
            if resp.status_code != 200:
                return -1, f"Error occurred: {resp.status_code}", False
            objs = json.loads(resp.text)
            return int(objs['artifacts_count']), "", True

        if source == 'sqldb':
            return _handle_request(_get_artifacts_count_from_sql, 'getting artifacts count')
        else:
            return -1, f"Didn't recognize source: {source}", False

    def query_graph(self, query: str, query_type='rw') -> Tuple[str, bool]:
        """
        :return: first element: returned result (as str with format corresponding to what query requests) or error message
                 second element: True for success, False for error
        """
        query_fmt = f'"query": "{query}", "type": "{query_type}"'
        resp = self.session.post(url=self.receiver_url + "/query", data='{' + query_fmt + '}', timeout=self.timeout_sec)
        if resp.status_code != 200:
            return f"Error occurred: {resp.status_code}", False
        return resp.text, True

    def _get_artifacts_from_sql(self, query_params: Dict[str, Any]) -> Tuple[List[Artifact], str, bool]:
        resp = self.session.get(url=self.receiver_url + "/artifacts", timeout=self.timeout_sec, params=query_params)
        if resp.status_code != 200:
            return [], f"Error occurred: {resp.status_code}", False

        objs = json.loads(resp.text)
        artifacts: List[Artifact] = [ArtifactSerialization.from_dict(o) for o in objs]
        return artifacts, "", True

    def _get_artifacts_from_graph(self) -> Tuple[List[Artifact], str, bool]:
        text, ok = self.query_graph('MATCH (a:Artifact) RETURN a.rk_id AS rk_id, a.type as rk_type')
        if not ok:
            return [], text, False

        # the text contains python like list [['<uuid>', '<type'>], ['<uuid>', '<type>']]
        objs = ast.literal_eval(text)
        artifacts: List[Artifact] = [
            ArtifactSerialization.from_dict(
                {'ID': o[0], 'Type': o[1], 'Properties': {}, 'CreatedAt': None, 'TaxonomyFiles': None}
            )
            for o in objs
        ]
        return artifacts, "", True

    def get_tags(self) -> Tuple[List[Dict], str, bool]:
        """
        :return: first element: list of metadata (as Dict), with fields: NamespaceID, Tag, EventID, UpdatedAt
                 second element: error message
                 third element: True for success, False for error
        """

        def _get_tags() -> Tuple[List[Any], str, bool]:
            resp = self.session.get(url=self.receiver_url + "/tags", timeout=self.timeout_sec)
            if resp.status_code != 200:
                return [], f"Error occurred: {resp.status_code}", False
            tags = json.loads(resp.text)
            return tags, 'OK', True

        return _handle_request(_get_tags, "getting tags")


def _handle_request(func: Callable, name: str) -> Tuple[Any, str, bool]:
    """
    Wraps the error, logging and exception handling.
    """
    try:
        obj, msg, ok = func()
        if not ok:
            log.error(msg)
            return "", msg, False
        return obj, 'OK', True

    except RequestException as exc:
        msg = f"{name} connection error: {exc}"
        log.error(msg)
        return '', msg, False


def _parse_params(
        page_index: int = -1,
        page_size: int = -1,
        sort_field: str = '',
        sort_order: str = '',
        filters: Optional[Dict] = None) -> dict:

    if filters is None:
        filters = {}
    query_params: Dict[str, Any] = {}
    if page_index != -1:
        query_params['pageIndex'] = page_index
    if page_size != -1:
        query_params['pageSize'] = page_size
    if sort_field != '':
        query_params['sortField'] = sort_field
    if sort_order != '':
        query_params['sortOrder'] = sort_order

    for key, value in filters.items():
        query_params[key] = value
    return query_params
