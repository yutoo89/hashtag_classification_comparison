.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: j
j:
	docker-compose exec app jupyter notebook --allow-root --ip=0.0.0.0
