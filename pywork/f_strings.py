# reference w3schools python ref string format

person = "Dave"
coins = 3

print("\n" + "Message0: " + person + " has " + str(coins) + " coin(s) left")

message1 = "\n Message1: %s has %s coin(s) left" %(person, coins)
print(message1)

message2 = "\n Message2: {} has {} coin(s) left".format(person, coins)
print(message2)

message3 = "\n Message3: {1} has {0} coin(s) left".format(coins, person)
print(message3)

message4 = "\n Message4: {person} has {coins} coin(s) left".format(coins=coins, person=person)
print(message4)

player = {"person": "Dave", "coins": 3}

message5 = "\n Message5: {person} has {coins} coin(s) left".format(**player)
print(message5)

#f-string examples

message6 = f"\n Message6: {person} has {coins} coin(s) left"
print(message6)

message7 = f"\n Message7: {person} has {2*5} coin(s) left"
print(message7)

message8 = f"\n Message8: {person.lower()} has {2*5} coin(s) left"
print(message8)

message9 = f"\n Message9: {player['person']} has {2*5} coin(s) left"
print(message9)

# formatting options

num = 18
print(f"\n2.25 time {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"2.25 time {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.32 {num / 4.32:.2%}")