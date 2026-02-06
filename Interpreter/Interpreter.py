from abc import ABC, abstractmethod

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# Terminal Expression
class Number(Expression):
    def __init__(self, value):
        self.value = value    

    def interpret(self):
        return self.value    
    
# Non-Terminal Expression
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right    

    def interpret(self):
        return self.left.interpret() + self.right.interpret()   

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right    

    def interpret(self):
        return self.left.interpret() - self.right.interpret()         