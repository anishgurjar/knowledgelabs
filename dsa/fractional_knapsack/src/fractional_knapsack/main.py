from typing import List

def main(values: List[int], weights: List[int], capacity: int) -> float:

    profit = 0
    weight_in_knapsack_so_far = 0
    
    if len(values) != len(weights):
        raise ValueError("Both values and weights need to be of the same length")


    values_and_weights = []
    for i in range(len(values)):
        values_and_weights.append((values[i], weights[i]))
    
    values_and_weights = sorted(values_and_weights, key= lambda x: x[0]/x[1], reverse=True)


    for current_object_value, current_object_weight in values_and_weights: 

        if weight_in_knapsack_so_far == capacity: 
            return profit

        remaining_space_in_knapsack = capacity - weight_in_knapsack_so_far
        if current_object_weight <= remaining_space_in_knapsack:
            weight_in_knapsack_so_far += current_object_weight
            profit += current_object_value
        
        else: 
            unit_price = current_object_value / current_object_weight

            weight_in_knapsack_so_far += remaining_space_in_knapsack
            profit += unit_price * remaining_space_in_knapsack

    return profit

if __name__ == "__main__":
    print(main([100, 60, 120], [20, 10, 30], 25))