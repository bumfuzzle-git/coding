import time

i = int(input("how much money do you have?: "))

while i >= 2:
	print("You are rich")
	i -= 1
	print("but now you only have")
	print(i)
	time.sleep(0.400)
else:
	print("you were rich, but now you are poor !!")

print("i have taken all your money, goodbye")
print("the rest ist yours")
