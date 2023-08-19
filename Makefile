
BASENAME = rleague
TAG = latest
DEVIMAGE = $(BASENAME)-dev:$(TAG)
DEVCONTAINER = $(BASENAME)-prod-c
PRODIMAGE = $(BASENAME)-prod:$(TAG)
PRODCONTAINER = $(BASENAME)-prod-c

build-dev:
	docker build . -t $(DEVIMAGE) --target=dev

build-prod:
	docker build . -t $(PRODIMAGE) --target=prod

run-dev:
	docker run -it --name $(DEVCONTAINER) --rm -p 8888:8888 -v $(pwd):/app "$(DEVIMAGE)"

run-prod:
	docker run -it --name $(PRODCONTAINER) --rm -p 8888:8888 -v $(pwd):/app "$(PRODIMAGE)"