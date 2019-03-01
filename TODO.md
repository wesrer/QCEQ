# QCEQ TODOs:

## Known Bugs

- Gate to Matrix transformation does not work for multi-qubit gates 
  if all the source qubits are not in order
- Qubit transformations don't work if the target qubit is above the source qubit (i.e, the matrix transformations right
now aren't complicated enough to handle different kinds of grammar - CX only means the source is above the target_qubit)

- Right now, the extra parameters that define the source qubit and the target qubit don't even mean anything - The
operations default to a natural behavior - i.e. start from this qubit - everything other than the last qubit is a source
qubit, but the last qubit is the target qubit

## Features

### Urgent

- Gate JSON parser
- Generating Strings from Qubit Notation
- Implementing Gate Transformations

### Short term

### Long term

### Someday

## To Test

## Being Tested

## Recent Bugfixes