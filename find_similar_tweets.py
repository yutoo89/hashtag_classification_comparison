from sqlalchemy import select
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertModel, BertTokenizer
from sqlalchemy import create_engine, Table, MetaData

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

# テキストを入力
input_text = "This is some input text."

# 入力テキストをベクトルに変換
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model(**inputs)
input_vector = outputs.last_hidden_state[:, 0, :].detach().numpy().tolist()

# データベースからベクトルを取得
with engine.begin() as connection:
    metadata = MetaData()
    metadata.bind = engine
    vector_table = Table("tweet_vectors", metadata, autoload_with=engine)
    s = select(vector_table.c.tweet_id, vector_table.c.vector)
    result = connection.execute(s).fetchall()

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
with engine.begin() as connection:
    metadata = MetaData()
    metadata.bind = engine
    tweet_table = Table("tweets", metadata, autoload_with=engine)
    s = select(tweet_table.c.text).where(tweet_table.c.id == most_similar_tweet)
    most_similar_tweet_text = connection.execute(s).scalar_one()

# 最も類似度が高いツイートと入力に使ったテキストを表示
print(f"Input text: {input_text}")
print(f"Most similar tweet: {most_similar_tweet_text}")
