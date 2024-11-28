from Exercise_9 import Complex

# Add opperation
print(Complex(-4.06, 3.89) + Complex(1.7, -1.75))

# Subtract opperation
print(Complex(-3.68, -4.28) - Complex(2.91, -1.32))

# Multiplication opperation
print(Complex(-4.34, 2.6) * Complex(-0.52, 3.7))

# Devition opperation
print(Complex(-0.87, 1.73) / Complex(-3.34, 3.42))

# All opperations are supported by both real and complex numbers
print(1 + Complex(-3.12, -2.81))
print(Complex(0.19, -4.48) + 1)
print(1 - Complex(-1.68, 0.83))
print(Complex(-0.12, -3.54) - 1)
print(1 * Complex(-1.15, -4.52))
print(Complex(-3.84, -4.53) * 1)
print(1 / Complex(-1.35, 1.25))
print(Complex(-4.55, -2.29) / 1)

# The class also handles strictley imaginary numbers
print(Complex(0, 3.52) + Complex(0, 4.14))
print(Complex(0, -1.84) - Complex(0, -1.91))
print(Complex(0, -4.03) * Complex(0, -0.9))
print(Complex(0, 1.2) / Complex(0, 3.54))



