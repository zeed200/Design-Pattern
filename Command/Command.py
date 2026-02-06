from abc import ABC, abstractmethod

# Interface
class Command(ABC): 
    @abstractmethod
    def excute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("ON")

    def turn_off(self):
        print("OFF")    

# Concrate Command
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def excute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()        

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def excute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command: Command):
        command.excute()
        self.history.append(command)

    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()        




lamp = Light()
on_command = LightOnCommand(lamp)
off_command = LightOffCommand(lamp)
remote = RemoteControl()

remote.press_button(on_command)
remote.press_undo()