def chat_msg(msg, chat):
    chat.append(msg)
    return chat


def delete_msg(msg, chat):
    chat.remove(msg)
    return chat


def edit_msg(msg, edited_msg, chat):
    chat[chat.index(msg)] = edited_msg
    return chat


def pin_msg(msg, chat):
    pinned = chat.pop(chat.index(msg))
    chat.append(pinned)
    return chat


chat_list = []

while True:
    command = input().split()
    action = command[0]
    if action == "end":
        break
    message = command[1]
    if action == "Chat":
        chat_list = chat_msg(message, chat_list)
    elif action == "Delete":
        if message in chat_list:
            chat_list = delete_msg(message, chat_list)
    elif action == "Edit":
        if message in chat_list:
            edited = command[2]
            chat_list = edit_msg(message, edited, chat_list)
    elif action == "Pin":
        if message in chat_list:
            chat_list = pin_msg(message, chat_list)

    elif action == "Spam":
        spam = command[1::]
        chat_list += spam

for line in chat_list:
    print(f"{line}")
