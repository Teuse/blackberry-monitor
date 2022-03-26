

set(PATH_BSEC_BASE    ${CMAKE_CURRENT_SOURCE_DIR}/BSEC_1.4.8.0_Generic_Release_updated_v3)
set(PATH_BSEC_EXAMPLE ${PATH_BSEC_BASE}/examples/bsec_iot_example)
set(PATH_BSEC_LIB     ${PATH_BSEC_BASE}/algo/normal_version/bin/gcc/Linux/x64)

set(FILES_BSEC ${PATH_BSEC_EXAMPLE}/bsec_interface.h
               ${PATH_BSEC_EXAMPLE}/bsec_datatypes.h
               ${PATH_BSEC_EXAMPLE}/bsec_integration.c
               ${PATH_BSEC_EXAMPLE}/bsec_integration.h
               ${PATH_BSEC_EXAMPLE}/bme680.h
               ${PATH_BSEC_EXAMPLE}/bme680.c)


add_library(bme680 STATIC ${FILES_BSEC})

# target_compile_options(bme680 PRIVATE -Wno-unused-but-set-variable -Wno-unused-variable)

if(EXISTS "${PATH_BSEC_LIB}/libalgobsec.a")
	target_link_libraries(bme680 PUBLIC ${PATH_BSEC_LIB}/libalgobsec.a)
else()
	message("Library algobsec.a missing")
endif()


target_include_directories(bme680 PUBLIC ${PATH_BSEC_EXAMPLE}) 
#${PATH_BSEC_LIB})

# For some reason, math library isn't implicitly imported so that needs to be manually
# done for now. You might be able to get rid of the hack at some point
target_link_libraries(bme680 PUBLIC m)