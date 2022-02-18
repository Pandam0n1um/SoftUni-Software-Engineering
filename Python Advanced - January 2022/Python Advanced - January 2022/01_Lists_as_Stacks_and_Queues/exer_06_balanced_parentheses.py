from collections import deque
stack=[]
is_balanced=True
expression=input()
for pos in expression:
    if pos in "({[":
        stack.append(pos)
    elif pos in ')}]':
        if len(stack)<1:
            is_balanced=False
            break
        opening_paren=stack.pop() #guard against empty stack
        if f'{opening_paren}{pos}' not in ['[]','()','{}']:
            is_balanced=False
            break
if is_balanced and not stack:
    print("YES")
else:
    print("NO")










#
# from collections import deque
#
# sequence = deque(input())
# is_balanced = True
# if len(sequence) % 2 == 0:
#     while sequence:
#         first = sequence.popleft()
#         last = sequence.pop()
#         if not ((first == "{" and last == "}")
#                 or (first == "(" and last == ")")
#                 or (first == "[" and last == "]")):
#             is_balanced = False
#             break
# else:
#     is_balanced = False
# if is_balanced:
#     print("YES")
# else:
#     print("NO")
