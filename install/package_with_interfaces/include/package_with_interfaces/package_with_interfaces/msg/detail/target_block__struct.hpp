// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from package_with_interfaces:msg/TargetBlock.idl
// generated code does not contain a copyright notice

#ifndef PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__STRUCT_HPP_
#define PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/pose_stamped__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__package_with_interfaces__msg__TargetBlock __attribute__((deprecated))
#else
# define DEPRECATED__package_with_interfaces__msg__TargetBlock __declspec(deprecated)
#endif

namespace package_with_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TargetBlock_
{
  using Type = TargetBlock_<ContainerAllocator>;

  explicit TargetBlock_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->color = "";
    }
  }

  explicit TargetBlock_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_alloc, _init),
    color(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->color = "";
    }
  }

  // field types and members
  using _position_type =
    geometry_msgs::msg::PoseStamped_<ContainerAllocator>;
  _position_type position;
  using _color_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _color_type color;

  // setters for named parameter idiom
  Type & set__position(
    const geometry_msgs::msg::PoseStamped_<ContainerAllocator> & _arg)
  {
    this->position = _arg;
    return *this;
  }
  Type & set__color(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->color = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    package_with_interfaces::msg::TargetBlock_<ContainerAllocator> *;
  using ConstRawPtr =
    const package_with_interfaces::msg::TargetBlock_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      package_with_interfaces::msg::TargetBlock_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      package_with_interfaces::msg::TargetBlock_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__package_with_interfaces__msg__TargetBlock
    std::shared_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__package_with_interfaces__msg__TargetBlock
    std::shared_ptr<package_with_interfaces::msg::TargetBlock_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TargetBlock_ & other) const
  {
    if (this->position != other.position) {
      return false;
    }
    if (this->color != other.color) {
      return false;
    }
    return true;
  }
  bool operator!=(const TargetBlock_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TargetBlock_

// alias to use template instance with default allocator
using TargetBlock =
  package_with_interfaces::msg::TargetBlock_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace package_with_interfaces

#endif  // PACKAGE_WITH_INTERFACES__MSG__DETAIL__TARGET_BLOCK__STRUCT_HPP_
