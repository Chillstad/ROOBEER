#default memory slots
#can be expanded
memory = {
	"FANTER":0,
	"SPIRTE":0,
	"PEPSIE":0,
	"MONSERT":0,
	"DRPEBBA":0
}

#turn a roo beer binary representation into an integer
def toInt(inputString):
	tokens = inputString.split(" ")
	step = 0
	total = 0
	negative = 1
	for i in tokens[::-1]:
		if i == "NO":
			negative = -1
		elif i == "BEER":
			step += 1
		elif i == "ROO":
			total += pow(2, step)
			step += 1
	return total * negative

#turn an integer into a roo beer binary representation
def toRoobeer(inputInt):
	output = ""
	inputInt = str(format(inputInt, "b"))
	
	for i in inputInt:
		if i == "-":
			output += "NO"
		elif i == "0":
			output += "BEER"
		elif i == "1":
			output += "ROO"
		output += " "

	return output

#find all binary numbers in the code, and convert them to usable integers
def cleanNumbers(codeList):
	for command in codeList:
		command.append("STOP")
		foundNumber = ""
		start = 0
		tokenFound = False
		
		while not tokenFound:
			for token in range(start, len(command)):
					if command[token] in ["NO", "ROO", "BEER"]:
						if not tokenFound:
							start = token
							tokenFound = True
						foundNumber += command[token] + " "
					else:
						if tokenFound:
							tokenFound = False
							for iteration in range(token - start):
								command.pop(start)
							command.insert(start, toInt(foundNumber))
							foundNumber = ""
						if token == len(command)-1:
							break
	

			break
		command.pop(len(command)-1)
	return codeList

#take a statement and evalute it, performing operations and comparisions
def eval(statement):
	sequence = []
	for i in statement:
		if i in memory:
			sequence.append(memory[i])
		else:
			sequence.append(i)

	value = sequence[0]
	i = 0
	
	while i < len(sequence)-1:
		
		if sequence[i] in ["BUY", "DRINK", "SHARE", "MORE", "IS", "BIG", "SMAL", "NOT", "LEFTOVER"]:
			
			if sequence[i] == "BUY":
				value += sequence[i+1]
				i += 1
				
			if sequence[i] == "DRINK":
				value -= sequence[i+1]
				i += 1
				
			if sequence[i] == "SHARE":
				value /= sequence[i+1]
				value = round(value)
				i += 1

			if sequence[i] == "LEFTOVER":
				value = value % sequence[i+1]
				i += 1

			if sequence[i] == "MORE":
				value *= sequence[i+1]
				i += 1
				
			if sequence[i] == "IS":
				if sequence[i+1] != "NOT":
					if value == sequence[i+1]:
						value = 1
					else:
						value = 0
				else:
					if value != sequence[i+2]:
						value = 1
					else:
						value = 0
						
			if sequence[i] == "SMAL":
				if value < sequence[i+1]:
					value = 1
				else:
					value = 0

			if sequence[i] == "BIG":
				if value > sequence[i+1]:
					value = 1
				else:
					value = 0			

		i += 1
	
	return value
			
#target is the file to run
#split the text file into tokens, seperated by into strings of commands
#iterate through each command string
def run(target):
	file = open(target, "r")
	code = file.read()
	tokenCodeLines = code.split("\n")
	tokenCode = []
	for i in tokenCodeLines:
		tokenCode.append(i.split(" "))

	tokenCode = cleanNumbers(tokenCode)
	
	


	i = 0
	while i < len(tokenCode):
		command = tokenCode[i]

		if command[0] == "COKEY":
			end = command.index("COLA")
			
			value = eval(command[1:end])
			if value == 1:
				temp = command[end+1:]
				command = temp
			else:
				i += 1
				continue
			
		if command[0] == "NEW":
			memory[command[1]] = 0
		
		if command[0] in memory:
			if command[1] == "ROOBEER":
				memory[command[0]] = eval(command[2:])
		elif command[0] == "GO":
			i += eval(command[1:]) - 1
		elif command[0] == "BACK":
			i -= eval(command[1:]) + 1
		elif command[0] == "MUG":
			try:
				if command[1] in memory or command[2] in ["BUY", "DRINK", "SHARE", "MORE", "IS", "ROO", "BEER", "SMAL", "BIG", "LEFTOVER"]:
					print(eval(command[1:]))
				else:
					output = ""
				
					for j in command[1:]:
						output += str(j) + " "
					print(output)
			except:
				output = ""
				
				for j in command[1:]:
					output += str(j) + " "
				print(output)
		elif command[0] == "SPILL":
			i = len(tokenCode)
		

		
			
		i += 1
		
run(input("I LOVE ROOBEER\nROOBEER FILE TO RUN: ") + ".roobeer")
	
	
