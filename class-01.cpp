#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <cassert>

using namespace std;
struct GMMemoryStats{
    size_t bytes_read = 0;
    size_t bytes_written = 0;

    void reset() {
        bytes_read = 0;
        bytes_written = 0;
    }   

    size_t total_bytes() const {
        return bytes_read + bytes_written;
    }
};

static GMMemoryStats gmm_stats;

template <typename T>
void gmm_read(T* ptr, size_t count) {
    gmm_stats.bytes_read += count * sizeof(T);
    // Simulate reading from memory
    for (size_t i = 0; i < count; ++i) {
        volatile T temp = ptr[i]; // Prevent optimization
    }
}

template <typename T>
void gmm_write(T* ptr, size_t count) {
    gmm_stats.bytes_written += count * sizeof(T);
    // Simulate writing to memory
    for (size_t i = 0; i < count; ++i) {
        ptr[i] = static_cast<T>(i); // Example write operation
    }
}

inline float fast_gelu(float x) {
    return x / (1.0f + exp(-1.702f * x));
}

void path_independent(const float*x,const float*z, float* y, int n) {
    for (int i = 0; i < n; ++i) {
        gmm_read(x + i, 1);
        gmm_read(z + i, 1);
        y[i] = fast_gelu(x[i] + z[i]);
        gmm_write(y + i, 1);
    }
}

int main(){

}