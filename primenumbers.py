import math
import itertools

range = lambda stop: iter(itertools.count().next, stop)

#############################################################################
#Prime factorization program written by Vincent Yang (DeltaSierra4)         #
#Use this program to find out if a given positive number is a prime number  #
#Or to carry out a prime factorization                                      #
#############################################################################

programexit = False #Set to true when user decides to exit program
validinput = False #Checks if the user made a valid input

def checkifprime(inputno): #Type an integer in and returns True if the integer is a prime number.
	if inputno == 2 or inputno == 3:
		return True
	divisor = 2
	divisorlist = [1, inputno]
	while divisor <= inputno/2 + 1:
		if inputno % divisor == 0:
			divisorlist.append(divisor)
		divisor += 1
	
	if len(divisorlist) == 2:
		return True
	else:
		return False

def primefactorization(inputno):
	inputnumber = int(inputno)
	listofprimes = primefactorrecursive(inputnumber, [])
	if len(listofprimes) == 0:
		listofprimes = [inputnumber]
	return listofprimes

def primefactorrecursive(inputno, listofcurrentprimes):
	endnum = inputno
	if inputno >= 4:
		endnum = int(math.sqrt(inputno))+1
	else:
		endnum = 3
	for number in range(endnum):
		if number == 0 or number == 1:
			continue
		elif inputno % number == 0:
			listofcurrentprimes.append(number)
			if inputno/number != 1:
				return primefactorrecursive((inputno/number), listofcurrentprimes)
			break
		elif number == endnum-1:
			listofcurrentprimes.append(inputno)
	return listofcurrentprimes
	

print("Thank you for using DS4's prime number program.")
while not programexit:
	validinput = False #Always assume user can make a faulty input. Reset this to False for each loop.
	print("Type 1 and press enter to decide if a number is a prime number.")
	print("Type 2 and press enter to do a prime factorization for any positive integer.")
	userchoice = raw_input("Type 3 and press enter to exit the program.")
	if userchoice == "1":
		print("For this function, prime numbers greater than 3 * 10^14 may take significant time.")
		while not validinput:
			inputnumberstr = raw_input("Type in a positive integer.")
			if inputnumberstr.isdigit():
				inputnumber = int(inputnumberstr)
				if int(inputnumber) >= 1:
					validinput = True
				else:
					print("You have input an invalid value.")
			else:
				print("You have input an invalid value.")
		
		inputnumber = int(inputnumberstr)
		primecheck = checkifprime(inputnumber)
		if primecheck:
			print(inputnumberstr + " is a prime number.")
		else:
			print(inputnumberstr + " is not a prime number.")
	elif userchoice == "2":
		print("For this function, prime numbers greater than 3 * 10^14 may take significant time.")
		while not validinput:
			inputnumber = raw_input("Type in a positive integer greater than 1.")
			if inputnumber.isdigit() and int(inputnumber) >= 2:
				validinput = True
			else:
				print("You have input an invalid value.")
		
		primefactorlist = primefactorization(inputnumber)
		if len(primefactorlist) == 1:
			print(inputnumber + " can be factorized into " + str(primefactorlist[0]))
		else:
			printstatement = inputnumber + " can be factorized into "
			for count in range(len(primefactorlist)):
				if count == 0:
					printstatement += str(primefactorlist[count])
				elif count == len(primefactorlist)-1:
					printstatement += " * " + str(primefactorlist[count]) + "."
				else:
					printstatement += " * " + str(primefactorlist[count])
			print(printstatement)
		
	elif userchoice == "3":
		userchoice = raw_input("Press the enter key to exit the program.")
		programexit = True
	else:
		print("You have made an invalid choice.")