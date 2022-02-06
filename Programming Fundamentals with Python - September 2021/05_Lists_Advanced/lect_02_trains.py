def add_people(wagon_list, people_count):
    wagon_list[-1] += people_count
    return wagon_list


def insert_people(wagon_list, wagon_index, people_count):
    wagon_list[wagon_index] += people_count
    return wagon_list


def leave_people(wagon_list, wagon_index, people_count):
    wagon_list[wagon_index] -= people_count
    return wagon_list


wagons_ammount = int(input())

wagon_list_main = [0] * wagons_ammount

command = input().split()

while not command[0] == "End":
    action = command[0]

    if action == "add":
        people = int(command[1])
        wagon_list_main = add_people(wagon_list_main, people)
    elif action == "insert":
        index = int(command[1])
        people = int(command[2])
        wagon_list_main = insert_people(wagon_list_main, index, people)
    elif action == "leave":
        index = int(command[1])
        people = int(command[2])
        wagon_list_main = leave_people(wagon_list_main, index, people)
    command = input().split()

print(wagon_list_main)
