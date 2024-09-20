def vowel_count(str):
	
	count = 0
	vowel = set("aeiouAEIOU")
	
	for alphabet in str:
		if alphabet in vowel:
			count = count + 1
	print("Number of vowels :", count)
	
str = "Aishwarya"
vowel_count(str)
