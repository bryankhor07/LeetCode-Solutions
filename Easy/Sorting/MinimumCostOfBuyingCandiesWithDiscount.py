def minimumCost(self, cost: List[int]) -> int:
    # Flags to keep track of candies counted in the "buy two, get one free" rule
    firstCandySold = False
    secondCandySold = False
    
    # Initialize the total minimum cost
    minCost = 0
    
    # Sort the cost list in ascending order
    # Sorting ensures that the cheapest candies are processed last, 
    # allowing us to take the most expensive candies into account for cost minimization
    cost.sort()

    # Traverse the sorted list in reverse order (from most expensive to cheapest)
    for i in range(len(cost) - 1, -1, -1):
        # If both flags are set (indicating two candies have been accounted for),
        # skip the third candy in the group (it's free) and reset the flags
        if firstCandySold and secondCandySold:
            firstCandySold = False
            secondCandySold = False
            continue
        
        # If the first candy in the group hasn't been processed, add its cost
        elif not firstCandySold:
            minCost += cost[i]
            firstCandySold = True  # Mark the first candy as processed
        
        # If the second candy in the group hasn't been processed, add its cost
        else:
            minCost += cost[i]
            secondCandySold = True  # Mark the second candy as processed
    
    # Return the total minimum cost after processing all candies
    return minCost

# Time Complexity: O(nlogn) due to the sorting operation
# Space Complexity: O(1) since we are using a constant amount of space