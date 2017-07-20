# /usr/bin/env

pushd `pwd`

cd ..
python setup.py build bdist

popd
