project(Atlas)

add_library(atlassim
    STATIC
    AtlasSim.cpp
)

# Atlas simulator
add_executable(atlas atlas.cpp)

target_link_libraries(atlas atlassim atlascore atlasinsts softfloat softfloat atlassys ${SPARTA_LIBS} mavis boost_json)

file (CREATE_LINK ${PROJECT_SOURCE_DIR}/../arch                    ${CMAKE_CURRENT_BINARY_DIR}/arch SYMBOLIC)
file (CREATE_LINK ${PROJECT_SOURCE_DIR}/../mavis/json              ${CMAKE_CURRENT_BINARY_DIR}/mavis_json SYMBOLIC)
