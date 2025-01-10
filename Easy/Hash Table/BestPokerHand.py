def bestHand(self, ranks: List[int], suits: List[str]) -> str:
    # Initialize dictionaries to count frequencies of ranks and suits
    hashmapRanks = {}  # To store the count of each rank
    hashmapSuits = {}  # To store the count of each suit

    # Count the frequency of each rank in the ranks list
    for rank in ranks:
        hashmapRanks[rank] = 1 + hashmapRanks.get(rank, 0)

    # Count the frequency of each suit in the suits list
    for suit in suits:
        hashmapSuits[suit] = 1 + hashmapSuits.get(suit, 0)

    # If all cards have the same suit, it's a "Flush"
    if len(hashmapSuits) == 1:
        return "Flush"

    # Determine the highest frequency of any rank
    maxRank = 0
    for key, value in hashmapRanks.items():
        maxRank = max(maxRank, value)

    # If there are 3 or more cards of the same rank, it's "Three of a Kind"
    if maxRank >= 3:
        return "Three of a Kind"
    # If there are exactly 2 cards of the same rank, it's a "Pair"
    elif maxRank == 2:
        return "Pair"

    # If no other hand is possible, return "High Card"
    return "High Card"

# Time complexity: O(n)
# Space complexity: O(n) where n is the number of cards in the input lists