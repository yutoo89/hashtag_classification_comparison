import configparser
import pandas as pd
from sqlalchemy import select
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertModel, BertTokenizer
from sqlalchemy import create_engine, Table, MetaData

# 設定を読み込む
config = configparser.ConfigParser()
config.read('config.ini')

# MySQLの設定
username = config['DATABASE']['USERNAME']
password = config['DATABASE']['PASSWORD']
hostname = config['DATABASE']['HOSTNAME']
database = config['DATABASE']['DATABASE']

engine = create_engine(f"mysql+pymysql://{username}:{password}@{hostname}/{database}")

# BERTの設定
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# データベースからベクトルを取得
metadata = MetaData()
metadata.bind = engine
vector_table = Table("tweet_vectors", metadata, autoload_with=engine)
s = select(vector_table.c.tweet_id, vector_table.c.vector)
with engine.begin() as connection:
    result = connection.execute(s).fetchall()

# 'verification_tweets.csv'を読み込む
df = pd.read_csv('verification_tweets.csv')

# DataFrameのtext列を1件ずつ取り出す
for input_text in df['text']:
    # 入力テキストをベクトルに変換
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model(**inputs)
    input_vector = outputs.last_hidden_state[:, 0, :].detach().numpy().tolist()

    max_similarity = 0
    most_similar_tweet = None

    # 各ベクトルと入力テキストのベクトルとの間で類似度を計算
    for row in result:
        tweet_id, vector = row
        similarity = cosine_similarity(input_vector, vector)

        # 最も類似度が高いツイートを見つける
        if similarity[0][0] > max_similarity:
            max_similarity = similarity[0][0]
            most_similar_tweet = tweet_id

    # 最も類似度が高いツイートの本文を取得
    tweet_table = Table("tweets", metadata, autoload_with=engine)
    s = select(tweet_table.c.text).where(tweet_table.c.id == most_similar_tweet)
    with engine.begin() as connection:
        most_similar_tweet_text = connection.execute(s).scalar_one()

    # 最も類似度が高いツイートと入力に使ったテキストを表示
    print(f"Input text: {input_text}")
    print(f"Most similar tweet: {most_similar_tweet_text}")
