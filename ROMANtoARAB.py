class Solution:
  def romanToInt(self, s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = 0
    i = 0
    while i < len(s):
      if s[i] in roman:
        count += roman[s[i]]
      if ((i > 0) & (roman[s[i]] > roman[s[i - 1]])):
        count -= 2 * roman[s[i - 1]]
      i += 1
    return count

print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("MMMCMXCIX"))

