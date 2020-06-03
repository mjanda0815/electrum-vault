from electrum.bitcoin import opcodes, var_int


def _get_var_int_of_key(key: str) -> bytes:
    byte_string = bytes.fromhex(key)
    key_len = var_int(len(byte_string))
    return bytes.fromhex(key_len)


class LockingScript:
    def __init__(self, recovery_key: str, instant_key: str = None):
        self.recovery_key = recovery_key
        self.recovery_key_len_in_var_int: bytes = _get_var_int_of_key(recovery_key)
        self.instant_key = instant_key
        if instant_key is not None:
            self.instant_key_len_in_var_int: bytes = _get_var_int_of_key(instant_key)

    def is_instant(self):
        return self.instant_key is not None

    def get_script_for_2keys(self, pub_key: str) -> str:
        pub_key_var_len = _get_var_int_of_key(pub_key)

        script = (
            bytes([opcodes.OP_IF]) +
            bytes([opcodes.OP_1]) +
            bytes([opcodes.OP_ELSE]) +
            bytes([opcodes.OP_2]) +
            bytes([opcodes.OP_ENDIF]) +

            pub_key_var_len +
            bytes.fromhex(pub_key) +

            self.recovery_key_len_in_var_int +
            bytes.fromhex(self.recovery_key) +

            bytes([opcodes.OP_2]) +
            bytes([opcodes.OP_CHECKMULTISIG])
        )
        return script.hex()

    def get_script_for_3keys(self, pub_key: str) -> str:
        pub_key_var_len = _get_var_int_of_key(pub_key)

        script = (
                bytes([opcodes.OP_IF]) +
                bytes([opcodes.OP_1]) +
                bytes([opcodes.OP_ELSE]) +
                bytes([opcodes.OP_IF]) +
                bytes([opcodes.OP_2]) +
                bytes([opcodes.OP_ELSE]) +
                bytes([opcodes.OP_3]) +
                bytes([opcodes.OP_ENDIF]) +
                bytes([opcodes.OP_ENDIF]) +

                pub_key_var_len +
                bytes.fromhex(pub_key) +

                self.instant_key_len_in_var_int +
                bytes.fromhex(self.instant_key) +

                self.recovery_key_len_in_var_int +
                bytes.fromhex(self.recovery_key) +

                bytes([opcodes.OP_3]) +
                bytes([opcodes.OP_CHECKMULTISIG])
        )
        return script.hex()
