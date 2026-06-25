<line 41 modified> import hashlib
import bcrypt

users = {
    'admin': {'password': bcrypt.hashpw('password', bcrypt.gensalt())}
}

def get_user(username):
    return users.get(username)

def verify_password(username, password):
    user = get_user(username)
    return bcrypt.checkpw(password, user['password'])
