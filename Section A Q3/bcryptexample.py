# One way hashing algorithm using bcrypt
import bcrypt

password = u'foobar'
salt = bcrypt.gensalt()
password_hashed = bcrypt.hashpw(password, salt)
print password_hashed
