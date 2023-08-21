
BASENAME = rleague
TAG = latest
DEVIMAGE = $(BASENAME)-dev:$(TAG)
DEVCONTAINER = $(BASENAME)-prod-c
PRODIMAGE = $(BASENAME)-prod:$(TAG)
PRODCONTAINER = $(BASENAME)-prod-c

dev-build:
	docker build . -t $(DEVIMAGE) --target=dev

prod-build:
	docker build . -t $(PRODIMAGE) --target=prod

dev-run:
	docker run -it --name $(DEVCONTAINER) --rm -v $(PWD):/app "$(DEVIMAGE)" /bin/bash

dev-test:
	docker run --name $(DEVCONTAINER) --rm "$(DEVIMAGE)" pipenv run pytest

prod-run:
	docker run -it --name $(PRODCONTAINER) --rm -p 8888:8888 -v $(pwd):/app "$(PRODIMAGE)"