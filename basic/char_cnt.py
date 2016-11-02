def char_cnt(str,ch):
	count = 0
	for letter in str:
		if letter == ch:
			count = count + 1
	return count

c=char_cnt('babana','b')
print(c)