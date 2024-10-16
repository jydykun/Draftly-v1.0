from datetime import timedelta

class Config:
    mysql_uri = "mysql+pymysql://root:admin@127.0.0.1:3306/theblogdb"
    sqlite_uri = "sqlite:///theblog.db"
    pssql_uri = "postgresql://theblogdb_fb1w_user:Atr94UXPP1aflWvJwMckVg5twPGN0db9@dpg-cs7bgkaj1k6c73cmmctg-a.oregon-postgres.render.com/theblogdb_fb1w"


    SQLALCHEMY_DATABASE_URI = mysql_uri
    SECRET_KEY = "dev"
    RECAPTCHA_PUBLIC_KEY = "6LdubDMqAAAAADlYsfdKWGeMR2vHoeG6LDhI78V_"
    RECAPTCHA_PRIVATE_KEY = "6LdubDMqAAAAADy5zk9EPk7LtZ4Asv-2IzFwPruu"
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    UPLOAD_FOLDER = "uploads"
    MAX_FILE_SIZE = 12 * 1000 * 1000
    APP_NAME = "theblog"