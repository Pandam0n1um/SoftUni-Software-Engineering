title = input()
content = input()
result = "<h1>\n    " + title + "\n</h1>\n" + "<article>\n    " + content + "\n</article>\n"
while True:
    comment = input()
    if comment == "end of comments":
        break
    result += "<div>\n    " + comment + "\n</div>\n"

print(result)
