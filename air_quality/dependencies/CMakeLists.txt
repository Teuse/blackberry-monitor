

set(PATH_BSEC_BASE    ${CMAKE_CURRENT_SOURCE_DIR}/bsec_1-4-9-2_generic_release)
set(PATH_BSEC_EXAMPLE ${PATH_BSEC_BASE}/examples)
set(PATH_BSEC_LIB     ${PATH_BSEC_BASE}/algo/normal_version/bin/gcc/Linux/x64)

set(FILES_BSEC ${PATH_BSEC_EXAMPLE}/bsec_interface.h
               ${PATH_BSEC_EXAMPLE}/bsec_datatypes.h
               ${PATH_BSEC_EXAMPLE}/bsec_integration.c
               ${PATH_BSEC_EXAMPLE}/bsec_integration.h
               ${PATH_BSEC_EXAMPLE}/bme680.h
               ${PATH_BSEC_EXAMPLE}/bme680.c)


add_library(bme680 STATIC ${FILES_BSEC})

# target_compile_options(bme680 PRIVATE -Wno-unused-but-set-variable -Wno-unused-variable)

link_directories(${PATH_BSEC_LIB})

if(EXISTS "${PATH_BSEC_LIB}/libalgobsec.a")
	set_target_properties(bme680 PROPERTIES IMPORTED_LOCATION ${PATH_BSEC_LIB}/libalgobsec.a)
	target_link_libraries(bme680 PUBLIC ${PATH_BSEC_LIB}/libalgobsec.a)
else()
	message("Library algobsec.a missing")
endif()

target_include_directories(bme680 PUBLIC ${PATH_BSEC_EXAMPLE}) 
#${PATH_BSEC_LIB})

# For some reason, math library isn't implicitly imported so that needs to be manually
# done for now. You might be able to get rid of the hack at some point
target_link_libraries(bme680 PUBLIC m)