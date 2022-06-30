import json
import subprocess

import pytest
from helpers import cmd
from pytest_httpserver import HTTPServer


def test_out(httpserver: HTTPServer):
    """Test out action with minimal input."""
    httpserver\
        .expect_request('^/api/v1/repos/myname/myproject/statuses/',
                        method='POST')

    data = {
        'source': {
            'uri': 'http://' + httpserver.host + ':' + str(httpserver.port) + '/myname/myproject.git',
            'no_ssl': 'true'
        },
        'version': {},
        'params': {
            'repository': 'test_repo',
            'status': 'success'
        }
    }
    subprocess.check_output(['scripts/out', '/tmp'], input=json.dumps(data).encode(), env={
        'ATC_EXTERNAL_URL': 'https://concourse.criticalinfra.home.objectivetruth.ca',
        'BUILD_TEAM_NAME': 'fake_team',
        'BUILD_PIPELINE_NAME': 'fake_pipeline',
        'BUILD_JOB_NAME': 'fake_job',
        'BUILD_NAME': '9'
    })


def test_empty_check(httpserver: HTTPServer):
    """Check must return an empty response but not nothing."""

    source = {
        'uri': 'http://' + httpserver.host + ':' + str(httpserver.port) + '/myname/myproject.git',
        'no_ssl': 'true'
    }

    check = cmd('check', source)

    assert check == []


