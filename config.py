from datetime import timedelta


# mysql_uri = "mysql+pymysql://root:admin@127.0.0.1:3306/theblogdb"
# sqlite_uri = "sqlite:///theblog.db"
# pssql_uri = "postgresql://theblogdb_fb1w_user:Atr94UXPP1aflWvJwMckVg5twPGN0db9@dpg-cs7bgkaj1k6c73cmmctg-a.oregon-postgres.render.com/theblogdb_fb1w"

class Config:
    
    def sqlite_db_uri(dbname="mydb") -> str:
        db_name = dbname.lower()
        return f"sqlite:///{db_name}.db"
    
    APP_NAME = "Draftly"
    SQLALCHEMY_DATABASE_URI = sqlite_db_uri(APP_NAME)
    SECRET_KEY = "SuperSecretKey"
    RECAPTCHA_PUBLIC_KEY = "6LdubDMqAAAAADlYsfdKWGeMR2vHoeG6LDhI78V_"
    RECAPTCHA_PRIVATE_KEY = "6LdubDMqAAAAADy5zk9EPk7LtZ4Asv-2IzFwPruu"
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    UPLOAD_FOLDER = "uploads"
    MAX_FILE_SIZE = 12 * 1000 * 1000