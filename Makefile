.PHONY: start stop build healthcheck test containerclean imageclean push

test: test_tests.py
	python3 test_tests.py

healthcheck: ./healthcheck.sh
	./healthcheck.sh

build: healthcheck Dockerfile
	docker build --no-cache -t sharkzeeh/crypto:latest .

start:
	docker run --detach --rm --name crypto --volume `pwd`:/app/ sharkzeeh/crypto

stop:
	docker stop crypto

push: build
	docker push sharkzeeh/crypto

containerclean:
	docker container prune -f

imageclean:
	docker rmi -f `docker images -a | grep crypto | grep -Po '\b\w{12}\b'` || true
	docker rmi -f `docker images -a | grep none | grep -Po '\b\w{12}\b'`






