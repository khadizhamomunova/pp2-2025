class myclass:
    def __init__ (self):
        self.my_string= " "
        
    def getstring (self):
        self.my_string= input ("Enter the string : ")
    
    def printstring (self):
        print(self.my_string.upper())