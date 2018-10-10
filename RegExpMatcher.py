'''
 Problem : Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
 
	Note:

		s could be empty and contains only lowercase letters a-z.
		p could be empty and contains only lowercase letters a-z, and characters like . or *.

 Link : https://leetcode.com/problems/regular-expression-matching/description/
'''

class RegExpMatcher(object):
	def match(self, src, reg):
		srcL = list(src)
		regL = list(reg)
		srcN = len(srcL)
		regN = len(regL)
		if srcN == 0:
			return regN == 0 or (regN == 2 and regL[1] == '*')
		elif regN == 0:
			return False
			
		idx = 0
		regIdx = 0
		while idx < srcN:
			if regL[regIdx] == '.': # if the current regex letter is "."
				if regIdx == regN - 1: # if the current regex index is the last one letter
					# if the current letter in the string is the last index, then the parse is OK; otherwise, KO.
					if idx == srcN - 1:  
						return True	
					else :
						return False
				elif regL[regIdx + 1] == '*': # if there is ".*" together, which may valid all the strings 
					# if this is the last letter in the regx, then it can valid all the strings
					if regIdx + 1 == regN - 1: 
						return True
					else:
						firstWordFoundIdx = -1
						for subRegIdx in range(regIdx + 2, regN):
							if regL[subRegIdx] != '.' and regL[subRegIdx] != '*':
								firstWordFoundIdx = subRegIdx 
								break
						if firstWordFoundIdx == -1:
							return True
						elif idx == srcN - 1:
							return False
						else:
							matchWordIdx = srcL[idx:].index(regL[firstWordFoundIdx])
							if matchWordIdx == -1:
								return False
							elif matchWordIdx + idx == srcN - 1 or self.match(''.join(srcL[matchWordIdx + 1:]), ''.join(regL[firstWordFoundIdx + 1:])):
								return True
							else:
								temRegL = regL[firstWordFoundIdx + 1:]
								temRegL.insert(0, '*')
								temRegL.insert(0, '.')
								return self.match(srcL[matchWordIdx + 1:], temRegL)
				else : # if there is a letter a-z after ".", then continue
					regIdx += 1
			else : # this is a letter
				if regIdx == regN - 1:
					return regL[regIdx] == srcL[idx] and idx == srcN - 1
				elif regL[regIdx + 1] == '.' or regL[regIdx + 1] != '*':
					if regL[regIdx] == srcL[idx]:
						regIdx += 1
					else :
						return False
				else : # A "*" follows a word
					if self.match(''.join(srcL[idx:]), ''.join(regL[regIdx + 2:])):
						return True
					elif regL[regIdx] != srcL[idx]:
						return False
					else:
						return self.match(''.join(srcL[idx + 1:]), ''.join(regL[regIdx:]))

			idx += 1 # move one position to the right by default  
	def process(self, src, reg):
		print("{0} matches {1} : {2}".format(src, reg, self.match(src, reg)))



if __name__ == "__main__" :
	RegExpMatcher().process('absxassaa', '.*s.a')
	RegExpMatcher().process('aa', 'a')
	RegExpMatcher().process('ab', '.*')
	RegExpMatcher().process('aab', 'c*a*b')
	RegExpMatcher().process('mississppi', 'mis*is*p*.')
	RegExpMatcher().process('aaa', 'a*a')
	RegExpMatcher().match('absxassaa', '.*s.a')


