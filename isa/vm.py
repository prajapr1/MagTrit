"""Minimal balanced-ternary virtual machine."""

from dataclasses import dataclass


@dataclass
class Instruction:
    op: str
    operand: int = 0


def run_vm(program: list[Instruction], trace: bool = True) -> int:
    acc = 0
    pc = 0
    steps = 0

    while 0 <= pc < len(program) and steps < 1000:
        steps += 1
        instr = program[pc]
        sign = -1 if acc < 0 else (1 if acc > 0 else 0)
        if trace:
            print(f"PC={pc:02d} | {instr.op:5s} {instr.operand:+3d} | ACC={acc:+4d} | SIGN={sign:+d}")

        if instr.op == "HALT":
            break
        elif instr.op == "LOAD":
            acc = instr.operand
            pc += 1
        elif instr.op == "ADD":
            acc += instr.operand
            pc += 1
        elif instr.op == "SUB":
            acc -= instr.operand
            pc += 1
        elif instr.op == "NEG":
            acc = -acc
            pc += 1
        elif instr.op == "JUMP":
            pc = instr.operand
        elif instr.op == "BNEG":
            pc = instr.operand if acc < 0 else pc + 1
        elif instr.op == "BZERO":
            pc = instr.operand if acc == 0 else pc + 1
        elif instr.op == "BPOS":
            pc = instr.operand if acc > 0 else pc + 1
        else:
            raise ValueError(f"Unknown opcode: {instr.op}")

    return acc


if __name__ == "__main__":
    demo = [
        Instruction("LOAD", 5),
        Instruction("ADD", -2),
        Instruction("SUB", 4),
        Instruction("BNEG", 5),
        Instruction("ADD", 10),
        Instruction("HALT", 0),
    ]
    final_val = run_vm(demo)
    print(f"Final ACC: {final_val:+d}")
