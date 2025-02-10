build:
	docker build -t nickosipov/flask-service:latest -f Dockerfile.prod .

push:
	docker push nickosipov/flask-service:latest

run:
	docker run -d -p 5000:5000 --name flask-service nickosipov/flask-service:latest