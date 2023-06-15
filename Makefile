.PHONY: up down db

up:
	docker-compose up -d

down:
	docker-compose down

db:
	docker-compose exec -it db mysql -u user -ppassword
