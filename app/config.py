import os

SECRET_KEY = 'uzbkr123'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://std_1630_exan:uzbkr123@std-mysql.ist.mospolytech.ru/std_1630_exan'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')

ADMIN_ROLE_ID = 1
MODERATOR_ROLE_ID = 2
USER_ROLE_ID = 3