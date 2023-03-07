// https://leetcode.com/problems/palindrome-number/
#include <iostream>
#include <string>

int main() {
  int number;
  std::cin >> number;
  if(number < 0) {
    std::cout << "false";
    return 0;
  }

  std::string parsed_number = std::to_string(number);
  const auto parsed_number_length = parsed_number.length();
  for (int index = 0; index < int(parsed_number_length/2); index++) {
    if (parsed_number[index] != parsed_number[parsed_number_length - index - 1]) {
      std::cout << "false";
      return 0;
    }
  }
  std::cout << "true";
}
