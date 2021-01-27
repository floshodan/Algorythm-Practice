word = input()
max_len = 10


if (len(word) >= max_len):
	new_word = word[0]+str(len(word)-2)+word[-1]
	print(new_word)
else:
	print(word)



