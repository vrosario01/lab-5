def pythagorean_triples( a, b, c):
  """ 
  signature: number^2 + number^2 = number^2  --> Boolean
  explanation: pythagorean triples takes in parameter a b and c and if a^2 + b^2 = c^2 then returns true if not the function returns it false
  doctests: 
  >>> print(pythagorean_triples(3,4,5))
  True
  >>> print(pythagorean_triples(6,4,8))
  False
  >>> print(pythagorean_triples(3,3,3))
  False
  """
  if  a**2 + b**2 == c**2:
    return True
  else:
    return False
