import configparser
import pandas as pd
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
df_tweet = pd.read_csv("tweets.csv")

# ツイートをデータベースに保存
with engine.begin() as connection:
    metadata = MetaData()
    metadata.bind = engine

    tweet_table = Table('tweets', metadata, autoload_with=engine)
    for tweet in df_tweet['text']:
        stmt = insert(tweet_table).values(text=tweet)
        connection.execute(stmt)
