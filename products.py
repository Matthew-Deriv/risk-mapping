import math

def calculate_stake_for_target(target=6000, max_tick_durations=None, max_aggregate_stakes=None):
    """
    Calculate the stake needed to reach a target amount for different growth rates.
    
    Args:
        target: Target amount to reach (default: 6000)
        max_tick_durations: Dict mapping growth rates to max tick durations
        max_aggregate_stakes: Dict mapping growth rates to max aggregate open stakes
    
    Returns:
        Dict with results for each growth rate
    """
    if max_tick_durations is None:
        max_tick_durations = {
            "growth_rate_0.01": 250,
            "growth_rate_0.02": 125,
            "growth_rate_0.03": 85,
            "growth_rate_0.04": 65,
            "growth_rate_0.05": 50
        }
    
    if max_aggregate_stakes is None:
        max_aggregate_stakes = {
            "growth_rate_0.01": 5000,
            "growth_rate_0.02": 5000,
            "growth_rate_0.03": 5000,
            "growth_rate_0.04": 5000,
            "growth_rate_0.05": 5000
        }
    
    results = {}
    
    for rate_key in max_tick_durations.keys():
        # Extract growth rate from key (e.g., "growth_rate_0.01" -> 0.01)
        growth_rate = float(rate_key.split('_')[-1])
        max_duration = max_tick_durations[rate_key]
        max_stake = max_aggregate_stakes[rate_key]
        
        # Calculate initial stake needed to reach target
        initial_stake = target / ((1 + growth_rate) ** max_duration)
        # Round down to 2 decimal places
        initial_stake_rounded = math.floor(initial_stake * 100) / 100
        
        # Calculate number of positions possible
        num_positions = int(max_stake / initial_stake_rounded)
        
        # Calculate remainder
        remainder = max_stake - (num_positions * initial_stake_rounded)
        
        # Calculate total payout
        position_payout = initial_stake_rounded * ((1 + growth_rate) ** max_duration)
        remainder_payout = remainder * ((1 + growth_rate) ** max_duration)
        total_payout = (num_positions * position_payout) + remainder_payout
        
        results[rate_key] = {
            "growth_rate": growth_rate,
            "max_duration": max_duration,
            "initial_stake": initial_stake_rounded,
            "num_positions": num_positions,
            "remainder": remainder,
            "position_payout": position_payout,
            "remainder_payout": remainder_payout,
            "total_payout": total_payout
        }
    
    return results

# Example usage
if __name__ == "__main__":
    max_tick_durations = {
        "growth_rate_0.01": 250,
        "growth_rate_0.02": 125,
        "growth_rate_0.03": 85,
        "growth_rate_0.04": 65,
        "growth_rate_0.05": 50
    }
    
    max_aggregate_stakes = {
        "growth_rate_0.01": 5000,
        "growth_rate_0.02": 5000,
        "growth_rate_0.03": 5000,
        "growth_rate_0.04": 5000,
        "growth_rate_0.05": 5000
    }
    
    results = calculate_stake_for_target(6000, max_tick_durations, max_aggregate_stakes)
    
    # Calculate total payout for one symbol (sum of all growth rates)
    one_symbol_total_payout = 0
    
    for rate, data in results.items():
        print(f"\n{rate}:")
        print(f"  Initial stake: {data['initial_stake']:.2f}")
        print(f"  Number of positions: {data['num_positions']}")
        print(f"  Remainder: {data['remainder']:.2f}")
        print(f"  Total payout: {data['total_payout']:.2f}")
        one_symbol_total_payout += data['total_payout']
    
    print(f"\nTotal payout for 1 symbol: {one_symbol_total_payout:.2f}")
    print(f"Total payout for 10 symbols: {(one_symbol_total_payout * 10):.2f}")
