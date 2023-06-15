import subprocess

# ダミーのツイートをMySQLに保存するスクリプトを実行
subprocess.call(["python", "save_tweets.py"])

# BERTを使ってツイートをベクトルに変換し、その結果をMySQLに保存するスクリプトを実行
subprocess.call(["python", "convert_and_save_vectors.py"])

# ベクトル間の距離を計算し、似たツイートを検索するスクリプトを実行
subprocess.call(["python", "find_similar_tweets.py"])
