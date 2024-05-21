import hashlib
import getpass

up_dic = {}

def logonget(prompt):
    user = input('Please, create your user:\n')
    hash_user = hashlib.sha256(user.encode()).hexdigest()
    password = getpass.getpass('Please, create your password:\n')
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return up_dic.update({hash_user:hash_password})

register = logonget(0)
logon = input('Please, input your user: \n')
hash_logon = hashlib.sha256(logon.encode()).hexdigest()
password = getpass.getpass('Please, input your password \n')
hash_password = hashlib.sha256(password.encode()).hexdigest()

if up_dic.get(hash_logon) == hash_password:
    print(f'Welcome!')
else:
    print(f'I don\'t know you.')