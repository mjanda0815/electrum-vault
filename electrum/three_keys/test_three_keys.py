from unittest import TestCase

from electrum.three_keys.script import LockingScript


class TestScripts(TestCase):
    def setUp(self) -> None:
        self.recovery_pub_key = '02ecec100acb89f3049285ae01e7f03fb469e6b54d44b0f3c8240b1958e893cb8c'
        self.instant_pub_key = '0263451a52f3d3ae6918969e1c5ce934743185578481ef8130336ad1726ba61ddb'

        self.random_2keys_pub_key = '02a3bcaf41515051185b05a6c1cda191a519d96797359ea2eca4efbf3af0389eb9'
        self.random_3keys_pub_key = '0322b4675430c8d89f42418bb4e61ad95ece3c89804f482a1be3e206ad86633116'

    def test_2keys_locking_script(self):
        locking = LockingScript(recovery_key=self.recovery_pub_key)
        redeem_script = locking.get_script_for_2keys(self.random_2keys_pub_key)
        self.assertEqual(
 '63516752682102a3bcaf41515051185b05a6c1cda191a519d96797359ea2eca4efbf3af0389eb92102ecec100acb89f3049285ae01e7f03fb469e6b54d44b0f3c8240b1958e893cb8c52ae',
            redeem_script
        )

    def test_3keys_locking_script(self):
        locking = LockingScript(recovery_key=self.recovery_pub_key, instant_key=self.instant_pub_key)
        redeem_script = locking.get_script_for_3keys(self.random_3keys_pub_key)
        self.assertEqual(
'635167635267536868210322b4675430c8d89f42418bb4e61ad95ece3c89804f482a1be3e206ad86633116210263451a52f3d3ae6918969e1c5ce934743185578481ef8130336ad1726ba61ddb2102ecec100acb89f3049285ae01e7f03fb469e6b54d44b0f3c8240b1958e893cb8c53ae',
            redeem_script
        )
