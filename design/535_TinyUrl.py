import string
import random

alphabet = string.ascii_letters+'0123456789'

class Codend(object):
    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}


    def encode(self,longurl):
        if longurl not in self.url_to_code:
            code = "".join(random.choice(alphabet) for i in range(6))
            if code not in self.code_to_url:
                self.code_to_url[code]=longurl
                self.url_to_code[longurl]=code
        return "http://tinyurl.com/"+code

    def decode(self,shorturl):
        print(self.code_to_url)
        return self.code_to_url[shorturl[-6:]]

obj = Codend()
print(obj.encode("hi"))
print(obj.decode(obj.encode("hello")))