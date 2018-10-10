'''
Problem : https://leetcode.com/problems/longest-valid-parentheses/description/
Description : Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

class LongestValidParenthesis(object):
	def __init__(self, input):
		self.input = input
	def processLongestValidParenthesis(self):
		difference = 0
		result = 0
		beginValidIndex = -1 #the begin index excludes in the valid substring
		endValidIndex = beginValidIndex   #the end index includes in the valid substring
		zeroDifferenceIdx = beginValidIndex
		for idx, letter in list(enumerate(list(self.input))):
			if letter == '(':
				difference += 1 
			else : 
				difference -= 1
			if difference < 0 :
				if result < endValidIndex - beginValidIndex :
					result = endValidIndex - beginValidIndex
				difference = 0
				beginValidIndex = endValidIndex = idx
			elif difference > 0 :
				endValidIndex = idx
			else :
				endValidIndex = idx
				zeroDifferenceIdx = idx

		 
		if difference > 0 and endValidIndex - beginValidIndex - difference > result :
			result = endValidIndex - max(beginValidIndex, zeroDifferenceIdx) - difference
		return result





if __name__ == '__main__':
	print("Test 1 longest valid length : {0}".format(LongestValidParenthesis("(").processLongestValidParenthesis()))
	print("Test 2 longest valid length : {0}".format(LongestValidParenthesis(")").processLongestValidParenthesis()))
	print("Test 3 longest valid length : {0}".format(LongestValidParenthesis("(()").processLongestValidParenthesis()))
	print("Test 4 longest valid length : {0}".format(LongestValidParenthesis(")()())").processLongestValidParenthesis()))
	print("Test 5 longest valid length : {0}".format(LongestValidParenthesis("(((((((((()()()))()()))()()))()()))()()))()()))()())((())))))))))))))))()()))()()))()()))()()))()()))()())))))))))))()()))()()))()()))()())))))))))))))))(((((((((()))))))))))(((((())").processLongestValidParenthesis()))
	print("Test 5 longest valid length : {0}".format(LongestValidParenthesis("()(()").processLongestValidParenthesis()))
