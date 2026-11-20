import unittest
from hardware.gates import sti, pti, nti, t_min, t_max, full_adder_trit
from isa.vm import Instruction, run_vm


class TestTernaryPrimitives(unittest.TestCase):
    def test_sti_and_extrema(self):
        self.assertEqual(sti(-1), 1)
        self.assertEqual(sti(0), 0)
        self.assertEqual(sti(1), -1)
        self.assertEqual(t_min(1, -1), -1)
        self.assertEqual(t_max(1, 0), 1)
        self.assertEqual(pti(1), -1)
        self.assertEqual(nti(-1), 1)

    def test_full_adder_carry_balancing(self):
        self.assertEqual(full_adder_trit(1, 1, 0), (-1, 1))
        self.assertEqual(full_adder_trit(-1, -1, 0), (1, -1))
        self.assertEqual(full_adder_trit(1, 0, -1), (0, 0))

    def test_vm_branch_and_sub(self):
        prog = [
            Instruction("LOAD", 5),
            Instruction("ADD", -2),
            Instruction("SUB", 4),
            Instruction("BNEG", 5),
            Instruction("ADD", 10),
            Instruction("HALT", 0),
        ]
        self.assertEqual(run_vm(prog, trace=False), -1)


if __name__ == "__main__":
    unittest.main()
