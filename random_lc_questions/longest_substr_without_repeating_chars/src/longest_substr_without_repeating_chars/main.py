def main(s: str) -> int:

    length, max_length = 0, 0
    l = 0

    curr_set = set()

    for r in range(len(s)):

        while s[r] in curr_set:
            curr_set.remove(s[l])
            l+=1
            length -= 1

        curr_set.add(s[r])
        length+=1

        max_length = max(max_length, length)
        
    return max_length

if __name__ == "__main__":
    main()