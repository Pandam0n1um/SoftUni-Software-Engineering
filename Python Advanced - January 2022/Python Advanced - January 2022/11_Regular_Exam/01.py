from collections import deque


def remove_letter_if_present(letter):
	for word in discovered_words:
		while True:
			if letter in discovered_words[word]:
				discovered_words[word].remove(letter)
			else:
				break
			if len(discovered_words[word]) == 0:
				return word
	return None


SEARCHED_WORDS = (
	'rose',
	'tulip',
	'lotus',
	'daffodil'
)

discovered_words = {x: list(x) for x in SEARCHED_WORDS}
is_found = False
result = None

vowels = deque(input().split())
consonants = input().split()

while True:
	if not (vowels and consonants):
		break

	if vowels:
		curr_vowel = vowels.popleft()
		result = remove_letter_if_present(curr_vowel)
		if result:
			is_found = True


	if consonants:
		curr_consonant = consonants.pop()
		result = result if result else remove_letter_if_present(curr_consonant)
		if result:
			is_found = True
	if is_found:
		break

if is_found:
	print(f"Word found: {result}")
else:
	print("Cannot find any word!")
if vowels:
	print(f"Vowels left: {' '.join(vowels)}")
if consonants:
	print(f"Consonants left: {' '.join(consonants)}")
# o e a o e a i
# p r s x r


# a a a
# x r l t p p
# u a o i u y o e
# p m t l


a={SEARCHED_WORD: SEARCHED_WORD for SEARCHED_WORD in SEARCHED_WORDS}