# LeetCode Solutions

Python solutions for beginner-friendly LeetCode problems.

## Problems Solved

| # | Problem | File | Concepts |
|---|---|---|---|
| 1 | Two Sum | `two_sum.py` | Arrays, nested loops, pair checking |
| 3 | Longest Substring Without Repeating Characters | `longest_substring_without_repeating_characters.py` | Strings, sliding window, hash map |
| 14 | Longest Common Prefix | `longest_common_prefix.py` | Strings, sorting, prefix matching |
| 15 | 3Sum | `three_sum.py` | Sorting, two pointers, duplicate handling |
| 20 | Valid Parentheses | `valid_parentheses.py` | Strings, stack, bracket matching |
| 26 | Remove Duplicates from Sorted Array | `remove_duplicates_from_sorted_array.py` | Arrays, in-place updates, two pointers |
| 27 | Remove Element | `remove_element.py` | Arrays, in-place writing, two pointers |
| 33 | Search in Rotated Sorted Array | `search_in_rotated_sorted_array.py` | Binary search, rotated arrays |
| 34 | Find First and Last Position of Element in Sorted Array | `find_first_and_last_position_of_element_in_sorted_array.py` | Binary search, boundary finding |
| 35 | Search Insert Position | `search_insert_position.py` | Arrays, binary search, lower bound |
| 36 | Valid Sudoku | `valid_sudoku.py` | Matrices, hash sets, constraint validation |
| 48 | Rotate Image | `rotate_image.py` | Matrices, transpose, in-place reversal |
| 49 | Group Anagrams | `group_anagrams.py` | Hash map, sorting, grouping |
| 54 | Spiral Matrix | `spiral_matrix.py` | Matrices, boundary traversal, simulation |
| 56 | Merge Intervals | `merge_intervals.py` | Arrays, sorting, interval merging |
| 69 | Sqrt(x) | `sqrtx.py` | Math, binary search, boundary finding |
| 73 | Set Matrix Zeroes | `set_matrix_zeroes.py` | Matrices, in-place markers |
| 75 | Sort Colors | `sort_colors.py` | Arrays, two pointers, Dutch National Flag |
| 76 | Minimum Window Substring | `minimum_window_substring.py` | Strings, sliding window, frequency counting |
| 121 | Best Time to Buy and Sell Stock | `best_time_to_buy_and_sell_stock.py` | Arrays, greedy tracking, minimum value so far |
| 125 | Valid Palindrome | `valid_palindrome.py` | Strings, two pointers, character filtering |
| 128 | Longest Consecutive Sequence | `longest_consecutive_sequence.py` | Hash set, sequence starts |
| 153 | Find Minimum in Rotated Sorted Array | `find_minimum_in_rotated_sorted_array.py` | Binary search, rotated arrays |
| 167 | Two Sum II - Input Array Is Sorted | `two_sum_ii_input_array_is_sorted.py` | Sorted arrays, two pointers |
| 202 | Happy Number | `happy_number.py` | Hash set, cycle detection, math |
| 205 | Isomorphic Strings | `isomorphic_strings.py` | Strings, bidirectional hash maps |
| 217 | Contains Duplicate | `contains_duplicate.py` | Arrays, set, duplicate checking |
| 219 | Contains Duplicate II | `contains_duplicate_ii.py` | Arrays, sliding window, hash map |
| 242 | Valid Anagram | `valid_anagram.py` | Hash map, character counting |
| 278 | First Bad Version | `first_bad_version.py` | Binary search, boundary finding |
| 283 | Move Zeroes | `move_zeroes.py` | Arrays, in-place writing, zero placement |
| 290 | Word Pattern | `word_pattern.py` | Strings, bidirectional hash maps |
| 303 | Range Sum Query - Immutable | `range_sum_query_immutable.py` | Arrays, prefix sums, range queries |
| 344 | Reverse String | `reverse_string.py` | Strings, two pointers, in-place swapping |
| 347 | Top K Frequent Elements | `top_k_frequent_elements.py` | Hash map, bucket sort |
| 349 | Intersection of Two Arrays | `intersection_of_two_arrays.py` | Hash sets, unique intersection |
| 383 | Ransom Note | `ransom_note.py` | Strings, hash map, frequency counting |
| 387 | First Unique Character in a String | `first_unique_character_in_a_string.py` | Strings, hash map, frequency counting |
| 394 | Decode String | `decode_string.py` | Strings, stacks, nested decoding |
| 424 | Longest Repeating Character Replacement | `longest_repeating_character_replacement.py` | Strings, sliding window, frequency counting |
| 438 | Find All Anagrams in a String | `find_all_anagrams_in_a_string.py` | Strings, fixed-size sliding window, frequency counting |
| 567 | Permutation in String | `permutation_in_string.py` | Strings, fixed-size sliding window, frequency counting |
| 643 | Maximum Average Subarray I | `maximum_average_subarray_i.py` | Arrays, fixed-size sliding window |
| 704 | Binary Search | `binary_search.py` | Sorted arrays, binary search |
| 724 | Find Pivot Index | `find_pivot_index.py` | Arrays, prefix sums, left and right sums |
| 875 | Koko Eating Bananas | `koko_eating_bananas.py` | Binary search on answer, greedy validation |
| 1011 | Capacity To Ship Packages Within D Days | `capacity_to_ship_packages_within_d_days.py` | Binary search on answer, greedy simulation |
| 1047 | Remove All Adjacent Duplicates in String | `remove_all_adjacent_duplicates_in_string.py` | Strings, stack, adjacent cancellation |
| 1480 | Running Sum of 1d Array | `running_sum_of_1d_array.py` | Arrays, running sum, prefix sums |
| 1672 | Richest Customer Wealth | `richest_customer_wealth.py` | Matrices, row sums, maximum tracking |

## Notes

### 1. Two Sum

This solution checks every pair of numbers and returns the indexes when their sum matches the target.

Time complexity: `O(n^2)`

Space complexity: `O(1)`

### 3. Longest Substring Without Repeating Characters

This solution expands a window with a right pointer and stores the latest index of each character. When a repeated character appears inside the current window, the left pointer jumps just past its previous position.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 14. Longest Common Prefix

This solution uses the first word as a reference and checks each character position against every other word. It stops as soon as a word ends or a character does not match.

Time complexity: `O(n * m)`, where `m` is the length of the shortest checked prefix

Space complexity: `O(1)`

### 15. 3Sum

This solution sorts the array, fixes one number, and searches for the other two with inward-moving pointers. Repeated values are skipped so every returned triplet is unique.

Time complexity: `O(n^2)`

Space complexity: `O(1)` excluding the output and sorting implementation

### 20. Valid Parentheses

This solution pushes opening brackets onto a stack. Every closing bracket must match the most recent opening bracket, and the stack must be empty when the scan finishes.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 33. Search in Rotated Sorted Array

This solution determines which half of the current range is sorted. It then checks whether the target belongs in that sorted half and discards the other half.

Time complexity: `O(log n)`

Space complexity: `O(1)`

### 34. Find First and Last Position of Element in Sorted Array

This solution performs two binary searches: one continues left after finding the target, while the other continues right. Together they locate the target's complete range.

Time complexity: `O(log n)`

Space complexity: `O(1)`

### 36. Valid Sudoku

This solution uses sets to track the digits already seen in every row, column, and 3-by-3 box. A repeated digit in any of those groups makes the board invalid.

Time complexity: `O(1)` because a Sudoku board always contains 81 cells

Space complexity: `O(1)` because the tracking structures have fixed maximum sizes

### 35. Search Insert Position

This solution performs a lower-bound binary search. It returns the first index whose value is greater than or equal to the target, which is also the correct insertion position when the target is absent.

Time complexity: `O(log n)`

Space complexity: `O(1)`

### 48. Rotate Image

This solution first transposes the square matrix across its main diagonal. Reversing every row afterward completes the 90-degree clockwise rotation without creating another matrix.

Time complexity: `O(n^2)`

Space complexity: `O(1)`

### 54. Spiral Matrix

This solution tracks the top, bottom, left, and right boundaries of the unvisited area. It traverses one edge at a time and moves each boundary inward until every element has been visited.

Time complexity: `O(m * n)`

Space complexity: `O(1)` excluding the output

### 73. Set Matrix Zeroes

This solution uses the first row and first column as marker storage for the remaining matrix. Two flags preserve whether those marker row and column must also be cleared, allowing the update to happen in place.

Time complexity: `O(m * n)`

Space complexity: `O(1)`

### 69. Sqrt(x)

This solution binary-searches for the largest integer whose square is no greater than `x`. The saved candidate is the truncated square root when no exact square exists.

Time complexity: `O(log x)`

Space complexity: `O(1)`

### 49. Group Anagrams

Each word is sorted and used as a dictionary key. Words with the same sorted letters are placed in the same group.

Time complexity: `O(n * m log m)`, where `m` is the average word length

Space complexity: `O(n * m)`

### 27. Remove Element

This solution keeps a write position called `length`. Every number that is not equal to `val` is copied into the front of the array.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 121. Best Time to Buy and Sell Stock

This solution keeps track of the lowest price seen so far and the best profit possible while looping through the array.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 125. Valid Palindrome

This solution moves two pointers toward the center, skips non-alphanumeric characters, and compares the remaining characters without case sensitivity.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 128. Longest Consecutive Sequence

This solution stores every number in a set. It only starts counting when a number has no previous neighbor, which means each sequence is counted from its beginning.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 167. Two Sum II - Input Array Is Sorted

This solution uses the sorted order to adjust two pointers. A sum that is too small moves the left pointer forward, while a sum that is too large moves the right pointer backward.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 202. Happy Number

This solution repeatedly replaces the number with the sum of its squared digits. A set remembers previous results so a repeating loop can be detected.

Time complexity: `O(log n)`

Space complexity: `O(log n)`

### 205. Isomorphic Strings

This solution keeps mappings in both directions. Each character in `s` must always map to the same character in `t`, and two characters in `s` cannot map to the same character in `t`.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 217. Contains Duplicate

This solution uses a set to remember numbers already visited. If a number appears again, the function returns `True`.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 219. Contains Duplicate II

This solution stores the latest index of each number. When a number appears again, it checks whether the distance from its previous index is at most `k`.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 242. Valid Anagram

This solution counts each letter in the first string, then removes those counts while reading the second string.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 283. Move Zeroes

This solution first moves all non-zero numbers to the front while keeping their order. After that, the remaining positions are filled with zeroes.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 153. Find Minimum in Rotated Sorted Array

This solution compares the middle value with the rightmost value. When the middle value is larger, the minimum must be to its right; otherwise, the middle may be the minimum and remains in the search range.

Time complexity: `O(log n)`

Space complexity: `O(1)`

### 278. First Bad Version

This solution binary-searches the version range for the first version where `isBadVersion` returns `True`. Each check discards half of the remaining versions.

Time complexity: `O(log n)`

Space complexity: `O(1)`

### 290. Word Pattern

This solution splits the sentence into words and builds mappings in both directions. Each pattern character must match exactly one word, and each word must match exactly one pattern character.

Time complexity: `O(n)`, where `n` is the length of the sentence

Space complexity: `O(n)`

### 26. Remove Duplicates from Sorted Array

Because the array is sorted, duplicate values are next to each other. A read pointer examines every value, while a write pointer marks where the next unique value should be stored. The first `k` positions contain the unique values when the scan finishes.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 56. Merge Intervals

The intervals are sorted by their starting point. Each interval is then compared with the last merged interval: overlapping intervals extend its end, while non-overlapping intervals begin a new entry.

Time complexity: `O(n log n)`

Space complexity: `O(n)` for the result

### 75. Sort Colors

The Dutch National Flag algorithm divides the array into regions for `0`, `1`, and `2`. Three pointers place each value into its correct region in one pass without using the built-in sort function.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 76. Minimum Window Substring

This solution expands the window until it contains every required character with the correct frequency. It then moves the left pointer inward while the window remains valid to find the smallest possible answer.

Time complexity: `O(n + m)`

Space complexity: `O(n + m)`

### 303. Range Sum Query - Immutable

This solution stores the running totals in a prefix sum list. To get the sum from `left` to `right`, it subtracts the total before `left` from the total through `right`.

Setup time complexity: `O(n)`

Time complexity for each query: `O(1)`

Space complexity: `O(n)`

### 344. Reverse String

This solution uses two pointers at opposite ends of the character list. It swaps the characters in place and moves both pointers toward the center.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 347. Top K Frequent Elements

This solution first counts every number. It then groups numbers by their frequency and reads the groups from highest frequency to lowest.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 349. Intersection of Two Arrays

This solution stores the first array in a set, then checks which values from the second array are also present. Another set keeps the answer unique.

Time complexity: `O(n + m)`

Space complexity: `O(n + m)`

### 383. Ransom Note

This solution counts the characters available in the magazine. It then uses one count for every character in the ransom note and returns `False` if a required character is unavailable.

Time complexity: `O(n + m)`

Space complexity: `O(1)` because both inputs contain only lowercase English letters

### 387. First Unique Character in a String

This solution first counts how often each character appears. A second pass returns the index of the first character with a frequency of one.

Time complexity: `O(n)`

Space complexity: `O(1)` because the problem input contains only lowercase English letters

### 394. Decode String

This solution uses one stack for repeat counts and another for previously built strings. Each closing bracket completes the innermost encoded section and attaches it to its parent section.

Time complexity: `O(n + d)`, where `d` is the length of the decoded output

Space complexity: `O(n + d)`

### 424. Longest Repeating Character Replacement

This solution expands a sliding window while tracking character frequencies and the largest frequency seen inside a useful window. When more than `k` replacements would be required, the left side moves forward.

Time complexity: `O(n)`

Space complexity: `O(1)` because the input contains only uppercase English letters

### 438. Find All Anagrams in a String

This solution keeps a fixed-size window equal to the pattern length. Character frequencies are updated as the window moves, and each matching frequency array identifies an anagram's starting index.

Time complexity: `O(n)`

Space complexity: `O(1)` because the frequency arrays always contain 26 entries

### 567. Permutation in String

This solution slides a fixed-size window across `s2`. If the window's character frequencies equal the frequencies in `s1`, that window is a permutation of `s1`.

Time complexity: `O(n)`

Space complexity: `O(1)` because the frequency arrays always contain 26 entries

### 643. Maximum Average Subarray I

This solution calculates the sum of the first window of size `k`. Each following window adds the new value and removes the value that just moved out, avoiding repeated summation.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 724. Find Pivot Index

This solution keeps a left sum while moving through the array. The right sum is calculated by subtracting the left sum and current number from the total sum.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 875. Koko Eating Bananas

This solution binary-searches the possible eating speeds. For each speed, it calculates the total hours required and keeps the smallest speed that finishes all piles within `h` hours.

Time complexity: `O(n log m)`, where `m` is the largest pile

Space complexity: `O(1)`

### 1011. Capacity To Ship Packages Within D Days

This solution binary-searches capacities between the heaviest package and the total weight. A greedy simulation counts the days required for each candidate capacity and keeps the smallest feasible one.

Time complexity: `O(n log s)`, where `s` is the sum of all package weights

Space complexity: `O(1)`

### 704. Binary Search

This solution repeatedly compares the target with the middle value of the sorted array. It discards the half that cannot contain the target until the value is found or the search range becomes empty.

Time complexity: `O(log n)`

Space complexity: `O(1)`

### 1047. Remove All Adjacent Duplicates in String

This solution treats the result as a stack. A character removes the matching character on top of the stack; otherwise, it is added for future comparisons.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 1480. Running Sum of 1d Array

This solution adds each previous running total to the current number. The array itself is updated and returned.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 1672. Richest Customer Wealth

This solution calculates the sum of every customer's accounts and keeps the largest total seen.

Time complexity: `O(m * n)`

Space complexity: `O(1)`
