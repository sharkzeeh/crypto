.PHONY: start stop build healthcheck test clean push

test: test_tests.py
	python3 test_tests.py

healthcheck: ./healthcheck.sh
	./healthcheck.sh

build: healthcheck Dockerfile
	docker build --no-cache -t sharkzeeh/crypto:latest .

start:
	docker run --detach --rm --name crypto --volume `pwd`:/app/ sharkzeeh/crypto

stop: healthcheck
	docker stop crypto

push: build
	docker push sharkzeeh/crypto

clean:
	docker container prune -f






