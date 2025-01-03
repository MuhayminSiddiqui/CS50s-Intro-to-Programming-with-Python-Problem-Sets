expression = input("Expression: ")
x, y, z = expression.split(" ")
x, z = float(x), float(z)

if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/" and z != 0:
    print(f"{x / z:.1f}")
else:
    print("Error: Invalid Input")