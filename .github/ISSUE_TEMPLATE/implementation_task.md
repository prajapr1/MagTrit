---
name: Implementation or Test Task
about: Scope a concrete coding, circuit/model, or test-suite task for contributors
title: "[Task] Concrete deliverable or test suite"
labels: ["good first issue", "help wanted"]
assignees: ""
---

## Target Layer & Path
* **Layer:** (e.g., Gates / ALU / ISA / Firmware / Assembler / IR / Language / Stdlib / Tests)
* **Suggested Path:** (e.g., `hardware/`, `isa/`, `toolchain/assembler/`, `stdlib/`, `tests/`)

## What Needs to Be Built
Describe the exact function, module, truth-table check, or test case needed, including inputs, outputs, and balanced-ternary (`-1`, `0`, `+1`) conventions.

## Acceptance Criteria
- [ ] Handles all valid balanced-ternary (`-1`, `0`, `+1`) inputs and boundary cases
- [ ] Includes unit/golden/property tests verifying expected behavior
- [ ] Documented clearly so other contributors can build on it
