value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 1:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print('Value is now is ' + str(value))

names = ["Dave", "Sara", "John"]
# for name in names:
#     print(name)

# for x in "Mississipi":
#     print(x)

# for name in names:
#     if name == "Sara":
#         break
#     print(name)

# for name in names:
#     if name == "Sara":
#         continue
#     print(name)

# for x in range(4):
#     print(x)

# print("\n")
# for x in range(2, 4):
#     print(x)

# for x in range(0, 50, 5):
#     print(x)
# else:
#     print("Glad that\'s over")

actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
