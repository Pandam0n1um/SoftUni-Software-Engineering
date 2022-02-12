import re

key_val = input().split()
treasure_dict = {}
while True:
    command = input()
    if command == "find":
        break
    decoded = ""
    for ind, val in enumerate(command):
        reductor = int(key_val[ind % len(key_val)])
        decoded += chr(ord(val) - reductor)
    decoded = decoded.split("&")
    tr_type = decoded[1]
    pattern = "<(.*?)>"
    coordinates = re.search(pattern, decoded[2]).group(1)
    print(f"Found {tr_type} at {coordinates}")

#     treasure_dict[decoded[1]]=coordinates
#
# for k,v in treasure_dict.items():
#     print(f"Found {k} at {v}")

# s = "abc123AUG|GAC|UGAasdfg789"
# pattern = "AUG\|(.*?)\|UGA"
#
# substring = re.search(pattern, s).group()
# print(substring)
