# Building and starting docker-compose containers
run:
	@docker-compose up -d


# Stopping and destroying docker-compose containers
stop:
	@docker-compose down -v
