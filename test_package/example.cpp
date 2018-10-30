#include <iostream>
#include "pstl/execution"
#include "pstl/algorithm"

int main() {
    std::array<int, 4> a{2, 3, 1, 4};
    std::sort(std::execution::par_unseq, a.begin(), a.end());
}
