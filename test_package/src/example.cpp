#include "coin3d.h"
#include <vector>
#include <string>

int main() {
    coin3d();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    coin3d_print_vector(vec);
}
