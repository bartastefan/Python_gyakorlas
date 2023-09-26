weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You're {converted} kilos.")
else:
    converted = weight / 0.45 #// for rounded value
    print(f"You're {converted} pounds.")
