command = input()
chat_logger = []


def check_msg(message):
    if message in chat_logger:
        return True


def chat(message):
    chat_logger.append(message)


def delete_msg(message):
    if check_msg(message):
        chat_logger.remove(message)


def edit_msg(message, edited_version):
    if check_msg(message):
        chat_logger[chat_logger.index(message)] = edited_version


def pin_msg(message):
    if check_msg(message):
        chat_logger.append(chat_logger.pop(chat_logger.index(message)))


def spam_msg(messages):
    for message in messages:
        chat_logger.append(message)


while command != "end":
    command_type, *messages = command.split()
    if "Chat" in command_type:
        chat(messages[0])
    elif "Delete" in command_type:
        delete_msg(messages[0])
    elif "Edit" in command_type:
        edit_msg(messages[0], messages[1])
    elif "Pin" in command_type:
        pin_msg(messages[0])
    elif "Spam" in command_type:
        spam_msg(messages)
    command = input()

for message in chat_logger:
    print(message)











