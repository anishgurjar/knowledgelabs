from typing import List

def main(height: List[int]) -> int:

    left_max, right_max = [0], [0]
    n = len(height)

    left_max_height = 0
    for i in range(1, n):
        left_max_height = max(left_max_height, height[i-1])
        left_max.append(left_max_height)
    
    right_max_height = 0
    for i in range(n-2,-1,-1):
        right_max_height = max(right_max_height, height[i+1])
        right_max.append(right_max_height)
    
    right_max.reverse()
    rainwater_content = 0
    for i in range(len(height)):

        rainwater = min(left_max[i], right_max[i]) - height[i]
        rainwater = rainwater if rainwater > 0 else 0
        rainwater_content += rainwater
    
    return rainwater_content



if __name__ == "__main__":
    print(main([0,1,0,2,1,0,1,3,2,1,2,1]))