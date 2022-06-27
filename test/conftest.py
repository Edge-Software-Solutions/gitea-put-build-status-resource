import subprocess


def pytest_sessionstart(session):
    """
    Called after the ``sessionstart`` hook has been called.
    Initialize a repo and create initial commit
    """
    print("==========================")
    print("Creating repo and initial commit in /tmp/test_repo for tests...")
    subprocess.run(['mkdir', '-p', '/tmp/test_repo'])
    subprocess.run(['git', 'init', '-q'], cwd='/tmp/test_repo')
    subprocess.run(['git', 'config', 'user.email', 'foo@example.com', '-q'], cwd='/tmp/test_repo')
    subprocess.run(['touch', 'foo'], cwd='/tmp/test_repo')
    subprocess.run(['git', 'add', '.'], cwd='/tmp/test_repo')
    subprocess.run(['git', 'commit', '-m', '"test_commit"', '-q'], cwd='/tmp/test_repo')
    print("...done")
