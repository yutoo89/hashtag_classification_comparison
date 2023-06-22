# ハッシュタグのカテゴリ分類

自然言語処理（NLP）技術、特にBERT、OpenAIのEmbedding API、ELECTRAを用いて、ハッシュタグのカテゴリ分類を行うアプリケーションです。

このアプリケーションでは、それぞれのモデルを用いてハッシュタグをベクトルに変換し、それを基にハッシュタグのカテゴリを予測します。そして、それぞれの予測結果を評価することで、各モデルの性能を比較します。

## 使用技術

以下の技術を使用しています：

- Python
- pandas
- numpy
- torch
- scikit-learn
- seaborn
- matplotlib
- transformers (BERT, ELECTRA)
- OpenAI Embedding API

## 処理の概要

1. ハッシュタグとそのカテゴリの情報が含まれたCSVファイルを読み込みます。
2. BERT, OpenAIのEmbedding API, ELECTRAを用いて、ハッシュタグとカテゴリをそれぞれベクトルに変換します。
3. 各ハッシュタグのベクトルと全カテゴリのベクトルのコサイン類似度を計算し、最も類似度が高いカテゴリを予測カテゴリとします。
4. 実際のカテゴリと予測カテゴリを比較し、各モデルの性能を評価します。

## インストール方法

このアプリケーションを実行するためには、Pythonとその必要なパッケージが必要です。Pythonのインストールは公式ウェブサイトを参照してください。Pythonがインストールされたら、このリポジトリをクローンしてください。

```bash
git clone https://github.com/yutoo89/hashtag_classification_comparison.git
```

クローンしたディレクトリに移動します。

```bash
cd hashtag_classification_comparison
```

## 実行方法

.env_sampleをコピーして.envを作成してください。

```
cp .env_sample .env
```

`your_openai_api_key_here`は適宜、自身の情報に書き換えてください。

次に、以下のコマンドを使ってDockerコンテナを起動します。

```bash
make up
```

ブラウザで表示されるURLをクリックして、Jupyter Notebookを開きます。その後、`ハッシュタグのカテゴリ分類の性能比較.ipynb`を開いて各セルを順に実行します。

## Dockerコンテナの停止方法

以下のコマンドを実行してDockerコンテナを停止します。

```bash
make down
```
