# Part 2 example program

| Opcode / operand | Instruction | Effect                             | Notes                |
|------------------|-------------|------------------------------------|----------------------|
| `0 3`            | `adv 3`     | A = (A ÷ 2^3) = (A ÷ 8) = (A >> 3) | shift A right 3 bits |
| `5 4`            | `out A`     | output (A % 8)                     |                      |
| `3 0`            | `jnz 0`     | go to zero, if A ≠ 0               |                      |

Converts (A ÷ 8) to octal, reversed, with a trailing zero.

# Puzzle input program

| Opcode / operand | Instruction | Effect                             | Notes                   |
|------------------|-------------|------------------------------------|-------------------------|
| `2 4`            | `bst A`     | B = (A % 8)                        | lowest 3 bits of A      |
| `1 7`            | `bxl 7`     | B = (B xor 7) = (7 - B)            | flip each bit           |
| `7 5`            | `cdv B`     | C = (A ÷ 2^B) = (A >> B)           | shift A right by B bits |
| `0 3`            | `adv 3`     | A = (A ÷ 2^3) = (A ÷ 8) = (A >> 3) | shift A right 3 bits    |
| `1 7`            | `bxl 7`     | B = (B xor 7) = (7 - B)            | flip each bit           |
| `4 1`            | `bxc`       | B = (B xor C)                      |                         |
| `5 5`            | `out B`     | output (B % 8)                     |                         |
| `3 0`            | `jnz 0`     | go to zero, if A ≠ 0               |                         |

* The program is 16 3-bit numbers long.
* Each iteration shifts A right by 3 bits.
* After the first two instructions, 0 ≤ B ≤ 7.
* After the 3rd instruction, C contains A shifted right by at most 7 bits.
* The output depends on the lowest 3 bits of B and C.

In the "worst case", if B is 7:

```
                                      │ ┌───────────────────────────┐
                                      │ │                           v
┌───┬───┬───┬───┬───┬───┐     ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│    15     │  14       │ ┄┄┄ │     3     │     2     │     1     │     0     │
└───┴───┴───┴───┴───┴───┘     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                                      │         │                           ^
                                      │         └───────────────────────────┘
```

So the value output during each iteration may depend on bit 9 - not necessarily just bits 0-2.

* The most significant 3-bit number must have at least 1 bit set, or the program would not run for 16 iterations.
* No bit higher than 47 (most significant bit of the most significant number) can be set, or the program would run for **more** than 16 iterations.
