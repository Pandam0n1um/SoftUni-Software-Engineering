lines=int(input())
sum_ascii=0
for n in range(lines):
    char_input=input()
    sum_ascii+=ord(char_input)

print(f"The sum equals: {sum_ascii}")