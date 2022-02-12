start=ord(input())
end=ord(input())
word=input()
sum=0

for symbol in word:
    curr_val=ord(symbol)
    if start<curr_val<end:
        sum+=curr_val
print(sum)