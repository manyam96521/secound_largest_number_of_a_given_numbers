x=int(input("enter x value: "))
y=int(input("enter y value: "))
z=int(input("enter z value: "))
if x>y and x<z:
    print(f"x={x} is the secound largest number in the given numbers")
elif y>x and y<z:
    print(f"y={y} is the secound largest number in the given numbers")
else:
    print(f"z={z} is the secound largest number in the given numbers")