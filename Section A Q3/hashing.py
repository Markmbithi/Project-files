# One way hashing algorithm impossible to
import hashlib
m = hashlib.sha1()
m.update("The quick brown fox jumps over the lazy dog")
print(m.hexdigest())