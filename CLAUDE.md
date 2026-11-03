# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A small interactive terminal program, written for a cybersecurity/pentesting with Python course. It asks the user for an integer and says whether it is prime. All of the code is in `numero_primo.py`, which has no third-party dependencies, no build step, no tests, and no linter config. It is licensed under AGPL-3.0.

## Running

```
python numero_primo.py
```

Requires Python 3.10+ because of the `int | None` annotation syntax. The program reads from stdin. To run it without typing input: `echo 7 | python numero_primo.py`.

## Code structure

- `mostrar_instrucciones()` prints the banner using ANSI color constants (`CIAN`, `AMARILLO`, `RESET`). On Windows it calls `os.system("")` first to turn on ANSI escape support in the console. Keep this call if you change the output.
- `dame_numero()` reads input and converts it to `int`. It returns `None` when the input is not numeric, and `main()` then asks again.
- `es_primo()` does the primality test by trial division with odd divisors up to √n. Numbers ≤ 1 are not prime.
- `main()` loops until it gets a valid number, classifies it with `es_primo()`, and exits after one answer. The entry point catches `KeyboardInterrupt` and `EOFError` and prints "Juego terminado."
- The commented-out `MINIMO`/`MAXIMO`/`random.randint` lines and the unused `import random` come from a number-guessing game template this file was adapted from.

## Conventions

User-facing text, identifiers, and comments are in Spanish. Keep new code consistent with that.
