# Conditions:
# If it's hot -it's a hot day - drink plenty of water
# otherwise if it's cold - it's a cold day - wear warm clothes
# otherwise - it's a lovely day

is_hot = False
is_cold = False

if is_hot: #IF True
    print("It's a hot day,")
    print("drink plenty of water!")
elif is_cold: #IF True; if instead of elif: hot and cold = true, both printed
    print("It's a cold day,")
    print("wear warm clothes!")
else: 
    print("It's a lovely day!")

print("Enjoy your day!")