#!/bin/sh

set -e

docker-compose build
docker-compose down
docker-compose up -d

docker exec -i statistics_app sh -c "python manage.py generate_statistics 10000"