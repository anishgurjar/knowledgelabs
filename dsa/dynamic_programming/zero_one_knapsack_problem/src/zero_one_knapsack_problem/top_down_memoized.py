from typing import List

def knapsack_01_memoized(weights: List[int], values: List[int], capacity: int) -> int:

    items = [(values[i], weights[i]) for i in range(len(weights))]
    memo = {}

    def calculate_profit(item, capacity):

        if item < 0:
            return 0
        
        profit, weight = items[item]

        if (item+1, capacity) not in memo:
            memo[(item - 1, capacity)] = calculate_profit(item - 1, capacity)

        profit_without_inclusion = memo[(item - 1, capacity)]
        
        if weight <= capacity: 

            if (item - 1, capacity - weight) not in memo:
                memo[(item - 1, capacity - weight)] =  calculate_profit(item - 1, capacity - weight)
            
            profit_with_inclusion = profit + memo[(item - 1, capacity - weight)]

            max_profit = max(profit_with_inclusion, profit_without_inclusion)
        
        else:
            max_profit = profit_without_inclusion

        return max_profit
    
    return calculate_profit(len(items)-1, capacity)




if __name__ == "__main__":
    print(knapsack_01_memoized([1, 2, 3], [6, 10, 12], 5))