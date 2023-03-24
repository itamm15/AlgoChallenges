// https://leetcode.com/problems/longest-common-prefix/
#include <iostream>
#include <vector>
#include <string>

int main() {
  // Sample vector
  std::vector<std::string> strs = {"flower", "flow", "flight"};
  bool prefixes_are_the_same = true;
  int index = 0;
  int longest_common_prefix = 0;
  char prefix = strs[0][0];
  while(prefixes_are_the_same && longest_common_prefix != strs[0].length()) {
    for (auto &value : strs) {
      if(value[index] != prefix) prefixes_are_the_same = false;
    }
    if(prefixes_are_the_same) {
      longest_common_prefix++;
      index++;
      prefix = strs[0][index];
    }
  }

  std::cout << strs[0].substr(0, longest_common_prefix);
}
