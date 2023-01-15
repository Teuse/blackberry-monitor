cmake_minimum_required(VERSION 3.5)
project(air_quality)

set (CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CC /usr/bin/arm-linux-gnueabihf-gcc-10)
set(CXX /usr/bin/arm-linux-gnueabihf-gcc-10)

set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -marm")

add_subdirectory(dependencies) 

set(FILES_AQ i2c_connection.h
             influxdb.hpp)

add_executable(air_quality main.cpp ${FILES_AQ})

target_link_libraries(air_quality PUBLIC bme680)
