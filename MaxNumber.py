''' 
Given an arbitary number in maths with at least 3 digits, remove 2 digits among it and guarantee the rest is the greatest number
'''
from types import *
from functools import *

NUMBER_OF_DIGITS = 2

def main():
	result = processNumber(5827403)
	print("Result is {0}".format(result))

def validateInput(inputNumber):
	if isinstance(inputNumber, int) and inputNumber >= 100:
		return True
	else:
		return False

def convertNumberToArr(inputNumber):
	return list(map(int, list(str(inputNumber))))
	
def processNumber(inputNumber):
	if validateInput(inputNumber):
		return parseArrToMaxNumber(convertNumberToArr(inputNumber))
	else:
		print("This isn't a valid number")
'''
This function parse an array with digit in order and tries to remove NUMBER_OF_DIGITS digits defined by the user
in order to find the greatest number constructing by the remain digits in order
'''
def parseArrToMaxNumber(arr):
	arrLength = len(arr)
	targetArr = []
	remainsDigitsToProcess = NUMBER_OF_DIGITS
	i = 0
	while i < (arrLength - remainsDigitsToProcess):
		if remainsDigitsToProcess > 0:
			maxNumIndex = i
			for j in range(1, remainsDigitsToProcess + 1):
				if arr[i + j] > arr[maxNumIndex]:
					maxNumIndex = i + j
			remainsDigitsToProcess = remainsDigitsToProcess - maxNumIndex + i
			targetArr.append(arr[maxNumIndex])
			i = maxNumIndex + 1
		else:
			targetArr += arr[i:arrLength]
			break
	return int(reduce(lambda x, y : x + str(y), targetArr, ''))



if __name__ == "__main__":
	main()