print("Please entre your current earth weight: ")
weight = input()

print("\nI have information for the following plantes: \n\n")
print(" 1. Venus  2. Mars   3. Jupiter\n")
print(" 4. Saturn 5. Uranus 6. Neptune\n")

print("Which planet are you visiting? ")
x = input()

if (x == 1):
    weight *= 0.78
elif (x == 2):
    weight *= 0.39
elif (x == 3):
    weight *= 2.65
elif (x == 4):
    weight *= 1.17
elif (x == 5):
    weight *= 1.05
elif (x == 6):
    weight *= 1.23
else:
    print("Not a valid planet.")

print("Your weight would be %r pounds on that planet" % (weight))
