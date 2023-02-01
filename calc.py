import sys
from pyparsing import nestedExpr

def convert_expression_to_list(input) -> list | int:
  """ Take a given string that satisfies a basic S Expression and convert it
  into a list that is nested as defined by the input.

  :param input: str
  :return: list | int

  >>> convert_expression_to_list("(add 1 2)")
  [['add', '1', '2']]
  >>> convert_expression_to_list("(add (multiply 1 3) (add (multiply 4 2) (multiply 4 5)))")
  [['add', ['multiply', '1', '3'], ['add', ['multiply', '4', '2'], ['multiply', '4', '5']]]]
  """

  if "(" in input and ")" in input:
    nested_parse = nestedExpr('(',')').parseString(input).as_list()
    return nested_parse
  return int(input)

def calculate(input) -> int:
  """ Evaluates the given list of the S expression

  :param input: str
  :return: int

  Addition
  >>> calculate([['add', '1', '2']])
  3
  >>> calculate([['add', '1', '2', '3']])
  6

  Multiplication
  >>> calculate([['multiply', '2', '3']])
  6
  >>> calculate([['multiply', '2', '3', '4']])
  24

  Combination of Addition and Multiplication
  >>> calculate([['add', ['multiply', '1', '3'], ['add', ['multiply', '4', '2'], ['multiply', '4', '5']]]])
  31
  >>> calculate([['add', ['multiply', '1', '3', '2'], ['add', ['multiply', '4', '2'], ['multiply', '4', '5'], '2', '4']]])
  40
  """
  if type(input) is list:
    if len(input) == 1:
      return calculate(input[0])

    method = input[0]

    if method == "multiply":
      value = 1
      for i in input[1:]:
        if int(i) == 0:
          return 0
        value = value * calculate(i)
      return value

    if method == "add":
      value = 0
      for i in input[1:]:
        value = value + calculate(i)
      return value

  return int(input)

if __name__ == "__main__":
  input = sys.argv[1]

  try:
    parsed_input = convert_expression_to_list(input)
    if type(parsed_input) is list:
      calculated = calculate(parsed_input)
      print(calculated)
    else:
      print(parsed_input)
  except:
    print("Could not compute a value from provided input")
