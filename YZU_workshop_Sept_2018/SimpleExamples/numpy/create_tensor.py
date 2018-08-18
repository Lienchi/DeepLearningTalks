'''
    This file is part of the September 2018 Workshop at Yuan Ze University.

    You can use these examples in the way you seem fit, though I can't make sure
    it will work fine in your case.
'''
# create tensor
from numpy import array
T = array([
  [[1, 2, 3],    [4, 5, 6],    [7, 8, 9]],
  [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
  [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
  ])

print("\n")
print("shape is: ", T.shape)
print("\n")
print("result is:\n")
print(T)
