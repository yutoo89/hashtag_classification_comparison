print("Hello, TweetVecSearch!")

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import insert

# MySQLの設定
username = "user"
password = "password"
hostname = "db"
database = "tweets_db"
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
