# Contributing to MagTrit

Welcome to **MagTrit**—an open-source project building a full-stack **balanced ternary (`-1`, `0`, `+1`)** computing system from scratch across **gates, ALU, ISA, firmware/runtime, assembler, intermediate representation (IR), programming language, standard library, test suites, and hardware**.

Our goal is **not** to replace general-purpose binary computing, but to create **energy-efficient, purpose-built ternary solutions** for workloads where native three-state computation shines (such as quantized/ternary AI inference, sparse zero-gated arithmetic, and 3-way control logic). We start from a clear assumption: **we have hardware capable of representing a trit across three distinct values (`-1`, `0`, `+1`)**. We do **not** copy binary designs—we **take inspiration from binary** where proven engineering discipline helps (clear interfaces, modular layers, compiler structure, and thorough testing) while letting three-state logic and three-way semantics drive the design.

We are looking for engineers with a genuine passion for building and problem-solving from first principles.

## Core Design Principles

1. **Three-State Native First:** Design around balanced trits (`-1`, `0`, `+1`) rather than retrofitting binary two's complement or two-state habits onto three values.
2. **Inspired by Binary, Not a Copy of Binary:** Learn from how mature binary systems organize tooling, verification, and pipelines, but question every binary assumption before adopting it.
3. **Explicit Assumptions & Trade-Offs:** State hardware assumptions, trit/word widths, carry/overflow rules, and noise-margin or complexity trade-offs plainly in every spec and PR.
4. **Test What You Build:** Include truth tables, edge cases (such as carry cascades across `+1` / `-1`, zero crossings, and branch boundaries), or automated tests alongside code and spec changes.

## Pull Request Checklist

* [ ] Clearly states which MagTrit layer(s) are touched.
* [ ] Respects balanced ternary (`-1`, `0`, `+1`) and avoids blindly copying binary conventions where a native ternary approach fits better.
* [ ] Includes truth tables, examples, or unit/differential tests for new behavior or edge cases.
* [ ] Updates relevant documentation in `docs/` or `README.md` if interfaces or formats change.
