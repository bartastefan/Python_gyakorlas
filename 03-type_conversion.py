from datetime import date
birthyear = input("Birth year: ")
# age = 2022 - int(birth_year)
# print(type(birth_year))
# print(type(age))
#birthyear = 1980
datum = date.today()
year = (str(datum)[0:4])
age = (int(year)) - (int(birthyear))
print("Today is " + str(datum))
print("You are " + str(age) + " years old.")
#print("year: " + year)