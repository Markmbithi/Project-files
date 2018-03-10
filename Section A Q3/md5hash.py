# Two way hashing algorithm using md5
import hashlib
m = hashlib.md5()
m.update("mynae")
print m.hexdigest()