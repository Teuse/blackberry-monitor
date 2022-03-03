cmake_minimum_required(VERSION 3.5)
project(air_quality)

set (CMAKE_CXX_STANDARD 17)

set(PATH_BSEC BSEC_1.4.8.0_Generic_Release_updated_v3/examples/bsec_iot_example)
set(FILES_BSEC ${PATH_BSEC}/bsec_interface.h
               ${PATH_BSEC}/bsec_datatypes.h
               ${PATH_BSEC}/bsec_integration.c
               ${PATH_BSEC}/bsec_integration.h
               ${PATH_BSEC}/bme680.h
               ${PATH_BSEC}/bme680.c)

set(FILES_AQ i2c_connection.h
             influx_client.h)

add_executable(air_quality main.cpp ${FILES_AQ} ${FILES_BSEC})

target_include_directories(air_quality PUBLIC
   ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/inc
   ${CMAKE_SOURCE_DIR}/BME680_driver-bme680_v3.5.9
   ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/examples/bsec_iot_example)

if (APPLE)
   target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/MAC/libalgobsec.a)
   target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/MAC)

elseif (UNIX)
   target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/gcc/Linux/x64/libalgobsec.a)
   target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/gcc/Linux/x64)
# else ()
# target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8/libalgobsec.a)
#    target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8)
endif()

