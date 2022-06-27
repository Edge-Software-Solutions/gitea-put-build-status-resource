#!/bin/sh

# fail if one command fails
set -e

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# test
#pylama /opt/scripts /opt/test/
py.test -l --tb=short -r fE "${SCRIPT_DIR}"

# cleanup
rm -fr /tmp/*