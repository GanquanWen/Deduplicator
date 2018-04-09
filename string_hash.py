import hashlib

#given a string, hash it!
def string_hash(string):
    h=hashlib.sha256()
    h.update(string)
    result=h.hexdigest()
    return result

stri='hello'
strin=stri.encode('utf-8')
string_hash(strin)
