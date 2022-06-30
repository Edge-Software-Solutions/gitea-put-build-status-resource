docker=docker
<<<<<<< HEAD
tag = gitea-put-build-status-resource
=======
tag = objectivetruth/gitea-put-build-status-resource
>>>>>>> master

.PHONY: test

build:
<<<<<<< HEAD
	@echo 'Building...'
	$(docker) build --target concourse_resource_build -t $(tag) .
=======
	$(docker) --target concourse_resource_test -t $(tag) .
>>>>>>> master

test:
	@echo 'Testing...'
	$(docker) build --target concourse_resource_test -t $(tag):test .
