
#################################################################################################
# نظام التحقق من تسجيل الدخول                                                                 #
# التأكد من وجود المستخدم، ثم التأكد من صحة كلمة المرور، ثم التأكد من أن حسابه ليس محظوراً #
#################################################################################################

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
    
class UserExistsHandler(Handler):
      def handle(self, request):
          users = ["admin", "ahmed", "asmaa"]
          if request["username"] not in users:
              return f"Error: User {request['username']} not found!"
          print("User exists... passing to next check.")
          return super().handle(request)
      
class PasswordCheckHandler(Handler):
    def handle(self, request):
        if request["password"] != "12345":
            return "Error: Invalid password!"
        print("Password correct... passing to next check.")
        return super().handle(request)

class AccountStatusHandler(Handler):
    def handle(self, request):
        if request["username"] == "asmaa": 
            return "Error: asmaa account is locked!"
        print("Account is active. Login successful!")
        return super().handle(request)


user_data = {"username": "asmaa", "password": "1234"}


auth_chain = UserExistsHandler()
check_pass = PasswordCheckHandler()
acc_status = AccountStatusHandler()

auth_chain.set_next(check_pass).set_next(acc_status)


result = auth_chain.handle(user_data)
if result:
    print(result)      