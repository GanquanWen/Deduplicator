import hashlib

#given a file name, hash it!
def file_hash(filename):
  h = hashlib.sha256()
  with open(filename, 'rb', buffering=0) as f:
    for b in iter(lambda : f.read(128*1024), b''):
      h.update(b)
    result=h.hexdigest()
  return result
a = file_hash('test.txt')
print(a)

