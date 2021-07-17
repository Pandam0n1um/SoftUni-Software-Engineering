type_animal = str(input().lower())

if type_animal == str('dog'):
    print('mammal')

elif type_animal == str('snake') or type_animal == str('tortoise') or type_animal == str('crocodile'):
    print('reptile')

else:
    print('unknown')
