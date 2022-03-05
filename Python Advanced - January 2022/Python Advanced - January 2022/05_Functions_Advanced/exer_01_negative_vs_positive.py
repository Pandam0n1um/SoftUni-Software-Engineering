def pos_neg(args):
    pos_sum = 0
    neg_sum = 0
    for el in args:
        if not "-" in el:
            pos_sum += int(el)
        else:
            neg_sum += int(el[1:])
    print(f"-{neg_sum}", pos_sum, sep='\n')
    if pos_sum > neg_sum:
        print('The positives are stronger than the negatives')
    elif pos_sum < neg_sum:
        print('The negatives are stronger than the positives')


values = input().split()

pos_neg(values)
