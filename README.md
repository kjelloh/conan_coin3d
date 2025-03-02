# conan_coin3d
A Conan package of the  Coin3D C++ library

250302 - git clone in conanfile.py fails with 'RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly'
         But: git clone from shell in macOS works fine?

## How this project was setup


## Coin3D version Coin 4.0.3

```sh
conan new cmake_lib -d name=coin3d -d version=4.0.3

File saved: CMakeLists.txt
File saved: conanfile.py
File saved: include/coin3d.h
File saved: src/coin3d.cpp
File saved: test_package/CMakeLists.txt
File saved: test_package/conanfile.py
File saved: test_package/src/example.cpp

```
