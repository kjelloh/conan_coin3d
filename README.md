# conan_coin3d
A Conan package of the  Coin3D C++ library

250302 - git clone in conanfile.py fails with 'RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly'
         But: git clone from shell in macOS works fine?

# How this project was setup

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

## coin README for installation

This project relies on the information in the coin README for installation: https://github.com/coin3d/coin/blob/master/INSTALL 

## conan source from Github including submodules

```sh
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/conan_coin3d % git clone --recurse-submodules https://github.com/coin3d/coin.git
Cloning into 'coin'...
remote: Enumerating objects: 210894, done.
remote: Counting objects: 100% (76553/76553), done.
remote: Compressing objects: 100% (11175/11175), done.
remote: Total 210894 (delta 76158), reused 65378 (delta 65378), pack-reused 134341 (from 4)
Receiving objects: 100% (210894/210894), 113.94 MiB | 2.37 MiB/s, done.
Resolving deltas: 100% (188922/188922), done.
Submodule 'build/general' (https://github.com/coin3d/generalmsvcgeneration) registered for path 'build/general'
Submodule 'cpack.d' (https://github.com/coin3d/cpack.d) registered for path 'cpack.d'
Submodule 'docs/doxygen-awesome' (https://github.com/coin3d/doxygen-awesome-css.git) registered for path 'docs/doxygen-awesome'
Cloning into '/Users/kjell-olovhogdahl/Documents/GitHub/conan_coin3d/coin/build/general'...
remote: Enumerating objects: 13, done.        
remote: Counting objects: 100% (13/13), done.        
remote: Compressing objects: 100% (8/8), done.        
remote: Total 13 (delta 5), reused 13 (delta 5), pack-reused 0 (from 0)        
Receiving objects: 100% (13/13), done.
Resolving deltas: 100% (5/5), done.
Cloning into '/Users/kjell-olovhogdahl/Documents/GitHub/conan_coin3d/coin/cpack.d'...
remote: Enumerating objects: 181, done.        
remote: Counting objects: 100% (181/181), done.        
remote: Compressing objects: 100% (72/72), done.        
remote: Total 181 (delta 113), reused 172 (delta 106), pack-reused 0 (from 0)        
Receiving objects: 100% (181/181), 31.65 KiB | 704.00 KiB/s, done.
Resolving deltas: 100% (113/113), done.
Cloning into '/Users/kjell-olovhogdahl/Documents/GitHub/conan_coin3d/coin/docs/doxygen-awesome'...
remote: Enumerating objects: 958, done.        
remote: Counting objects: 100% (380/380), done.        
remote: Compressing objects: 100% (80/80), done.        
remote: Total 958 (delta 340), reused 300 (delta 300), pack-reused 578 (from 2)        
Receiving objects: 100% (958/958), 7.59 MiB | 1.90 MiB/s, done.
Resolving deltas: 100% (577/577), done.
Submodule path 'build/general': checked out 'a61fae6a84bd57364fa07a5345eeb4b7ae030318'
Submodule path 'cpack.d': checked out '118ac5a21bcf57f0f90e2b0e681c9dcbf07074c2'
Submodule path 'docs/doxygen-awesome': checked out '6217657eef6aec24a0e4ecea4695031c1a622cf3'
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/conan_coin3d % 
```

The Coin3D Github repo is about 200 MB.


```sh
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/conan_coin3d % du -sh coin       

202M    coin
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/conan_coin3d % 
```