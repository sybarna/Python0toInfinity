import string

class Checker:
    def __init__(self, password):
        self.password = password

    def uppercase(self):
        for x in self.password:
            if 'A' <= x <='Z':
                return True
        return False
    
    def lowercase(self):
        for x in self.password:
            if 'a' <= x <='z':
                return True
        return False
    
    def digits(self):
        for x in self.password:
            if '0' <= x <='9':
                return True
        return False
    
    def special(self):
        special_char = string.punctuation
        for x in self.password:
            if x in special_char:
                return True
        return False
    
    def strong(self):
        length = len(self.password)
        if self.uppercase() and self.lowercase() and self.digits() and self.special() and length >= 12:
            print("strong")
        elif self.uppercase() or self.lowercase() and self.digits() and 12 <= length <= 8:
            print("mid")
        else:
            print("weak")
    
    
password1 = Checker("bab")
password1.strong()

         
