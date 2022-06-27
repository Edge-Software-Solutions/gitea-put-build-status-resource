import json
import subprocess

import pytest
from helpers import cmd


def test_out(httpbin):
    """Test out action with minimal input."""

    data = {
        'source': {
            'uri': httpbin + '/status/200',
        },
        'version': {}
    }
    subprocess.check_output('scripts/out', input=json.dumps(data).encode())

