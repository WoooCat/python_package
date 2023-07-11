# Building and starting docker-compose containers
run:
	@docker-compose up -d

# Stopping and destroying docker-compose containers
stop:
	@docker-compose down -v

# Removing all stopped Docker images
clear:
	@@docker images -q | xargs -r docker rmi -f

# Get Docker Images status
status:
	@docker ps -a