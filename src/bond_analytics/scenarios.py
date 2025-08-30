import pandas as pd

PREBUILT_SCENARIOS = {
    "2008 Crisis": {"spread_shock": 0.03, "rate_shock": 0.01},
    "COVID-2020": {"spread_shock": 0.02, "rate_shock": -0.005},
    "RBI Rate Hike 200bps": {"spread_shock": 0.01, "rate_shock": 0.02}
}

def apply_scenario(bond_df, scenario):
    shock = PREBUILT_SCENARIOS.get(scenario, {})
    df = bond_df.copy()
    if 'spread_shock' in shock:
        df['stressed_spread'] = df['spread'] + shock['spread_shock']
    if 'rate_shock' in shock:
        df['stressed_rate'] = df.get('rate', 0) + shock['rate_shock']
    return df