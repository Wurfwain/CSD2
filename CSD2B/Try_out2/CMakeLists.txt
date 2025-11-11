cmake_minimum_required(VERSION 3.20)
project(CMakeTestProject LANGUAGES CXX)

add_executable(example Try_out2.cpp)
target_compile_features(example PRIVATE cxx_std_20)