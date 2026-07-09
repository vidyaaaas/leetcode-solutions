# LeetCode Solutions

Python solutions for beginner-friendly LeetCode problems.

## Problems Solved

| # | Problem | File | Concepts |
|---|---|---|---|
| 1 | Two Sum | `two_sum.py` | Arrays, nested loops, pair checking |
| 14 | Longest Common Prefix | `longest_common_prefix.py` | Strings, sorting, prefix matching |
| 27 | Remove Element | `remove_element.py` | Arrays, in-place writing, two pointers |
| 121 | Best Time to Buy and Sell Stock | `best_time_to_buy_and_sell_stock.py` | Arrays, greedy tracking, minimum value so far |
| 217 | Contains Duplicate | `contains_duplicate.py` | Arrays, set, duplicate checking |
| 283 | Move Zeroes | `move_zeroes.py` | Arrays, in-place writing, zero placement |

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

### 121. Best Time to Buy and Sell Stock

This solution keeps track of the lowest price seen so far and the best profit possible while looping through the array.

Time complexity: `O(n)`

Space complexity: `O(1)`

### 217. Contains Duplicate

This solution uses a set to remember numbers already visited. If a number appears again, the function returns `True`.

Time complexity: `O(n)`

Space complexity: `O(n)`

### 283. Move Zeroes

This solution first moves all non-zero numbers to the front while keeping their order. After that, the remaining positions are filled with zeroes.

Time complexity: `O(n)`

Space complexity: `O(1)`
