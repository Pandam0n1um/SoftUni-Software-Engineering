class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    email_data = input()
    if email_data == "Stop":
        break
    s, r, c = email_data.split()
    current_email = Email(s, r, c)
    emails.append(current_email)
ind_sent_mails = [int(index) for index in input().split(", ")]

for index_sent in ind_sent_mails:
    email = emails[index_sent]
    email.send()

for email in emails:
    print(email.get_info())
