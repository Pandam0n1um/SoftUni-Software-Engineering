oscar_number = int(input())
is_88=False
is_86=False
if oscar_number == 88:
    is_88=True
    print("Leo finally won the Oscar! Leo is happy")
elif oscar_number == 86:
    is_86=True
    print("Not even for Wolf of Wall Street?!")
elif 88 < oscar_number:
    print("Leo got one already!")
else :
    print("When will you give Leo an Oscar?")