# LeetCode Solutions

Python solutions for beginner-friendly LeetCode problems.

## Problems Solved

| # | Problem | File | Concepts |
|---|---|---|---|
| 1 | Two Sum | `two_sum.py` | Arrays, nested loops, pair checking |
| 14 | Longest Common Prefix | `longest_common_prefix.py` | Strings, sorting, prefix matching |
| 27 | Remove Element | `remove_element.py` | Arrays, in-place writing, two pointers |
| 49 | Group Anagrams | `group_anagrams.py` | Hash map, sorting, grouping |
| 121 | Best Time to Buy and Sell Stock | `best_time_to_buy_and_sell_stock.py` | Arrays, greedy tracking, minimum value so far |
| 217 | Contains Duplicate | `contains_duplicate.py` | Arrays, set, duplicate checking |
| 242 | Valid Anagram | `valid_anagram.py` | Hash map, character counting |
| 283 | Move Zeroes | `move_zeroes.py` | Arrays, in-place writing, zero placement |
| 303 | Range Sum Query - Immutable | `range_sum_query_immutable.py` | Arrays, prefix sums, range queries |
| 347 | Top K Frequent Elements | `top_k_frequent_elements.py` | Hash map, bucket sort |
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

### 27. Remove Element

This solution keeps a write position called `length`. Every number that is not equal to `val` is copied into the front of the array.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 49. Group Anagrams

Each word is sorted and used as a dictionary key. Words with the same sorted letters are placed in the same group.

Time complexity: `O(n * m log m)`, where `m` is the average word length

Space complexity: `O(n * m)`

### 121. Best Time to Buy and Sell Stock

This solution keeps track of the lowest price seen so far and the best profit possible while looping through the array.

Time complexity: `O(n)`

Space complexity: `O(1)`

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

### 724. Find Pivot Index

This solution keeps a left sum while moving through the array. The right sum is calculated by subtracting the left sum and current number from the total sum.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 1480. Running Sum of 1d Array

This solution adds each previous running total to the current number. The array itself is updated and returned.

Time complexity: `O(n)`

Space complexity: `O(1)`
