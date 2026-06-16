# cmake_minimum_required(VERSION 3.0.2)
# PROJECT(zed_config_export)

# if(COMMAND cmake_policy)
# 	cmake_policy(SET CMP0003 OLD)
# 	cmake_policy(SET CMP0015 OLD)
# endif(COMMAND cmake_policy)

# SET(CMAKE_BUILD_TYPE "RelWithDebInfo")
# SET(EXECUTABLE_OUTPUT_PATH ".")

# find_package(ZED 3 REQUIRED)
# find_package(CUDA ${ZED_CUDA_VERSION} EXACT REQUIRED)

# include_directories(${ZED_INCLUDE_DIRS})
# include_directories(${CUDA_INCLUDE_DIRS})

# link_directories(${ZED_LIBRARY_DIR})

# ADD_EXECUTABLE(${PROJECT_NAME} main.cpp)
# add_definitions(-std=c++14)

# TARGET_LINK_LIBRARIES(${PROJECT_NAME} ${ZED_LIBRARIES})

# # ------------------------------

# # Use catkin_simple to automate the standard ROS boilerplate
# find_package(catkin REQUIRED COMPONENTS catkin_simple roscpp)
# catkin_simple()

# # The original code still requires the ZED SDK to be present in the Docker environment
# find_package(ZED 3 REQUIRED)
# find_package(CUDA ${ZED_CUDA_VERSION} EXACT REQUIRED)

# # Include paths for ZED and CUDA
# include_directories(${ZED_INCLUDE_DIRS} ${CUDA_INCLUDE_DIRS})

# # Create the executable
# # Changed from ${PROJECT_NAME} to fixed name so "rosrun kalibr zed_config_export" works
# cs_add_executable(zed_config_export main.cpp)
# add_definitions(-std=c++14)

# # Link ZED libraries
# target_link_libraries(zed_config_export ${ZED_LIBRARIES})

# # catkin_simple automatically handles the install() and catkin_package() calls
# cs_install()
# cs_export()