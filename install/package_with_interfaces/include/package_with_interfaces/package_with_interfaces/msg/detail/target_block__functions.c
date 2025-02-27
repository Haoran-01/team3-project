// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from package_with_interfaces:msg/TargetBlock.idl
// generated code does not contain a copyright notice
#include "package_with_interfaces/msg/detail/target_block__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `position`
#include "geometry_msgs/msg/detail/pose_stamped__functions.h"
// Member `color`
#include "rosidl_runtime_c/string_functions.h"

bool
package_with_interfaces__msg__TargetBlock__init(package_with_interfaces__msg__TargetBlock * msg)
{
  if (!msg) {
    return false;
  }
  // position
  if (!geometry_msgs__msg__PoseStamped__init(&msg->position)) {
    package_with_interfaces__msg__TargetBlock__fini(msg);
    return false;
  }
  // color
  if (!rosidl_runtime_c__String__init(&msg->color)) {
    package_with_interfaces__msg__TargetBlock__fini(msg);
    return false;
  }
  return true;
}

void
package_with_interfaces__msg__TargetBlock__fini(package_with_interfaces__msg__TargetBlock * msg)
{
  if (!msg) {
    return;
  }
  // position
  geometry_msgs__msg__PoseStamped__fini(&msg->position);
  // color
  rosidl_runtime_c__String__fini(&msg->color);
}

bool
package_with_interfaces__msg__TargetBlock__are_equal(const package_with_interfaces__msg__TargetBlock * lhs, const package_with_interfaces__msg__TargetBlock * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // position
  if (!geometry_msgs__msg__PoseStamped__are_equal(
      &(lhs->position), &(rhs->position)))
  {
    return false;
  }
  // color
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->color), &(rhs->color)))
  {
    return false;
  }
  return true;
}

bool
package_with_interfaces__msg__TargetBlock__copy(
  const package_with_interfaces__msg__TargetBlock * input,
  package_with_interfaces__msg__TargetBlock * output)
{
  if (!input || !output) {
    return false;
  }
  // position
  if (!geometry_msgs__msg__PoseStamped__copy(
      &(input->position), &(output->position)))
  {
    return false;
  }
  // color
  if (!rosidl_runtime_c__String__copy(
      &(input->color), &(output->color)))
  {
    return false;
  }
  return true;
}

package_with_interfaces__msg__TargetBlock *
package_with_interfaces__msg__TargetBlock__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  package_with_interfaces__msg__TargetBlock * msg = (package_with_interfaces__msg__TargetBlock *)allocator.allocate(sizeof(package_with_interfaces__msg__TargetBlock), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(package_with_interfaces__msg__TargetBlock));
  bool success = package_with_interfaces__msg__TargetBlock__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
package_with_interfaces__msg__TargetBlock__destroy(package_with_interfaces__msg__TargetBlock * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    package_with_interfaces__msg__TargetBlock__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
package_with_interfaces__msg__TargetBlock__Sequence__init(package_with_interfaces__msg__TargetBlock__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  package_with_interfaces__msg__TargetBlock * data = NULL;

  if (size) {
    data = (package_with_interfaces__msg__TargetBlock *)allocator.zero_allocate(size, sizeof(package_with_interfaces__msg__TargetBlock), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = package_with_interfaces__msg__TargetBlock__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        package_with_interfaces__msg__TargetBlock__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
package_with_interfaces__msg__TargetBlock__Sequence__fini(package_with_interfaces__msg__TargetBlock__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      package_with_interfaces__msg__TargetBlock__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

package_with_interfaces__msg__TargetBlock__Sequence *
package_with_interfaces__msg__TargetBlock__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  package_with_interfaces__msg__TargetBlock__Sequence * array = (package_with_interfaces__msg__TargetBlock__Sequence *)allocator.allocate(sizeof(package_with_interfaces__msg__TargetBlock__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = package_with_interfaces__msg__TargetBlock__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
package_with_interfaces__msg__TargetBlock__Sequence__destroy(package_with_interfaces__msg__TargetBlock__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    package_with_interfaces__msg__TargetBlock__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
package_with_interfaces__msg__TargetBlock__Sequence__are_equal(const package_with_interfaces__msg__TargetBlock__Sequence * lhs, const package_with_interfaces__msg__TargetBlock__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!package_with_interfaces__msg__TargetBlock__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
package_with_interfaces__msg__TargetBlock__Sequence__copy(
  const package_with_interfaces__msg__TargetBlock__Sequence * input,
  package_with_interfaces__msg__TargetBlock__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(package_with_interfaces__msg__TargetBlock);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    package_with_interfaces__msg__TargetBlock * data =
      (package_with_interfaces__msg__TargetBlock *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!package_with_interfaces__msg__TargetBlock__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          package_with_interfaces__msg__TargetBlock__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!package_with_interfaces__msg__TargetBlock__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
