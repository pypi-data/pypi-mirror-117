# Copy the repository in a data folder, to be packaged by setuptools
rsync -av --progress . ./data --exclude data --exclude .git --exclude .github --exclude dist --exclude build
# Run CMake to generate the `setup.py` build file
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$PWD/product
# Extract setup.py
mv pynest/setup.py ..
cd ..
# Extract the nest Python files
cp -r pynest/* .
# Use `setup.py` to package the data folder and nest code folder into a source distribution.
python setup.py sdist
