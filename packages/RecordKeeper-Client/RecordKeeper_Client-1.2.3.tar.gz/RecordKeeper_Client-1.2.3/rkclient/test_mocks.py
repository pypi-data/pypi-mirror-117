import os
import unittest
import uuid
import json
import responses
from uuid import UUID

from rkclient import RKClient, RKClientFactory


class TestAPI(unittest.TestCase):

    def test_rk_factory(self):
        os.environ['RK_MOCK'] = 'true'
        rk = RKClientFactory.get('', )
        del os.environ['RK_MOCK']

        pred = rk.prepare_pem('', None)
        self.assertIsNotNone(pred)

        pem = rk.prepare_pem('some_type_name', pred.ID, { "value_int": -123 })
        self.assertIsNotNone(pem)

        _, ok = rk.send_pem(pred)
        self.assertTrue(ok)

        _, ok = rk.ping()
        self.assertTrue(ok)

        _, ok = rk.get_info()
        self.assertTrue(ok)

        test_uuid = UUID("a606c8ea-39a1-11eb-8ad5-0a9a235141b1")
        _, ok = rk.get_tag(test_uuid, 'foo')
        self.assertTrue(ok)

        test_uuid = UUID("a606c8ea-39a1-11eb-8ad5-0a9a235141b1")
        _, ok = rk.set_tag(test_uuid, 'bar', pem)
        self.assertTrue(ok)

        _, ok = rk.get_info()
        self.assertTrue(ok)

    def test_rk_factory_default(self):
        rk = RKClientFactory.get('', )
        pem = rk.prepare_pem('', None)
        self.assertIsNotNone(pem)

        _, ok = rk.send_pem(pem)
        self.assertFalse(ok)

    def test_prepare_pem(self):
        emitter_id = uuid.uuid4()
        rk = RKClient('', emitter_id)
        pred = rk.prepare_pem('', None)
        pem = rk.prepare_pem('some_type_name', pred.ID, { "value_int": -123 })

        self.assertIs(type(pem.ID), UUID)
        self.assertEqual(pem.Predecessor, pred.ID)
        self.assertEqual(pem.Emitter, emitter_id)
        self.assertEqual(pem.Properties["value_int"], -123)

    @responses.activate
    def test_send_pem_ok(self):
        def request_callback(request):
            resp_body = "ack getting some_type_name"
            headers = {}
            return 200, headers, json.dumps(resp_body)

        responses.add_callback(
            responses.POST, 'http://localhost:8082/pem',
            callback=request_callback,
            content_type='application/json',
        )

        emitter_id = uuid.uuid4()
        rk = RKClient('http://localhost:8082/', emitter_id)

        pem = rk.prepare_pem('some_type_name', None)
        msg, ok = rk.send_pem(pem)
        self.assertEqual(ok, True, msg=msg)

    @responses.activate
    def test_send_pem_error(self):
        def request_callback(request):
            resp_body = "PEM is not valid: Type is empty"
            headers = {}
            return 400, headers, json.dumps(resp_body)

        responses.add_callback(
            responses.POST, 'http://localhost:8082/pem',
            callback=request_callback,
            content_type='application/json',
        )

        emitter_id = uuid.uuid4()
        rk = RKClient('http://localhost:8082/', emitter_id)

        pem = rk.prepare_pem('', None)
        msg, ok = rk.send_pem(pem)
        self.assertEqual(ok, False, msg=msg)
