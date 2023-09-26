# logical operators (and, or, not...)
# has_high_income = False
# has_good_credit = True
# if has_high_income and has_good_credit:
#    print("Eligible for loan")

# temperature = 30
# > < >= <= != == (= is for statements, not the operators)
# if temperature > 30:
#    print("It's a hot day.")
# elif temperature < 10:
#    print("It's a cold day.")
# else:
#    print("It's neither hot or cold.")

# exercise: if name less than 3 characters long: name must be at least 3 character
# otherwise if it's more than 50 characters long: name can be a maximum of 50 characters
# otherwise: name looks good!

name = input(str("Please enter a name (min:3, max:50 chr): "))
name_length = len(name)
# print (str(name_length))
if name_length < 3:
    print (f"you've entered {name_length} chr long name, the name must be at least 3 character")
elif name_length > 50:
    print (f"you've entered {name_length} chr long name, the name can be a maximum of 50 characters")
else:
    print("name looks good!")
