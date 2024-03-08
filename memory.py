class Memory:
    """
        Memory with load/store to bit, byte and word access.
        Access to an unaligned memory address lead to an Exception.
    """

    def __init__(self, mem_size, arch_bits=32):
        self.__mem__ = [False for _ in range(mem_size)]  # each position contains a bit. Init to False
        self.arch_bits = arch_bits
        self.max_int = (2 ** (arch_bits - 1)) - 1
        self.min_int = -1 * (2 ** (arch_bits - 1))

    # ==============================BIT OPERATIONS==============================
    def load_bit(self, addr):
        return self.__mem__[addr]

    def store_bit(self, addr, value: bool):
        self.__mem__[addr] = value

    # ==============================BYTE OPERATIONS=============================
    def load_byte(self, addr):
        # TODO: Check for addr alignment
        return self.__mem__[addr]

    def store_byte(self, addr, value):
        # TODO: Check for addr alignment
        # TODO: Check value range
        self.__mem__[addr] = value

    # ==============================WORD OPERATIONS=============================
    def load_word(self, addr):
        # TODO: Check for addr alignment
        return self.__mem__[addr]

    def store_word(self, addr, value):
        # TODO: Check for addr alignment
        # TODO: Check value range
        self.__mem__[addr] = value

    # ============================VISUAL OPERATIONS=============================

    def print_memory_bits(self, blocking_bits=1, hexa_addr=False):
        print(f"Displaying memory for each {blocking_bits}")

        for addr in range(0, len(self.__mem__), blocking_bits):
            add_srt= hex(add_srt) if hexa_addr else str(addr)
            print(hex(addr), "@", end=" ")
            for value in self.__mem__[addr:addr + blocking_bits]:
                print(int(value), end="")
            print()

    # ============================PRIVATE OPERATIONS============================
    def __check_addr__(self, addr, target_operation=None):
        if addr > len(self.__mem__):
            raise Exception("Out of range access")

    def __convert_to_bits__(self, value: int):
        # Check if it can be represented in the current arch

        # Convert to bit-representation & return

        pass


