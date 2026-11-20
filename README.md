# MagTrit — Open-Source Ternary Computation Stack

**MagTrit** is an **open-source** project building a full-stack **balanced ternary (`-1`, `0`, `+1`)** computing system from scratch—spanning **gates, ALU, ISA, firmware/VM, assembler, intermediate representation (IR), programming language, standard library, test suites, and hardware**.

## Our Mission

MagTrit does **not** aim to replace binary computing. General-purpose binary hardware and software are deeply mature and remain the right tool for broad everyday workloads.

Instead, our mission is to build **energy-efficient, purpose-built ternary solutions** for domains where native three-state computation has a structural advantage over binary—such as **ternary/quantized AI inference (`{-1, 0, +1}` weights and activations)**, **sparse and zero-gated arithmetic**, **symmetric signed signal processing**, and **three-way decision/control logic**.

## Why Balanced Ternary & Why We're Building This

* **Zero-Gated Energy Efficiency:** In balanced ternary (`-1`, `0`, `+1`), `0` is a first-class neutral state. Hardware and execution layers can natively detect `0` to skip unnecessary switching, multiplication, or memory movement—cutting wasted energy in sparse workloads.
* **Higher Information Density & Simpler Signed Math:** Each trit carries `log2(3) ≈ 1.58` bits of information, reducing interconnect and storage pressure for certain representations. Negation is a trivial symmetric flip (`+1` <-> `-1`) with no separate sign bit or two's-complement asymmetry.
* **End-to-End Co-Design:** Most ternary experiments stop at isolated logic gates or a toy simulator. To make ternary practical for real, energy-sensitive workloads, the entire stack—from physical/logical primitives up to the compiler and runtime—needs to be designed together.
* **Inspired by Binary, Not a Copy of Binary:** We start from a foundational assumption: **we have hardware capable of representing a trit across three distinct values (`-1`, `0`, `+1`)**. We take **inspiration** from proven binary engineering practices (modular layering, structured pipelines, clean toolchains, and rigorous verification) while letting three-state semantics shape our logic, arithmetic, branching, and language design.

## What We Plan to Do

1. **Define & Verify Ternary Primitives:** Formalize 3-state logic gates, noise-margin/hardware assumptions, and a balanced-ternary ALU designed for low-overhead arithmetic and zero-skipping.
2. **Build a Coherent Execution Stack:** Implement a clean ternary ISA, step-traceable VM/firmware runtime, human-readable assembler, and typed IR with native 3-way control flow.
3. **Create a Native Language & Standard Library:** Develop a programming language and standard library with first-class `trit` / `tribool` types and domain helpers for math, codecs, and sparse/ternary kernels.
4. **Benchmark & Validate:** Build comprehensive truth-table, differential, and end-to-end test suites to measure correctness, code density, and energy/operation efficiency against targeted workloads.
5. **Grow an Open Engineering Community:** Welcome contributors with a genuine passion for first-principles engineering across circuit/logic design, computer architecture, firmware, compilers, tooling, and verification.

## Layer-Wise Architecture & Build Scope

1. **Ternary Logic Gates:** STI, PTI, NTI, T-MIN, T-MAX, trit multiplication / consensus primitives, and 3-state signal/noise-margin specs.
2. **ALU (Arithmetic Logic Unit):** Single-trit half/full adders, multi-trit adders/subtractors (`A - B = A + STI(B)`), base-3 shifts/rotations, and 3-state flags (`-1 / 0 / +1`).
3. **ISA (Instruction Set Architecture):** Registers (`ACC`, `PC`, 3-state flags, address/general state), instruction encodings, `LOAD`, `STORE`, `MOV`, `ADD`, `SUB`, `NEG`, `MIN`, `MAX`, `JMP`, 3-way/conditional branches (`BNEG`, `BZERO`, `BPOS`, or 3-target `B3`), and `HALT`.
4. **Firmware & Execution Runtime:** Low-level bring-up routines, memory/register checks, fault/trap handling, I/O drivers, and step-traceable execution runtime.
5. **Assembler & Intermediate Representation (IR):** Human-readable mnemonics, labels, balanced-ternary literals, typed IR (`trit` / `tribool`, words, 3-way branch terminators), and optimization/lowering passes.
6. **Ternary Programming Language:** Syntax, variables, functions, loops, first-class 3-state `trit` / `tribool` types, native 3-way branching, and compiler frontend/codegen.
7. **Programs & Standard Library:** Balanced-ternary math helpers, min/max/signum, base-3 conversions, codecs, buffers, and reference programs.
8. **Testing & Verification:** Truth-table verification, carry/sign-flip edge cases, assembler/IR/compiler golden & differential tests, and end-to-end execution traces.

## Quick Start

```bash
python3 -m unittest discover -s tests -v
python3 isa/vm.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) to get involved.
