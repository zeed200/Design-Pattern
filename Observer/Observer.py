class Subject:
    def __init__(self):
        self._observers = []

    def ataach(self, observer):
        self._observers.append(observer)    

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class SMSNotification:
    def update(self, message):
        print(f"sending SMS :{message}")

class EmailNotification:
    def update(self, message):
        print(f"sending Email :{message}")        

store = Subject()

sms_user = SMSNotification()
email_user = EmailNotification()

store.ataach(sms_user)
store.ataach(email_user)

store.notify("new message")
