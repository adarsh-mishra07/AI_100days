def longestSubstring(S):
    l=len(S)
    char_map={}
    right=0
    left=0
    max_lenght=0

    for right in range(l):
        current_char=S[right]
        if current_char in char_map and char_map[current_char]>=left:
              left=char_map[current_char]+1
        char_map[current_char]=right

        current_window_size=right-left+1
        max_lenght=max(max_lenght,current_window_size)
    return max_lenght


S=["a","b","a","c","b","a","b","c"]
print("Longest Substring:",longestSubstring(S),S)