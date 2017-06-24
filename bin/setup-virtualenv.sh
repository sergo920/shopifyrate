#!/bin/bash
#
# This script setups virtual environment either in default directory or where you specify it
#

## Get real path of current script file ##
_script="$(readlink -f ${BASH_SOURCE[0]})"

## Delete last component from $_script ##
_mydir="$(dirname ${_script})"

#APP_DIR=/var/www/html/kilometer/kilometer-website
APP_VIRTUAL_ENV='venv'

APP_DIR=$(dirname ${_mydir})
if [ $# -gt 1 ]; then
    APP_DIR=$1
fi

if [ $# -gt 1 ]; then
  APP_VIRTUAL_ENV=$2
fi

pushd "${APP_DIR}"

if [ -d "$(pwd)/$APP_VIRTUAL_ENV" ]; then
  rm -rf "$(pwd)/${APP_VIRTUAL_ENV}"
  echo "Removed existing virtual environment"
fi

echo -e "setup-virtualenv:\n\tUSER=${USER}\n\t_mydir=${_mydir}\n\tAPP_DIR=${APP_DIR}\n\tAPP_VIRTUAL_ENV=${APP_VIRTUAL_ENV};\n\tpwd(line 32)=$(pwd)"

echo "Installing a fresh virtual environment"

echo "Create Python VirtualEnvironment in '$(pwd)/${APP_VIRTUAL_ENV}'"
virtualenv --python='python3' "$(pwd)/${APP_VIRTUAL_ENV}"

source ./venv/bin/activate
pip install -r ./requirements.txt
deactivate

popd

exit 0