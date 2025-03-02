cmake_minimum_required(VERSION 3.15)
project(coin3d CXX)




add_library(coin3d src/coin3d.cpp)
target_include_directories(coin3d PUBLIC include)



set_target_properties(coin3d PROPERTIES PUBLIC_HEADER "include/coin3d.h")
install(TARGETS coin3d)
