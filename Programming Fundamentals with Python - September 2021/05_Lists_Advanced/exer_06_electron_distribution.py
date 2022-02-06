number_electrons = int(input())

electrons = []
current_shell = 1
while number_electrons > 0:
    max_el_shell = 2 * current_shell ** 2
    if max_el_shell > number_electrons:
        electrons.append(number_electrons)
        break
    else:
        electrons.append(max_el_shell)
    number_electrons -= max_el_shell
    current_shell += 1
print(electrons)