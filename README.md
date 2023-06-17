# BERTを使ったTweetの検索

自然言語処理（NLP）技術であるBERT（Bidirectional Encoder Representations from Transformers）を用いて、テキストメッセージの類似度を計算し、データベースから最も似たテキストメッセージを検索するアプリケーションです。

このアプリケーションでは、検索性能よりも処理のシンプルさを優先しています。そのため、日本語テキストを事前学習したモデルを使用する、タスクに応じたファインチューニングを行うといった性能向上は別途行う必要があります。

## 使用技術

以下の技術を使用しています：

- Python
- BERT (Bidirectional Encoder Representations from Transformers)
- MySQL
- Docker
- Docker Compose
- Jupyter Notebook

## シーケンス図

```Mermaid
sequenceDiagram
    participant MySQL
    participant Python
    participant BERT

    Note over BERT,MySQL: 事前準備
    Python->>MySQL: テキストメッセージ100件を保存
		MySQL->>Python: テキストメッセージ100件を取得
    Python->>BERT: テキストメッセージをトークンに変換
    BERT-->>Python: トークン
    Python->>BERT: トークンをベクトル表現に変換
    BERT-->>Python: ベクトル表現
    Python->>MySQL: ベクトル表現を保存

    Note over BERT,MySQL: 検索
    Python->>BERT: 任意のテキストをトークンに変換
    BERT-->>Python: トークン
    Python->>BERT: トークンをベクトル表現に変換
    BERT-->>Python: ベクトル表現
    Python->>MySQL: 保存されているベクトル表現をすべて取得
    MySQL-->>Python: 保存されたベクトル表現
    Python->>Python: 今回テキストと保存されたテキストのコサイン類似度を計算
　　　　　　　　Python->>MySQL: 今回のテキストに最も似たテキストメッセージを取得
		MySQL->>Python: 最も似たテキストメッセージ
    Python->>Python: 最も似たテキストメッセージを表示
```

## インストール方法

このアプリケーションを実行するためには、DockerとDocker Composeが必要です。以下の公式サイトからそれぞれのインストール方法をご覧ください。

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

それらがインストールされたら、このリポジトリをクローンしてください。

```bash
git clone <repository_url>
```

そして、クローンしたディレクトリに移動します。

```bash
cd <repository_directory>
```

## 実行方法

次に、以下のコマンドを使ってDockerコンテナを起動します。

```bash
make up
```

その後、以下のコマンドで`BERTを使ったtweetの検索.ipynb`を実行します。

```bash
make j
```

ブラウザで表示されるURLをクリックして、Jupyter Notebookを開きます。その後、`BERTを使ったtweetの検索.ipynb`を開いて各セルを順に実行します。

## Dockerコンテナの停止方法

以下のコマンドを実行してDockerコンテナを停止します。

```bash
make down
```
