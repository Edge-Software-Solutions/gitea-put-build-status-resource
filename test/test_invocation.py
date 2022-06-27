import json
import subprocess

import pytest
from helpers import cmd


def test_out(httpbin):
    """Test out action with minimal input."""

    data = {
        'source': {
            'uri': httpbin + '/status/200',
            'no_ssl': 'true'
        },
        'version': {},
        'params': {
            'repository': 'test_repo',
            'status': 'success'
        }
    }
    subprocess.check_output(['scripts/out', '/tmp'], input=json.dumps(data).encode(), env={
        'ATC_EXTERNAL_URL': 'https://extena.io',
        'BUILD_TEAM_NAME': 'team',
        'BUILD_PIPELINE_NAME': 'pipeline',
        'BUILD_JOB_NAME': 'job',
        'BUILD_NAME': 'build'
    })


def test_empty_check(httpbin):
    """Check must return an empty response but not nothing."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
    }

    check = cmd('check', source)

    assert check == []


