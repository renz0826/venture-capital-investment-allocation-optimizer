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

def run_greedy_heuristic(startups, budget):
    """
    Approximate Solution: O(n log n) Time Complexity.
    Sorts by highest ROI and fully funds until the budget is exhausted.
    """

    # Sort startups descending by ROI ratio
    sorted_startups = sorted(startups, key=lambda x: x.ratio, reverse=True)
    
    total_profit = 0
    funded_startups = []
    remaining_budget = budget
    
    # Greedily evaluate and fund
    for startup in sorted_startups:
        if startup.capital <= remaining_budget:
            remaining_budget -= startup.capital
            total_profit += startup.profit
            funded_startups.append(startup)
            
    return total_profit, funded_startups, remaining_budget
        print(f"  -{s.id} {s.name} (Cost: ${s.capital:,})")