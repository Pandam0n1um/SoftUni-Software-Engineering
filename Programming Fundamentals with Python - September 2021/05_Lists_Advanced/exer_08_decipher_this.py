words_list = input().split()
new_list = []
for elem in words_list:
    ord_value = (''.join(i for i in elem if i.isdigit()))

    elem = elem[len(ord_value):]
    ord_value = int(ord_value)
    char_value = chr(ord_value)
    elem = char_value + elem
    elem=list(elem)
    elem[1],elem[-1]=elem[-1],elem[1]
    elem="".join(elem)
    new_list.append(elem)
print(" ".join(new_list))