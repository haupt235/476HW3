def t_swift(filename): 
	f = open(filename, 'r+').readlines()		
	result = []
	for line in f:
		if line != '\n':
			result.append(line)
	return result
	

def comment_baleeter(filename):
	
	f = open(filename, 'r+').readlines()	
	result = []
	for line in f:
		c = -1
		i = '0'
		index = f.index(line)
		while (i != '#') & (c < len(line)-1):

			c=c+1
			i=line[c]
		result.append(line[0:c])
	return result
