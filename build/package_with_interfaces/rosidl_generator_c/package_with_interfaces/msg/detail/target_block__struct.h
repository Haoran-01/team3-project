// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from package_with_interfaces:msg/TargetBlock.idl
// generated code does not contain a copyright notice

#ifndef PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__STRUCT_H_
#define PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/pose_stamped__struct.h"
// Member 'color'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/TargetBlock in the package package_with_interfaces.
/**
  * This message contain target position and target color
 */
typedef struct package_with_interfaces__msg__TargetBlock
{
  geometry_msgs__msg__PoseStamped position;
  rosidl_runtime_c__String color;
} package_with_interfaces__msg__TargetBlock;

// Struct for a sequence of package_with_interfaces__msg__TargetBlock.
typedef struct package_with_interfaces__msg__TargetBlock__Sequence
{
  package_with_interfaces__msg__TargetBlock * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} package_with_interfaces__msg__TargetBlock__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__STRUCT_H_
