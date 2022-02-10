dict_contacts = {}
n_searched = ""
while True:
    new_line = input()
    if "-" not in new_line:
        n_searched = int(new_line)
        break
    contact, phone_num = new_line.split("-")

    # if contact not in dict_contacts:
    dict_contacts[contact] = phone_num

for i in range(n_searched):
    cont_name=input()
    if cont_name in dict_contacts:
        print(f"{cont_name} -> {dict_contacts[cont_name]}")
    else:
        print(f"Contact {cont_name} does not exist.")
