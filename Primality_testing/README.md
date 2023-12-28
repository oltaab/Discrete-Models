# Miller-Rabin Primality Test

## Overview
This folder contains a Python implementation of the Miller-Rabin primality test, a probabilistic algorithm used to determine if a number is prime. It's particularly effective for large integers and is widely used in cryptographic applications.

## Files
- `primality.py`: The main Python script containing the implementation of the Miller-Rabin test and necessary auxiliary functions like fast modular exponentiation and finding `k` and `m`.

## Features
- **Fast Modular Exponentiation**: Efficiently calculates bases raised to high powers modulo a number.
- **Adaptive Rounds**: Allows specifying the number of rounds for the test, balancing speed and accuracy.
- **Probabilistic Primality Testing**: Implements the Miller-Rabin test to check if numbers are likely prime.

## Contributing
Feel free to fork the repository, make changes, or suggest improvements by creating issues or pull requests.


