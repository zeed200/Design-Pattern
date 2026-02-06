class ChatMediator:
    """الوسيط (برج المراقبة)"""
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    """الكائن الذي يتواصل عبر الوسيط"""
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        print(f"--- {self.name} sends: {message} ---")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} received: {message}")


chat = ChatMediator()

ali = User("Ali", chat)
sara = User("Sara", chat)
omar = User("Omar", chat)

chat.add_user(ali)
chat.add_user(sara)
chat.add_user(omar)

ali.send("Hello everyone!")