import beverages

print (dir(beverages))

no_of_family_members = int(input('How many people do u want ot serve'))

names = []
wants_sugar = []

for i in range(no_of_family_members):
    names.append(input("Whats family member name: "))
    wants_sugar.append(int(input("whats his/her preference (1:yes, 0: no): ")))

teas = beverages.family(names, wants_sugar)

for tea in teas:
    print(tea)

    