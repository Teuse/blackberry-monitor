cmake_minimum_required(VERSION 3.5)

project(air_quality)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)


set(FILES_BME680 BME680_driver-bme680_v3.5.9/bme680.h
                 BME680_driver-bme680_v3.5.9/bme680.c)

set(FILES_BSEC BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/inc/bsec_interface.h
               BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/inc/bsec_datatypes.h)


add_executable(air_quality main.cpp ${FILES_BME680} ${FILES_BSEC})

target_include_directories(air_quality PUBLIC
   ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/inc
   ${CMAKE_SOURCE_DIR}/BME680_driver-bme680_v3.5.9)

if (APPLE)
   target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/MAC/libalgobsec.a)
   target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/MAC)

elseif (UNIX)
   target_link_libraries(air_quality ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8/libalgobsec.a)
   target_include_directories(air_quality PUBLIC ${CMAKE_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3/algo/normal_version/bin/RaspberryPi/PiThree_ArmV8)
endif()

