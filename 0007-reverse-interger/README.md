# 7. Reverse Integer
## 📝 Problem Statement
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

### Examples

**Example 1:**
- **Input:** `x = 123`
- **Output:** `321`

**Example 2:**
- **Input:** `x = -123`
- **Output:** `-321`

**Example 3:**
- **Input:** `x = 120`
- **Output:** `21`

---

## 💡 Solution Approach
This solution leverages Python's powerful string slicing mechanism to reverse the integer efficiently:

1. **Sign Extraction:** We record whether the input number is negative or positive using a `sign` variable.
2. **String Reversal:** We take the absolute value of the integer, convert it to a string, and reverse it using the slice step syntax `[::-1]`.
3. **Reconstruct & Bound Check:** We convert the reversed string back into an integer, reapply its original sign, and verify that the final value falls within the strict 32-bit signed integer limits `[-2^31, 2^31 - 1]`. If it overflows, we safely return `0`.

---

## 🛠️ Code Implementation

```python
class Solution:
    def reverse(self, n: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer.
        Returns 0 if the reversed integer overflows the 32-bit range.
        """
        # Define 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        # Determine the sign of the integer
        sign = -1 if n < 0 else 1
        
        # Reverse the digits using string manipulation
        reversed_val = int(str(abs(n))[::-1]) * sign
        
        # Return the reversed value if within bounds, otherwise return 0
        return reversed_val if MIN_INT <= reversed_val <= MAX_INT else 0
```

---

## 📊 Complexity Analysis

- **Time Complexity:** **$O(\log_{10} n)$** — The number of digits in an integer $n$ is roughly $\log_{10} n$. Converting the integer to a string and reversing it scales linearly with the total digit count.
- **Space Complexity:** **$O(\log_{10} n)$** — Additional space is allocated to temporarily hold the string representation of the integer during conversion and slice operations.
