user=bar
name=foo


docker=docker
tag = $(user)/$(name)
dockerfile = Dockerfile

.PHONY: test

build:
    $(docker) build -t $(tag) .

test:
    @echo "Testing..."