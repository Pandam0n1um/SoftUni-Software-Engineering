lines = int(input())

stack = []

for i in range(lines):
    command, *tokens = input().split()
    if command == "1":
        stack.append(int(tokens[0]))
    elif command == "2" and stack:
        stack.pop()
    elif command == "3" and stack:
        print(max(stack))
    elif command == "4" and stack:
        print(min(stack))
reversed_num = []

for i in range(len(stack)):
    reversed_num.append(str(stack.pop()))
print(", ".join(reversed_num))
