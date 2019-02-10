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
	person = None #防止第一行就不是兩人名字,person未被宣告
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count +=len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count +=len(m) 
	print('allen說了',allen_word_count,'傳了',allen_sticker_count,'個貼圖','傳了',allen_image_count,'個圖片')
	print('viki說了',viki_sticker_count,'傳了',viki_sticker_count,'個貼圖','傳了',viki_image_count,'個圖片')


def write_file(filename,lines):
	with open(filename,'w') as f: 
		for line in lines:
			f.write(line+'\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	#write_file('-LINE-Viki.txt',lines)


main()