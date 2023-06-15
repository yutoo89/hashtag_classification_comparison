import configparser
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import insert

# 設定を読み込む
config = configparser.ConfigParser()
config.read('config.ini')

# MySQLの設定
username = config['DATABASE']['USERNAME']
password = config['DATABASE']['PASSWORD']
hostname = config['DATABASE']['HOSTNAME']
database = config['DATABASE']['DATABASE']

engine = create_engine(f"mysql+pymysql://{username}:{password}@{hostname}/{database}")

# ダミーのツイート
tweets = [
    {"id": 1, "text": "This is the first tweet."},
    {"id": 2, "text": "This is another tweet."},
    # ...
]

# ツイートをデータベースに保存
with engine.begin() as connection:
    metadata = MetaData()
    metadata.bind = engine

    tweet_table = Table('tweets', metadata, autoload_with=engine)
    for tweet in tweets:
        stmt = insert(tweet_table).values(id=tweet["id"], text=tweet["text"])
        connection.execute(stmt)
