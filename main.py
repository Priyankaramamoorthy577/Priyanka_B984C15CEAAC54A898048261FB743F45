number = int(input("enter a value: "))
fact = 1
for i in range(1, number + 1):
  fact = fact * i
print("The factorial of %d %d" % (number, fact))
