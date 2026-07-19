# LeetCode Solutions

Python solutions for beginner-friendly LeetCode problems.

## Problems Solved

| # | Problem | File | Concepts |
|---|---|---|---|
| 1 | Two Sum | `two_sum.py` | Arrays, nested loops, pair checking |
| 14 | Longest Common Prefix | `longest_common_prefix.py` | Strings, sorting, prefix matching |
| 15 | 3Sum | `three_sum.py` | Sorting, two pointers, duplicate handling |
| 27 | Remove Element | `remove_element.py` | Arrays, in-place writing, two pointers |
| 49 | Group Anagrams | `group_anagrams.py` | Hash map, sorting, grouping |
| 121 | Best Time to Buy and Sell Stock | `best_time_to_buy_and_sell_stock.py` | Arrays, greedy tracking, minimum value so far |
| 125 | Valid Palindrome | `valid_palindrome.py` | Strings, two pointers, character filtering |
| 128 | Longest Consecutive Sequence | `longest_consecutive_sequence.py` | Hash set, sequence starts |
| 167 | Two Sum II - Input Array Is Sorted | `two_sum_ii_input_array_is_sorted.py` | Sorted arrays, two pointers |
| 202 | Happy Number | `happy_number.py` | Hash set, cycle detection, math |
| 217 | Contains Duplicate | `contains_duplicate.py` | Arrays, set, duplicate checking |
| 242 | Valid Anagram | `valid_anagram.py` | Hash map, character counting |
| 283 | Move Zeroes | `move_zeroes.py` | Arrays, in-place writing, zero placement |
| 303 | Range Sum Query - Immutable | `range_sum_query_immutable.py` | Arrays, prefix sums, range queries |
| 347 | Top K Frequent Elements | `top_k_frequent_elements.py` | Hash map, bucket sort |
| 349 | Intersection of Two Arrays | `intersection_of_two_arrays.py` | Hash sets, unique intersection |
| 724 | Find Pivot Index | `find_pivot_index.py` | Arrays, prefix sums, left and right sums |
| 1480 | Running Sum of 1d Array | `running_sum_of_1d_array.py` | Arrays, running sum, prefix sums |

## Notes

### 1. Two Sum

This solution checks every pair of numbers and returns the indexes when their sum matches the target.

Time complexity: `O(n^2)`

Space complexity: `O(1)`

### 14. Longest Common Prefix

This solution sorts the words first. After sorting, the smallest and largest words are the only two words that need to be compared.

Time complexity: `O(n log n)`

Space complexity: `O(1)`

### 15. 3Sum

This solution sorts the array, fixes one number, and searches for the other two with inward-moving pointers. Repeated values are skipped so every returned triplet is unique.

Time complexity: `O(n^2)`

Space complexity: `O(1)` excluding the output and sorting implementation

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

### 217. Contains Duplicate

This solution uses a set to remember numbers already visited. If a number appears again, the function returns `True`.

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

### 303. Range Sum Query - Immutable

This solution stores the running totals in a prefix sum list. To get the sum from `left` to `right`, it subtracts the total before `left` from the total through `right`.

Setup time complexity: `O(n)`

Time complexity for each query: `O(1)`

Space complexity: `O(n)`

### 347. Top K Frequent Elements

This solution first counts every number. It then groups numbers by their frequency and reads the groups from highest frequency to lowest.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 349. Intersection of Two Arrays

This solution stores the first array in a set, then checks which values from the second array are also present. Another set keeps the answer unique.

Time complexity: `O(n + m)`

Space complexity: `O(n + m)`

### 724. Find Pivot Index

This solution keeps a left sum while moving through the array. The right sum is calculated by subtracting the left sum and current number from the total sum.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 1480. Running Sum of 1d Array

This solution adds each previous running total to the current number. The array itself is updated and returned.

Time complexity: `O(n)`

Space complexity: `O(1)`
