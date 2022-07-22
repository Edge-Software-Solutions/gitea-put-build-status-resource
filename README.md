# Gitea Put Build Status Resource ![Docker Pulls](https://img.shields.io/docker/pulls/edgesoftwaresolution/gitea-put-build-status-resource)

A concourse resource to put build statuses to gitea

## Source Configuration

```yaml
resource_types:
- name: gitea-put-build-status
  type: docker-image
  source:
    repository: edgesoftwaresolutions/gitea-put-build-status-resource

resources:
- name: my-repo-build-status
  type: gitea-put-build-status
  source:
    uri: https://my.gitea.host/myname/myproject.git
    private_token: XXX
```

* `uri`: The location of the repository (required)
* `private_token`: Your Gitea user's private token (required, can be found in your profile settings)
* `no_ssl`: Set to `true` if the Gitea API should be used over HTTP instead of HTTPS

> Please note that you have to provide either `private_key` or `username` and `password`.

## Behavior

### `check` and `in` are not implemented


### `out`: Update a pull request's pull status

Updates the pull request's `status` which displays nicely in the Gitea UI and allows to only pull changes if they pass the test.

#### Parameters

* `repository`: The path of the repository of the pull request's source branch (required)
* `status`: The new status of the pull request (required, can be either `pending`, `pending`, `error`, `failure`, or `warning`)
* `build_label`: The label of the build in Gitea (optional, defaults to `"Concourse"`)
* `description`: The description to pass to Gitea (optional)

## Example

```yaml
jobs:
- name: test-pull-request
  plan:
  - get: repo
    resource: repo-mr
    trigger: true
  - put: repo-mr
    params:
      repository: repo
      status: running
  - task: run-tests
    file: repo/ci/tasks/run-tests.yml
  on_failure:
    put: repo-mr
    params:
      repository: repo
      status: failed
  on_success:
    put: repo-mr
    params:
      repository: repo
      status: success
```
