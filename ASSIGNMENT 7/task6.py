from typing import List

def shortestToChar(s: str, c: str) -> List[int]:
    indices = [i for i, char in enumerate(s) if char == c]  # Get indices of character 'c'

    result = []
    for i in range(len(s)):
        if s[i] == c:
            result.append(0)
        else:
            distances = [abs(i - index) for index in indices]
            result.append(min(distances))

    return result

# Test the function
output = shortestToChar(s="loveleetcode", c="e")
print(output)
