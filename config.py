class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@127.0.0.1:3306/theblogdb"
    SECRET_KEY = "dev"
    RECAPTCHA_PUBLIC_KEY = "6LdubDMqAAAAADlYsfdKWGeMR2vHoeG6LDhI78V_"
    RECAPTCHA_PRIVATE_KEY = "6LdubDMqAAAAADy5zk9EPk7LtZ4Asv-2IzFwPruu"
    UPLOAD_FOLDER = "uploads"
    MAX_FILE_SIZE = 12 * 1000 * 1000
    APP_NAME = "theblog"