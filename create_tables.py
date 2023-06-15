import pymysql

# MySQLデータベースへの接続情報を設定
host = "db"  # Docker Composeで定義したMySQLサービスのサービス名
port = 3306  # MySQLのデフォルトのポート番号
user = "user"  # MySQLのユーザ名
password = "password"  # MySQLのパスワード
database = "tweets_db"  # MySQLのデータベース名

# MySQLデータベースに接続
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# カーソルオブジェクトを作成
cursor = connection.cursor()

# tweetsテーブルを作成するSQL文
create_table_query = """
CREATE TABLE IF NOT EXISTS tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# SQL文を実行
cursor.execute(create_table_query)

# 変更をコミット（確定）
connection.commit()

# MySQLデータベースとの接続を閉じる
connection.close()
