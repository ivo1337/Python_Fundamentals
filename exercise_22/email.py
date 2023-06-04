class Email:
    email_information = []

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


data_input = input()

while data_input != "Stop":
    sender, receiver, *content = data_input.split()
    Email.email_information.append(Email(sender, receiver, ''.join(content)))
    data_input = input()

send_mails = [int(x) for x in input().split(", ")]

for pos, email in enumerate(Email.email_information):
    if pos in send_mails:
        email.send()
    print(email.get_info())

