SECRET_KEY = 'THISISTOPSECRET'
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
CSRF_ENABLED = True
USER_ENABLE_EMAIL = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# mail configurations
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USERNAME = 'guptaparas039@gmail.com'
MAIL_PASSWORD = 'jyqcdtsdkwhhxueu'
MAIL_DEFAULT_SENDER = 'guptaparas039@gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True

# flask user settings
USER_APP_NAME = 'pySimplified'
USER_CONFIRM_EMAIL_LOGIN = '10*60'  # 10 minutes
USER_LOGOUT_URL = '/auth/logout'
