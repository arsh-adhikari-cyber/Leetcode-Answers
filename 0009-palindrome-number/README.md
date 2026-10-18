# 9. Palindrome Number

## 📝 Problem Statement
Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same backward as forward. For example, `121` is a palindrome while `123` is not.

### Examples

**Example 1:**
- **Input:** `x = 121`
- **Output:** `true`

**Example 2:**
- **Input:** `x = -121`
- **Output:** `false`
- **Explanation:** From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

**Example 3:**
- **Input:** `x = 10`
- **Output:** `false`
- **Explanation:** Reads `01` from right to left. Therefore it is not a palindrome.

---

## 💡 Solution Approach
This solution uses a **mathematical approach** to reverse the integer without converting it into a string:

1. **Negative Check:** Any negative number cannot be a palindrome due to the minus sign, so we immediately return `False`.
2. **Reversing the Integer:** We store a copy of the original number. Then, we use a `while` loop to extract the last digit using modulo `x % 10` and append it to our `reversed_num` variable. We discard the last digit using floor division `x //= 10`.
3. **Comparison:** Finally, we check if the fully reversed integer matches the original saved value.

---

## 🛠️ Code Implementation

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether an integer is a palindrome without string conversion.
        """
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
            
        original_val = x
        reversed_num = 0
        
        # Mathematically reverse the integer
        while x > 0:
            last_digit = x % 10
            reversed_num = (reversed_num * 10) + last_digit
            x //= 10
            
        # Return True if the reversed number matches the original
        return reversed_num == original_val
```

---

## 📊 Complexity Analysis

- **Time Complexity:** **\(O(\log_{10} n)\)** — We divide the input number by 10 in every iteration of the loop. The total number of iterations is equal to the number of digits in the integer n.
- **Space Complexity:** **O(1)** — We only use a few integer variables (`original_val`, `reversed_num`, `last_digit`) which consume constant extra space regardless of the input size.
