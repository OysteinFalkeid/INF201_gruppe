from Exercise_9 import Complex, Immaginary

# Add opperation
print('1 ', Complex(-4.06, 3.89) + Complex(1.7, -1.75))

# Subtract opperation
print('2 ', Complex(-3.68, -4.28) - Complex(2.91, -1.32))

# Multiplication opperation
print('3 ', Complex(-4.34, 2.6) * Complex(-0.52, 3.7))

# Devition opperation
print('4 ', Complex(-0.87, 1.73) / Complex(-3.34, 3.42))

# All opperations are supported by both real and complex numbers
print('5 ', 1 + Complex(-3.12, -2.81))
print('6 ', Complex(0.19, -4.48) + 1)
print('7 ', 1 - Complex(-1.68, 0.83))
print('8 ', Complex(-0.12, -3.54) - 1)
print('9 ', 1 * Complex(-1.15, -4.52))
print('10 ', Complex(-3.84, -4.53) * 1)
print('11 ', 1 / Complex(-1.35, 1.25))
print('12 ',Complex(-4.55, -2.29) / 1)

# The class also handles strictley imaginary numbers
print('13 ', Complex(0, 3.52) + Complex(0, 4.14))
print('14 ', Complex(0, -1.84) - Complex(0, -1.91))
print('15 ', Complex(0, -4.03) * Complex(0, -0.9))
print('16 ', Complex(0, 1.2) / Complex(1, 3.54)) # changed to 1 instead of 0, else division by zero

# Conjugate
print('17 ', Complex(2, 2).__conj__())

# Constant value add/sub/mul/div
print('18 ', Complex(2,-3) + 4 + Immaginary(2))
print('19 ', Complex(2,-3) - 4 - Immaginary(2))
print('20 ', Complex(2,-3) * 4)
print('21 ', Complex(2,-3) / 4)

