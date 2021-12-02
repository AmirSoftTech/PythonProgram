from collections import deque
#Queue Fist In Firt Out (FIFO) Serve
bank = deque(["A", "B", "C", "D", "E", "F", "G"])
print("Queue List:")
for i in bank:
    print(i, end="  ")

for x in range(3):# How many times pop in the list?
    bank.popleft()

print("\n-----------------------------")
print("After popleft queue list here:")
for i in bank:
    print(i, end="  ")

if not bank:
    print("No Item left")


