import numpy as np

def calculate_liquidity_metrics(df):
    # Simulate or use real bid-ask and volume data
    if 'bid_ask_spread' not in df.columns:
        df['bid_ask_spread'] = np.random.uniform(0.1, 2.0, size=len(df))
    if 'trading_volume' not in df.columns:
        df['trading_volume'] = np.random.randint(1000, 100000, size=len(df))
    liquidity_metrics = df[['bond', 'bid_ask_spread', 'trading_volume']]
    return liquidity_metrics