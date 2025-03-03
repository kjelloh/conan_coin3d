cmake_minimum_required(VERSION 3.20)
project(coin3d CXX)

find_package(Boost)


# In effect: cmake -Hcoin -Bcoin_build -G "Unix Makefiles" -DCOIN_BUILD_DOCUMENTATION=OFF -DCOIN_BUILD_MAC_FRAMEWORK=OFF
set(COIN_BUILD_DOCUMENTATION OFF CACHE BOOL "Disable documentation")
set(COIN_BUILD_MAC_FRAMEWORK OFF CACHE BOOL "Disable Mac framework")

# patch CMAKE_MODULE_PATH to work with 'our' CMAKE_SOURCE_DIR
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/coin/cmake" ${CMAKE_MODULE_PATH})

add_subdirectory(coin)