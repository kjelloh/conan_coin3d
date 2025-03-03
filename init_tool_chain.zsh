#!/bin/zsh

# Exit the script on any command failure
set -e

conan install . --build=missing
cmake --preset conan-release
