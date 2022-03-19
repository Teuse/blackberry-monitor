cmake_minimum_required(VERSION 3.5)
project(air_quality)

set (CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


set(PATH_BSEC_BASE dependencies/BSEC_1.4.8.0_Generic_Release_updated_v3)
set(PATH_BSEC ${PATH_BSEC_BASE}/examples/bsec_iot_example)

set(FILES_BSEC ${PATH_BSEC}/bsec_interface.h
               ${PATH_BSEC}/bsec_datatypes.h
               ${PATH_BSEC}/bsec_integration.c
               ${PATH_BSEC}/bsec_integration.h
               ${PATH_BSEC}/bme680.h
               ${PATH_BSEC}/bme680.c)

set(FILES_AQ i2c_connection.h
             influxdb.hpp)

add_executable(air_quality main.cpp ${FILES_AQ} ${FILES_BSEC})

target_include_directories(air_quality PUBLIC
   # ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/inc
   ${CMAKE_SOURCE_DIR}/${PATH_BSEC})


# if (APPLE)
#    target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/MAC/libalgobsec.a)
#    target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/MAC)

# elseif (UNIX)
#    target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/gcc/Linux/x64/libalgobsec.a)
#    target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/gcc/Linux/x64)
# else ()
add_library(air_quality STATIC IMPORTED GLOBAL)
set_target_properties(air_quality PROPERTIES IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8/libalgobsec.a")
set_target_properties(air_quality PROPERTIES INTERFACE_INCLUDE_DIRECTORIES ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8)

target_link_libraries(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8/libalgobsec.a)
# target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/${PATH_BSEC_BASE}/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8)
# endif()

