def test_out_failure(httpbin):
    """Test action failing if not OK http response."""

    data = {
        'source': {
            'uri': httpbin + '/status/404',
        },
        'version': {}
    }
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('/opt/scripts/out', input=json.dumps(data).encode())


def test_auth(httpbin):
    """Test basic authentication."""

    data = {
        'source': {
            'uri': 'http://user:password@{0.host}:{0.port}/basic-auth/user/password'.format(httpbin),
        },
    }
    subprocess.check_output('/opt/scripts/out', input=json.dumps(data).encode())


def test_json(httpbin):
    """Json should be passed as JSON content."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'json': {
            'test': 123,
        },
        'version': {}
    }

    output = cmd('out', source)

    assert output['json']['test'] == 123
    assert output['version'] == {}


def test_interpolation(httpbin):
    """Values should be interpolated recursively."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'json': {
            'object': {
                'test': '{BUILD_NAME}'
            },
            'array': [
                '{BUILD_NAME}'
            ]
        }
    }

    output = cmd('out', source)

    assert output['json']['object']['test'] == '1'
    assert output['json']['array'][0] == '1'
    assert output['version'] == {}


def test_data_urlencode(httpbin):
    """Test passing URL encoded data."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'form_data': {
            'field': {
                'test': 123,
            },
        }
    }

    output = cmd('out', source)

    assert output['form'] == {'field': '{"test": 123}'}
    assert output['version'] == {}


def test_data_ensure_ascii(httpbin):
    """Test form_data json ensure_ascii."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'form_data': {
            'field': {
                'test': '日本語',
            },
        },
    }

    output = cmd('out', source)

    assert output['form'] == {'field': '{"test": "日本語"}'}


def test_not_parsed_data(httpbin):
    """Test form_data in a standard format."""

    source = {
        'uri': httpbin + '/post',
        'method': 'POST',
        'parse_form_data': False,
        'form_data': {
            'firstname': 'John',
            'lastname': 'Doe'
        }
    }

    output = cmd('out', source)

    assert output['form'] == {"firstname": "John", "lastname": "Doe"}
    assert output['version'] == {}
