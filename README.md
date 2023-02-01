# Simple S Expression Calculator

This script is able to calculate simple nested S Expressions https://en.wikipedia.org/wiki/S-expression.
It is dependant on the `pyparsing` library.

The calculator accepts only two operations at this time, `add` and `multiply` but can easily be expanded to support other operations such as `exponent`.

Each operation accepts an arbitrary number of inputs.

The script can be run from the root directory:
  `py .\calc.py "(add (multiply 1 3) (add (multiply 4 2) (multiply 4 5)))"`
