.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: run
run:
	docker-compose run app python main.py

.PHONY: table
table:
	docker-compose run app python create_tables.py

.PHONY: db
db:
	docker-compose exec -it db mysql -u user -ppassword
