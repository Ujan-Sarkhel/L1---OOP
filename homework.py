class Dog:
    breed=''
    colour=''
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
ob1=Dog("Retriever", "yellow")
print('the breed of dog1 is',ob1.breed, "and its colour is",ob1.colour)
ob2=Dog("Spaniel", "yellow")
print('the breed of dog1 is',ob1.breed, "and its colour is also",ob1.colour)