# QCEQ
(Q)uantum (C)omputation (EQ)uation Solver

A simple equation solver for quantum circuits that outputs the gate transformations of the qubits symbolically (using Dirac notations).

## Why Symbolic Computation?

Symbolic computation deals with the computation of mathematical object symbolically. ([From: SymPy documentation](https://docs.sympy.org/latest/tutorial/intro.html) )This means that the mathematical expressions are not reduced to approximations, and are represented using algebraic symbols, which replicates how equations are solved by humans.

## Why Symbolic Computation for Quantum Computing?

The complexity of Quantum Circuits increase exponentially with a linear increase in the number of Qubits. Therefore, any sufficiently complex Quantum Circuit requires a tedious amounts of manual labor to break down the mathematical transformations implemented by the Quantum Gates. **QCEQ** wishes to remove this barrier of entry for Quantum Computations and make Quantum Computation accessible to busy individuals that might be detterred by the time commitment necessary for manual computations.
