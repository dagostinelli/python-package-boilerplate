# /usr/bin/env

pushd `pwd`

# put us into the right place (relative to the script itself)
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ..
python setup.py build bdist

popd
