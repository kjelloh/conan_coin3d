#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define COIN3D_EXPORT __declspec(dllexport)
#else
  #define COIN3D_EXPORT
#endif

COIN3D_EXPORT void coin3d();
COIN3D_EXPORT void coin3d_print_vector(const std::vector<std::string> &strings);
