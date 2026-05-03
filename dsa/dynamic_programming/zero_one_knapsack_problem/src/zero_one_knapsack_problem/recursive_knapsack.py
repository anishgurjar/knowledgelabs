from typing import List

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:

    items = [(values[i], weights[i]) for i in range(len(weights))]

    def calculate_profit(item, capacity):

        if item < 0:
            return 0
        
        profit, weight = items[item]


        profit_without_inclusion = calculate_profit(item - 1, capacity)
        if weight <= capacity: 

            profit_with_inclusion = profit + calculate_profit(item - 1, capacity - weight)
            max_profit = max(profit_with_inclusion, profit_without_inclusion)
        
        else:
            max_profit = profit_without_inclusion

        return max_profit
    
    return calculate_profit(len(items)-1, capacity)




if __name__ == "__main__":
    print(knapsack_01([1, 2, 3], [6, 10, 12], 5))