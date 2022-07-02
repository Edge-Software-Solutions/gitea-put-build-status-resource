docker=docker
tag = objectivetruth/gitea-put-build-status-resource

.PHONY: test

build:
	$(docker) build --target prod_build -t $(tag) .

test:
	@echo "Testing..."
	$(docker) build --target test_build -t $(tag):test .
