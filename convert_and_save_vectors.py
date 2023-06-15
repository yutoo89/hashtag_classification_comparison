import torch
from sqlalchemy import select
from transformers import BertModel, BertTokenizer
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import insert

# MySQLの設定
username = "user"
password = "password"
hostname = "db"
database = "tweets_db"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{hostname}/{database}")

# BERTの設定
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# ツイートをデータベースから取得
with engine.begin() as connection:
    metadata = MetaData()
    metadata.bind = engine
    tweet_table = Table('tweets', metadata, autoload_with=engine)
    s = select(tweet_table.c.id, tweet_table.c.text)
    result = connection.execute(s).fetchall()

    for row in result:
        tweet_id, text = row
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)

        vector = outputs.last_hidden_state[:, 0, :].numpy().tolist()
        # ベクトルをデータベースに保存
        vector_table = Table("tweet_vectors", metadata, autoload_with=engine)
        stmt = insert(vector_table).values(tweet_id=tweet_id, vector=vector)
        connection.execute(stmt)
