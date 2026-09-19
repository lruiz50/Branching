hours = int(input("Enter the KW hours used: "))

if hours <= 1000 :
    amount = (hours * 7.633) / 100
else :
    amount = ((1000 * 7.633) + ((hours - 1000) * 9.259)) / 100
print("Amounted owed is %.2f" % amount)
