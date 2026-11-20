# Layer 2: Balanced Ternary ALU

* Place values use powers of `3`: `..., 27, 9, 3, 1`.
* Single-trit addition of two trits (`-1, 0, +1`) plus carry-in (`-1, 0, +1`) produces a `sum` trit and a `carry` trit in `{-1, 0, +1}`.
* Subtraction `A - B` is performed via `A + STI(B)` without two's complement conversion.
