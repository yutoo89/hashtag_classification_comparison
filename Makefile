.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: run
run:
	docker-compose run app python main.py

.PHONY: j
j:
	jupyter notebook --ip 0.0.0.0 --allow-root

.PHONY: tweets
tweets:
	docker-compose run app python create_tweets_table.py

.PHONY: tweet_vectors
tweet_vectors:
	docker-compose run app python create_tweet_vectors_table.py

.PHONY: db
db:
	docker-compose exec -it db mysql -u user -ppassword
