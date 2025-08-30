import requests
import pandas as pd

class MacroAPI:
    def fetch_fred(self, series_id, api_key):
        url = f"https://api.stlouisfed.org/fred/series/observations"
        params = {"series_id": series_id, "api_key": api_key, "file_type": "json"}
        r = requests.get(url, params=params)
        data = r.json()
        df = pd.DataFrame(data['observations'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        return df[['date', 'value']]

    # Add similar methods for World Bank, IMF as needed

    def link_macro_to_bonds(self, macro_df, bond_df, macro_col='value', bond_col='spread'):
        # Example: correlate macro variable with bond spreads
        merged = bond_df.copy()
        merged[macro_col] = macro_df[macro_col].iloc[-1]  # Use latest macro value
        return merged