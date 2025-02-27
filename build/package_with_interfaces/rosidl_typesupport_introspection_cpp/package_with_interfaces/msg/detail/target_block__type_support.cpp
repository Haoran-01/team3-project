// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from package_with_interfaces:msg/TargetBlock.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "package_with_interfaces/msg/detail/target_block__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace package_with_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TargetBlock_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) package_with_interfaces::msg::TargetBlock(_init);
}

void TargetBlock_fini_function(void * message_memory)
{
  auto typed_message = static_cast<package_with_interfaces::msg::TargetBlock *>(message_memory);
  typed_message->~TargetBlock();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TargetBlock_message_member_array[2] = {
  {
    "position",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::PoseStamped>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(package_with_interfaces::msg::TargetBlock, position),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "color",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(package_with_interfaces::msg::TargetBlock, color),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TargetBlock_message_members = {
  "package_with_interfaces::msg",  // message namespace
  "TargetBlock",  // message name
  2,  // number of fields
  sizeof(package_with_interfaces::msg::TargetBlock),
  TargetBlock_message_member_array,  // message members
  TargetBlock_init_function,  // function to initialize message memory (memory has to be allocated)
  TargetBlock_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TargetBlock_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TargetBlock_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace package_with_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<package_with_interfaces::msg::TargetBlock>()
{
  return &::package_with_interfaces::msg::rosidl_typesupport_introspection_cpp::TargetBlock_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, package_with_interfaces, msg, TargetBlock)() {
  return &::package_with_interfaces::msg::rosidl_typesupport_introspection_cpp::TargetBlock_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
