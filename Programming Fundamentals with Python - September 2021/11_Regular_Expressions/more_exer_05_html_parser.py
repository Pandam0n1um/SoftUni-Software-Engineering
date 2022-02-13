import re

text = input()

title = re.search(r'(?<=<title>)(.+?)(?=</title>)', text)[0]
raw_content = re.search(r'(?<=<body>)(.*)(?=</body>)', text)[0]
no_tags_content =re.sub(r'<.*?>',"", raw_content)
filtered_content = no_tags_content.replace(r'\n', ' ')

print(f"""Title: {title}
Content: {filtered_content}""")