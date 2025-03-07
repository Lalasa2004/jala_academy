try:
    result = 10 / 0
except ArithmeticError as e:
    print("Exception handled:", e)
finally:
    print("Finally block executed")
