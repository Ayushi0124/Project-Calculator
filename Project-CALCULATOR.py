A = int(input('Enter the first number : '))
B = int(input('Enter the second number : '))
C = input('Enter your operation : ')
if C == '+':
    print(A + B)
elif C == '-':
    print(A - B)
elif C == '*': # * means multiplication in python
    print(A * B)
elif C == '/': # / means division in python
    print(A / B)
elif C == '%': # % means modulus in python
    print(A % B) 
elif C == '**': # ** means exponentiation in python
    print(A ** B)
elif C == '//': # // means floor division in python
    print(A // B)
elif C == 'sqrt': # sqrt means square root in python
    print(A ** 0.5)
elif C == 'log': # log means logarithm in python
    import math
    print(math.log(A))
elif C == 'sin': # sin means sine in python
    import math
    print(math.sin(A))
elif C == 'cos': # cos means cosine in python
    import math
    print(math.cos(A))
elif C == 'tan': # tan means tangent in python
    import math
    print(math.tan(A))
elif C == 'factorial': # factorial means factorial in python
    import math
    print(math.factorial(A))
elif C == 'gcd': # gcd means greatest common divisor in python
    import math
    print(math.gcd(A, B))
elif C == 'lcm': # lcm means least common multiple in python
    import math
    print(math.lcm(A, B))
elif C == 'abs': # abs means absolute value in python
    print(abs(A))
elif C == 'round': # round means rounding in python
    print(round(A))
elif C == 'ceil': # ceil means ceiling in python
    import math
    print(math.ceil(A))
elif C == 'floor': # floor means flooring in python
    import math
    print(math.floor(A))
elif C == 'degrees': # degrees means converting radians to degrees in python
    import math
    print(math.degrees(A))
elif C == 'radians': # radians means converting degrees to radians in python
    import math
    print(math.radians(A))
elif C == 'exp': # exp means exponential in python
    import math
    print(math.exp(A))
elif C == 'log10': # log10 means logarithm base 10 in python
    import math
    print(math.log10(A))
elif C == 'log2': # log2 means logarithm base 2 in python
    import math
    print(math.log2(A))
elif C == 'sinh': # sinh means hyperbolic sine in python
    import math
    print(math.sinh(A))
elif C == 'cosh': # cosh means hyperbolic cosine in python
    import math
    print(math.cosh(A))
elif C == 'tanh': # tanh means hyperbolic tangent in python
    import math
    print(math.tanh(A))
elif C == 'asinh': # asinh means inverse hyperbolic sine in python
    import math
    print(math.asinh(A))
elif C == 'Fibonacci' : 
    n = int("Enter the number of terms:")
    a = 0
    b = 1
     for i in range(n):
         print(a, end="")
         a,b = a+b
elif C == 'prime':
   n=int(input('Enter a number:'))
    if n>1:
    for i in range(2,n):
        if n % i == 0:
            print('Not a prime number')
            break
        else:
            print('Prime number")
        else:
            print('Not a prime number')
    print("Something went wrong, please check your input and try again.")
