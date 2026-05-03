from typing import List

def knapsack_01_tabulation(weights: List[int], values: List[int], capacity: int) -> int:

    if len(weights) == 0 or len(values) == 0:
        return 0
        
    items = [(values[i], weights[i]) for i in range(len(weights))]
    
    store = {}
    #base case
    for cap in range(capacity + 1):
        store[(0, cap)] = 0 #not including the object
        profit, weight = items[0]
        if weight <= cap:
            store[(0, cap)] = profit

    for i in range(1, len(items)):
        
        profit, weight = items[i]

        for cap in range(capacity + 1):
            
            profit_without_exclusion = store[(i - 1, cap)]

            if weight <= cap:
                
                max_profit = max(profit_without_exclusion, profit + store[(i-1, cap - weight)])
            else:
                max_profit = profit_without_exclusion
            
            store[(i, cap)] = max_profit

    return store[(len(items) - 1, capacity)]




if __name__ == "__main__":
    print(knapsack_01_tabulation([1, 2, 3], [6, 10, 12], 5))