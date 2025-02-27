// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from package_with_interfaces:msg/TargetBlock.idl
// generated code does not contain a copyright notice

#ifndef PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__BUILDER_HPP_
#define PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "package_with_interfaces/msg/detail/target_block__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace package_with_interfaces
{

namespace msg
{

namespace builder
{

class Init_TargetBlock_color
{
public:
  explicit Init_TargetBlock_color(::package_with_interfaces::msg::TargetBlock & msg)
  : msg_(msg)
  {}
  ::package_with_interfaces::msg::TargetBlock color(::package_with_interfaces::msg::TargetBlock::_color_type arg)
  {
    msg_.color = std::move(arg);
    return std::move(msg_);
  }

private:
  ::package_with_interfaces::msg::TargetBlock msg_;
};

class Init_TargetBlock_position
{
public:
  Init_TargetBlock_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TargetBlock_color position(::package_with_interfaces::msg::TargetBlock::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_TargetBlock_color(msg_);
  }

private:
  ::package_with_interfaces::msg::TargetBlock msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::package_with_interfaces::msg::TargetBlock>()
{
  return package_with_interfaces::msg::builder::Init_TargetBlock_position();
}

}  // namespace package_with_interfaces

#endif  // PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__BUILDER_HPP_
