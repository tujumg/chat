import os
def read_file(filename):
	lines = []
	with open(filename,'r',encoding='utf-8-sig ')  as f:
		                     #-sig作用為除掉ufeff
		for line in f:
			lines.append(line.strip())
			             #去掉\n
	return lines 
def convert(lines):
	new = []
	person = None #防止第一行就不是兩人名字,person未被宣告
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #跳下一個迴圈
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person+':'+line) 
	return new
def write_file(filename,lines):
	with open(filename,'w') as f: 
		for line in lines:
			f.write(line+'\n')
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt',lines)
main()