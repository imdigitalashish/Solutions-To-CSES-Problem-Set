string = input()

n = len(string)
best = 0
curr = 1

for i in range(1, n):
    # print(f"Checking if {string[i]} != {string[i-1]}")

    if string[i] != string[i - 1]:
        best = max(best, curr)
        # print(f"Assigning best = max (best, curr ) which is {best}")
        curr = 0
        # print("Assining curr = 0")

    curr += 1
    # print("increment curr by one " + str(curr))
    # print()
best = max(best, curr)
# print()
# print(f"Assigning best = max (best, curr ) which is {best}")

print(best)
