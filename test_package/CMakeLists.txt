PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}")

message(STATUS ": ${CMAKE_MODULE_PATH}")
find_package(ParallelSTL)
ADD_EXECUTABLE(example example.cpp)
TARGET_LINK_LIBRARIES(example pstl::ParallelSTL)
