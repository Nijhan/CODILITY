def length_of_longest_substring(s):
    longest = 0
    current = ""

    for char in s:
        if char in current:
            index = current.index(char)
            current = current[index + 1:]
        current += char
        longest = max(longest, len(current))

    return longest

# Example usage
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3
print(length_of_longest_substring("abcabcbb"))  # Output: 3
