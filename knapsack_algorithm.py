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

def run_dynamic_programming(startups, budget):
    """
    Optimal Solution: O(n * W) Time Complexity.
    Uses top-down recursion with memoization (caching) to find absolute maximum profit.
    """
    # The Cache: Stores tuple of (max_profit, list_of_startups)
    # Key: (current_startup_index, remaining_budget)
    memo = {}

    def dp(index, current_budget):
        # Base Case: List exhausted or budget empty
        if index < 0 or current_budget == 0:
            return 0, []
            
        # Optimization: Return cached result in O(1) time if it exists
        state_key = (index, current_budget)
        if state_key in memo:
            return memo[state_key]
            
        startup = startups[index]
        
        # Condition A: Startup exceeds current budget, skip it
        if startup.capital > current_budget:
            result = dp(index - 1, current_budget)
            
        # Condition B: Simulate both paths (Fund vs. Reject)
        else:
            # Path 1: Reject Startup
            profit_without, list_without = dp(index - 1, current_budget)
            
            # Path 2: Fund Startup
            profit_with, list_with = dp(index - 1, current_budget - startup.capital)
            profit_with += startup.profit
            
            # Keep the path with the highest profit
            if profit_with > profit_without:
                # Create a new list and append to avoid mutating shared lists
                result = (profit_with, list_with + [startup])
            else:
                result = (profit_without, list_without)
                
        # Save state to cache before returning
        memo[state_key] = result
        return result

    # Start the recursive chain from the last index
    return dp(len(startups) - 1, budget)

# ==========================================
# EXPERIMENTAL DATASET & EXECUTION
# ==========================================

if __name__ == "__main__":
    # The $10,000,000 Venture Capital Budget
    TOTAL_BUDGET = 10000000

    # The 10-Startup Dataset
    dataset = [
        Startup(1, "Quantum Encryption Solutions", 4500000, 12000000),
        Startup(2, "Cloud Kitchen Logistics", 1200000, 3100000),
        Startup(3, "Agritech Drone Surveying", 800000, 2200000),
        Startup(4, "VR Surgical Training", 2500000, 6500000),
        Startup(5, "Blockchain Supply Chain", 3000000, 8000000),
        Startup(6, "AI Customer Support Bots", 600000, 1500000),
        Startup(7, "Smart Grid Energy Analytics", 1800000, 4800000),
        Startup(8, "Telehealth Diagnostics", 2200000, 5900000),
        Startup(9, "Peer-to-Peer Micro-lending", 500000, 1200000),
        Startup(10, "Next-Gen Battery Tech", 4200000, 11500000)
    ]

    # --- Execute Greedy Heuristic ---
    print("--- 1. ROI-BASED GREEDY HEURISTIC ---")
    g_profit, g_list, g_leftover = run_greedy_heuristic(dataset, TOTAL_BUDGET)
    print(f"Total Projected Profit: ${g_profit:,}")
    print(f"Unused Capital: ${g_leftover:,}")
    print("Funded Portfolio:")
    for s in g_list:
        print(f"  - {s.id}{s.name} (Cost: ${s.capital:,})")

    print("\n" + "="*40 + "\n")

    # --- Execute Dynamic Programming ---
    print("--- 2. TOP-DOWN DYNAMIC PROGRAMMING ---")
    dp_profit, dp_list = run_dynamic_programming(dataset, TOTAL_BUDGET)
    
    # Calculate DP leftover budget manually
    dp_cost = sum(s.capital for s in dp_list)
    dp_leftover = TOTAL_BUDGET - dp_cost
    
    print(f"Total Guaranteed Profit: ${dp_profit:,}")
    print(f"Unused Capital: ${dp_leftover:,}")
    print("Optimal Funded Portfolio:")
    for s in (dp_list): 
        print(f"  -{s.id} {s.name} (Cost: ${s.capital:,})")