from collections import namedtuple
from typing import List
from unittest import TestCase

from electrum import Transaction
from electrum.three_keys.multisig_generator import MultisigScriptGenerator

class DummyGenerator(MultisigScriptGenerator):

    def get_redeem_script(self, public_keys: List[str]) -> str:
        pass

    def get_script_sig(self, signatures: List[str], public_keys: List[str]) -> str:
        pass


class Test2KeysTransaction(TestCase):
    def test_setting_multisig_generator(self):
        tr = Transaction(None)
        generator = DummyGenerator()
        tr.multisig_script_generator = generator
        self.assertTrue(generator is tr.multisig_script_generator)

    def test_failed_multisig_setting(self):
        Gen = namedtuple('Gen', ['a', 'b'])
        generator = Gen(1, 1)
        tr = Transaction(None)
        with self.assertRaises(TypeError) as error:
            tr.multisig_script_generator = generator

        self.assertEqual(
            'Cannot set multisig_script_generator. It has to be MultisigScriptGenerator',
            str(error.exception)
        )
