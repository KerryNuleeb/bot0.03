import random


def get(id_chat, vk):
    while True:
        users = vk.messages.getChat(chat_id=id_chat, fields='nickname')["users"]
        gay = users[random.randrange(0, len(users))]
        gayName = gay["first_name"] + " " + gay["last_name"]
        if (gayName.find("Бот") == -1):
            return gayName
