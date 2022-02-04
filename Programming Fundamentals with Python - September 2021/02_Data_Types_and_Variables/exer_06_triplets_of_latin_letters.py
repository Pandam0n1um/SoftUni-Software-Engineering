n_value=int(input())


for i in range (97,97+n_value):
    for j in range(97, 97 + n_value):
        for k in range(97, 97 + n_value):
            print(f"{chr(i)}{chr(j)}{chr(k)}")