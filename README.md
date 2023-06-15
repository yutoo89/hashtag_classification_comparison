# tweet_vec_search

データベースへの接続を確認する。

```
docker-compose exec -it db mysql -u user -ppassword
```

MySQLのプロンプトからシェルのプロンプトに戻る。

```
exit
```

出力結果

```
[+] Running 1/0
 ✔ Container tweet_vec_search-db-1  Running                                                                                                                                                                                                                                                                                                                                           0.0s 
Downloading (…)solve/main/vocab.txt: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 970kB/s]
Downloading (…)okenizer_config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 28.0/28.0 [00:00<00:00, 2.80kB/s]
Downloading (…)lve/main/config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 570/570 [00:00<00:00, 513kB/s]
Downloading model.safetensors: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 440M/440M [00:13<00:00, 33.6MB/s]
Some weights of the model checkpoint at bert-base-uncased were not used when initializing BertModel: ['cls.seq_relationship.weight', 'cls.predictions.transform.dense.weight', 'cls.predictions.transform.dense.bias', 'cls.seq_relationship.bias', 'cls.predictions.bias', 'cls.predictions.transform.LayerNorm.weight', 'cls.predictions.transform.LayerNorm.bias']
- This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Input text: 一緒に働く田中が冗談を言って、場の雰囲気が良くなった。
Most similar tweet: 犬の喜びそうな顔を見ると、一日の疲れが吹っ飛ぶ。
Input text: 久しぶりに砂浜に行ってリフレッシュできた。
Most similar tweet: 新しいプログラミング言語を学び始めた。チャレンジは成長につながる。
Input text: 昨日読んだ推理小説の最後に驚くべきどんでん返しがあった。
Most similar tweet: 昨日観た映画が素晴らしかった。深いメッセージが心に残った。
Input text: 不具合の修正ばかりで1日が終わったが、やりきると清々しい。
Most similar tweet: 猫の毛づくろいを見ていると癒される。彼らの日常が特別。
Input text: サンスベリアを部屋に置くと有害物質を除去してくれるらしい。
Most similar tweet: パズルゲームの新レベルをクリア。脳を活性化させる感じが好き。
```
