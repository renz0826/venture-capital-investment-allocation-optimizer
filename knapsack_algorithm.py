import time
import tracemalloc

class Startup:
    def __init__(self, id, name, capital, profit):
        self.id = id
        self.name = name
        self.capital = capital
        self.profit = profit
        self.ratio = profit / capital

def run_greedy_heuristic(startups, budget):
    """ O(n log n) Time | O(n) Space """
    sorted_startups = sorted(startups, key=lambda x: x.ratio, reverse=True)
    
    total_cost = 0
    total_profit = 0
    funded_startups = []
    remaining_budget = budget
    
    for startup in sorted_startups:
        if startup.capital <= remaining_budget:
            remaining_budget -= startup.capital
            total_cost += startup.capital
            total_profit += startup.profit
            funded_startups.append(startup)
            
    return total_cost, total_profit, funded_startups, remaining_budget

def run_dynamic_programming(startups, budget):
    """ O(n * W) Time | O(n * W) Space """
    memo = {}

    def dp(index, current_budget):
        if index < 0 or current_budget == 0:
            return 0, []
            
        state_key = (index, current_budget)
        if state_key in memo:
            return memo[state_key]
            
        startup = startups[index]
        
        if startup.capital > current_budget:
            result = dp(index - 1, current_budget)
        else:
            profit_without, list_without = dp(index - 1, current_budget)
            profit_with, list_with = dp(index - 1, current_budget - startup.capital)
            profit_with += startup.profit
            
            if profit_with > profit_without:
                result = (profit_with, list_with + [startup])
            else:
                result = (profit_without, list_without)
                
        memo[state_key] = result
        return result

    return dp(len(startups) - 1, budget)

# ==========================================
# EXPERIMENTAL DATASET & EXECUTION
# ==========================================

if __name__ == "__main__":
    TOTAL_BUDGET = 10000000

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

    # ----------------------------------------------------
    # 1. EXECUTE GREEDY HEURISTIC
    # ----------------------------------------------------
    print("\n" + "="*50)
    print("--- 1. ROI-BASED GREEDY HEURISTIC ---")
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    g_cost, g_profit, g_list, g_leftover = run_greedy_heuristic(dataset, TOTAL_BUDGET)
    
    end_time = time.perf_counter()
    _, g_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Total Projected Profit: ${g_profit:,}")
    print(f"Unused Capital: ${g_leftover:,}")
    
    print("\n[ HARDWARE PERFORMANCE ]")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print(f"Peak RAM (Space Used): {g_peak / 1024**2:.6f} MB")


    # ----------------------------------------------------
    # 2. EXECUTE DYNAMIC PROGRAMMING
    # ----------------------------------------------------
    print("\n" + "="*50)
    print("--- 2. TOP-DOWN DYNAMIC PROGRAMMING ---")
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    dp_profit, dp_list = run_dynamic_programming(dataset, TOTAL_BUDGET)
    
    end_time = time.perf_counter()
    _, dp_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    dp_cost = sum(s.capital for s in dp_list)
    dp_leftover = TOTAL_BUDGET - dp_cost

    print(f"Total Guaranteed Profit: ${dp_profit:,}")
    print(f"Unused Capital: ${dp_leftover:,}")

    print("\n[ HARDWARE PERFORMANCE ]")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print(f"Peak RAM (Space Used): {dp_peak / 1024**2:.6f} MB")
    print("="*50 + "\n")