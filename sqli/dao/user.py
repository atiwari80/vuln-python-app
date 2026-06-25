<line 41 removed> import hashlib
import bcrypt

def get_user_password(username):
    user = get_user(username)
    return bcrypt.hashpw(user['password'], bcrypt.gensalt())

def verify_password(username, password):
    user_password = get_user_password(username)
    return bcrypt.checkpw(password, user_password)
