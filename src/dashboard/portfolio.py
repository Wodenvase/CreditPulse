import pandas as pd
from bond_analytics.portfolio import Portfolio

REQUIRED_COLUMNS = ['bond', 'sector', 'duration', 'convexity', 'var', 'expectedshortfall']

class Portfolio:
    def __init__(self, file_path):
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")

        # Normalize column names
        df.columns = [col.strip().lower() for col in df.columns]

        # Check for required columns
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(missing)}")

        self.df = df

    def aggregate_metrics(self):
        try:
            metrics = {
                'Total Duration': self.df['duration'].sum(),
                'Total Convexity': self.df['convexity'].sum(),
                'Portfolio VaR': self.df['var'].sum(),
                'Portfolio Expected Shortfall': self.df['expectedshortfall'].sum()
            }
            return metrics
        except Exception as e:
            return {"Error": f"Could not calculate aggregate metrics: {e}"}

    def sector_exposure(self):
        try:
            exposure = self.df.groupby('sector').agg({
                'bond': 'count',
                'duration': 'sum',
                'var': 'sum'
            }).rename(columns={'bond': 'Bond Count'})
            return exposure
        except Exception as e:
            return {"Error": f"Could not calculate sector exposure: {e}"}

    def concentration_risk(self):
        try:
            sector_counts = self.df['sector'].value_counts(normalize=True)
            return sector_counts
        except Exception as e:
            return {"Error": f"Could not calculate concentration risk: {e}"}