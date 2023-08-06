import time
import logging
import datetime
from uuid import UUID, uuid1
from typing import Dict, Any, Optional, Tuple, Callable
from importlib.metadata import version
from urllib3.exceptions import InsecureRequestWarning

import requests
from requests.exceptions import RequestException

from rkclient.entities import PEM, Artifact
from rkclient.serialization import PEMSerialization, _encode_as_base64

log = logging.getLogger("rkclient")
RK_VERSION = version('RecordKeeper_Client')


def add_pem_context(files: Dict[str, Any], pem: PEM):
    files['rk_context'] = pem.ID.hex


# request == Flask request
def get_pem_from_request(request) -> Optional[UUID]:
    rk_context = request.files.get('rk_context', None)
    if rk_context is None:
        return None
    pem_id: str = rk_context.stream.read().decode("UTF8")
    return UUID(hex=pem_id)


class RKClient:
    """
        All network functions return tuple [str, bool]
        If bool is False, str contains error description

        Errors are also logged to rkclient logger

    """

    def __init__(self, receiver_url: str, emitter_id: Optional[UUID] = None, timeout_sec: int = 5, insecure: bool = True):
        self.receiver_url = receiver_url.rstrip('/')
        if emitter_id is None:
            emitter_id = uuid1()
        self.emitter_id = emitter_id
        self.timeout_sec = timeout_sec
        self.session = requests.Session()
        log.info(f"ver {RK_VERSION}, connecting to: {self.receiver_url}")
        if insecure:
            self.session.verify = False
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
            log.warning("Disabled SSL certificate check")

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    @staticmethod
    def get_version() -> str:
        """
        :return: Version of RKClient
        """
        return RK_VERSION

    def prepare_pem(self,
                    type: str,
                    predecessor_id: Optional[UUID] = None,
                    properties: Optional[Dict] = None,
                    tag_name: str = 'latest',
                    tag_namespace: Optional[UUID] = None) -> PEM:
        """
        In memory creation of PEM
        :param type: user defined type of event
        :param predecessor_id: pass None if this event doesn't have a predecessor
        :param properties:
        :param tag_name:
        :param tag_namespace:
        :return: new PEM
        """
        uid = uuid1()
        now = datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        pem = PEM(uid, type, predecessor_id, self.emitter_id, now)
        if properties is not None:
            pem.Properties = properties
        pem.Tag = tag_name
        if tag_namespace is None:
            pem.TagNamespace = self.emitter_id.hex
        else:
            pem.TagNamespace = tag_namespace.hex
        return pem

    def prepare_artifact(self,
                         type: str,
                         properties: Dict[str, str],
                         uid: Optional[UUID] = None) -> Artifact:
        """
        In memory creation of Artifact. It needs to be passed to PEM.add_uses/produces_artifact()
        :param type:
        :param properties:
        :param uid:
        :return: new Artifact
        """
        if uid is None:
            uid = uuid1()
        art = Artifact(uid, type, properties)
        return art

    def send_pem(self, pem: PEM) -> Tuple[str, bool]:
        """
        Sends PEM to Record Keeper.
        :return: check class description
        """
        payload: str = PEMSerialization.to_json(pem)

        def _send_pem():
            return self.session.post(url=self.receiver_url + "/pem", data=payload, timeout=self.timeout_sec)
        log.debug(f"sending PEM: {payload}")
        return _handle_request(_send_pem, "sending PEM")

    def ping(self) -> Tuple[str, bool]:
        """
        :return: check class description
        """
        def _ping():
            return self.session.get(url=self.receiver_url + "/ping", timeout=self.timeout_sec)
        return _handle_request(_ping, "pinging")

    def get_info(self) -> Tuple[str, bool]:
        """
        Returns json with 'postgres_enabled' and 'neo4j_enabled' bools, and 'version' with string semver
        :return: check class description
        TODO: return object instead of str
        """
        def _get_info():
            return self.session.get(url=self.receiver_url + "/info", timeout=self.timeout_sec)
        return _handle_request(_get_info, "getting info", True)

    def get_tag(self, namespace: UUID, tag_name: str) -> Tuple[str, bool]:
        """
        Returned tag is UUID in hex (do: UUID(hex=result))
        :return: check class description
        """
        tag_base64 = _encode_as_base64(tag_name)

        def _get_tag():
            return self.session.get(url=self.receiver_url + f"/tag/{namespace.hex}/{tag_base64}", timeout=self.timeout_sec)
        return _handle_request(_get_tag, "getting tag", True)

    def set_tag(self, namespace: UUID, tag_name: str, pem: PEM) -> Tuple[str, bool]:
        """
        Sets tag_name on pem.ID, within namespace
        :param tag_name: can contain space, / and other characters, but recommended charset: is A-Za-z0-9_-
        :param namespace:
        :param pem:
        :return: check class description
        """
        tag_base64 = _encode_as_base64(tag_name)

        def _set_tag():
            return self.session.post(url=self.receiver_url + f"/tag/{namespace.hex}/{tag_base64}/{pem.ID.hex}", timeout=self.timeout_sec)
        return _handle_request(_set_tag, "setting tag")


def _handle_request(func: Callable, name: str, ret_text_on_ok: bool = False) -> Tuple[str, bool]:
    """
    Wraps the error, logging and exception handling.
    """
    try:
        resp = func()
        if resp.status_code != 200:
            msg = f"{name} failed: {resp.status_code}: {resp.text}"
            log.error(msg)
            return msg, False
        if ret_text_on_ok:
            return resp.text, True
        else:
            return 'OK', True

    except RequestException as exc:
        msg = f"{name} connection error: {exc}"
        log.error(msg)
        return msg, False
