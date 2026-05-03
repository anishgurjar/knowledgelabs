from collections import defaultdict

def main(s: str, t: str) -> str:

    l = 0
    result_window_length = float("inf")

    tmap, smap = defaultdict(int), defaultdict(int) #TODO: what's a better way to write this? 
    for i in t:
        tmap[i]+=1
    required = len(tmap)
    satisfied = 0

    res_l, res_r = 0, 0

    for r in range(len(s)):

        curr_window = s[l:r+1]
        if s[r] in tmap:
            smap[s[r]] += 1

            if smap[s[r]] == tmap[s[r]]:
                satisfied += 1

        while satisfied == required:
            curr_window_length = r - l + 1

            if curr_window_length < result_window_length:
                result_window_length = curr_window_length
                res_l, res_r = l, r
            
            if s[l] in smap:
                if smap[s[l]] == tmap[s[l]]:
                    satisfied -= 1
                smap[s[l]]-=1
            l += 1

    return "" if result_window_length == float("inf") else s[res_l: res_r + 1]


if __name__ == "__main__":
    print(main("ADOBECODEBANC", "ABC"))

