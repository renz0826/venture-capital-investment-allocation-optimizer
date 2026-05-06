# Venture Capital Resource Allocation: 0/1 Knapsack Problem
# Algorithms: ROI-Based Greedy Heuristic vs. Top-Down Dynamic Programming

class Startup:
    def __init__(self, id, name, capital, profit):
        self.id = id
        self.name = name
        self.capital = capital
        self.profit = profit

        # Calculates the ROI ratio for the Greedy algorithm
        self.ratio = profit / capital
