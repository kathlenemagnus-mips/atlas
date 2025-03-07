#!/usr/bin/env bash

set -x

source "/usr/share/miniconda/etc/profile.d/conda.sh"
conda activate riscv_func_model

echo "Starting Build Entry"
echo "HOME:" $HOME
echo "GITHUB_WORKSPACE:" $GITHUB_WORKSPACE
echo "GITHUB_EVENT_PATH:" $GITHUB_EVENT_PATH
echo "CONDA_PREFIX:" $CONDA_PREFIX
echo "PWD:" `pwd`

CXX_COMPILER=${COMPILER/clang/clang++}

#
# Compile Sparta Infra (always build with release)
#   Have other build types point to release
#
echo "Building Sparta Infra"
cd ${GITHUB_WORKSPACE}/map/sparta
mkdir -p release
cd release
CC=$COMPILER CXX=$CXX_COMPILER  cmake ..-DCMAKE_BUILD_TYPE=Release -DGEN_DEBUG_INFO=OFF -DCMAKE_INSTALL_PREFIX=${CONDA_PREFIX}
if [ $? -ne 0 ]; then
    echo "ERROR: CMake for Sparta framework failed"
    exit 0
fi
make -j$(nproc --all) install > install.log
BUILD_SPARTA=$?
if [ ${BUILD_SPARTA} -ne 0 ]; then
    echo "ERROR: build sparta FAILED!!!"
    echo "$(<install.log)"
    exit 1
fi
rm install.log

cd ${GITHUB_WORKSPACE}
mkdir $ATLAS_BUILD_TYPE
cd $ATLAS_BUILD_TYPE
cmake ..  -DCMAKE_C_COMPILER=$COMPILER -DCMAKE_CXX_COMPILER=$CXX_COMPILER -DCMAKE_BUILD_TYPE=$ATLAS_BUILD_TYPE -DGEN_DEBUG_INFO=OFF
if [ $? -ne 0 ]; then
    echo "ERROR: CMake for atlas failed"
    exit 1
fi
make -j$(nproc --all) regress > regress.log
BUILD_ATLAS=$?
if [ ${BUILD_ATLAS} -ne 0 ]; then
    echo "ERROR: build/regress of Atlas FAILED!!!"
    echo "$(<regress.log)"
    exit 1
fi
rm regress.log
