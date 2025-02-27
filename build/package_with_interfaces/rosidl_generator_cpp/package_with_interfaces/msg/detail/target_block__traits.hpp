// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from package_with_interfaces:msg/TargetBlock.idl
// generated code does not contain a copyright notice

#ifndef PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__TRAITS_HPP_
#define PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "package_with_interfaces/msg/detail/target_block__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"

namespace package_with_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const TargetBlock & msg,
  std::ostream & out)
{
  out << "{";
  // member: position
  {
    out << "position: ";
    to_flow_style_yaml(msg.position, out);
    out << ", ";
  }

  // member: color
  {
    out << "color: ";
    rosidl_generator_traits::value_to_yaml(msg.color, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TargetBlock & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position:\n";
    to_block_style_yaml(msg.position, out, indentation + 2);
  }

  // member: color
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "color: ";
    rosidl_generator_traits::value_to_yaml(msg.color, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TargetBlock & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace package_with_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use package_with_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const package_with_interfaces::msg::TargetBlock & msg,
  std::ostream & out, size_t indentation = 0)
{
  package_with_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use package_with_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const package_with_interfaces::msg::TargetBlock & msg)
{
  return package_with_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<package_with_interfaces::msg::TargetBlock>()
{
  return "package_with_interfaces::msg::TargetBlock";
}

template<>
inline const char * name<package_with_interfaces::msg::TargetBlock>()
{
  return "package_with_interfaces/msg/TargetBlock";
}

template<>
struct has_fixed_size<package_with_interfaces::msg::TargetBlock>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<package_with_interfaces::msg::TargetBlock>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<package_with_interfaces::msg::TargetBlock>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__TRAITS_HPP_
