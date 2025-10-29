#!/usr/bin/env python3
"""
Test script for FRED API integration with CreditPulse
This script tests the FRED API functionality without needing the full dashboard
"""

import sys
import os
sys.path.append('/Users/dipantabhattacharyya/Desktop/CreditPulse/src')

from bond_analytics.macro_api import MacroAPI
import pandas as pd

def test_fred_api():
    """Test FRED API with sample data"""
    
    print("=== CreditPulse FRED API Test ===\n")
    
    # Initialize MacroAPI
    macro = MacroAPI()
    
    # Test with a sample API key (you'll need to replace with a real one)
    sample_api_key = "your_fred_api_key_here"
    
    print("Testing FRED API connection...")
    print("Note: You need a real FRED API key to test this functionality")
    print("Get your free API key at: https://fred.stlouisfed.org/")
    print()
    
    # Popular series for bond analysis
    test_series = {
        "DGS10": "10-Year Treasury Constant Maturity Rate",
        "DGS2": "2-Year Treasury Constant Maturity Rate", 
        "DFF": "Federal Funds Rate",
        "BAMLH0A0HYM2": "ICE BofA US High Yield Index Option-Adjusted Spread"
    }
    
    print("Available FRED Series for Bond Analysis:")
    for series_id, description in test_series.items():
        print(f"  {series_id}: {description}")
    
    print("\nTo test with real data, replace 'your_fred_api_key_here' with your actual FRED API key")
    print("and run this script again.")
    
    # If user has provided a real API key, uncomment and test:
    """
    if sample_api_key != "your_fred_api_key_here":
        try:
            print(f"\nTesting with series: DGS10")
            data = macro.fetch_fred("DGS10", sample_api_key)
            print(f"Successfully fetched {len(data)} data points")
            print("Latest 5 observations:")
            print(data.tail())
        except Exception as e:
            print(f"Error fetching data: {e}")
    """

def test_portfolio_loading():
    """Test loading the sample portfolio"""
    
    print("\n=== Testing Portfolio Loading ===\n")
    
    portfolio_path = "/Users/dipantabhattacharyya/Desktop/CreditPulse/detailed_bond_portfolio.csv"
    
    try:
        # Load the portfolio CSV
        df = pd.read_csv(portfolio_path)
        print(f"Successfully loaded portfolio with {len(df)} bonds")
        print(f"Columns: {list(df.columns)}")
        print(f"\nSector distribution:")
        print(df['sector'].value_counts())
        print(f"\nRating distribution:")
        print(df['rating'].value_counts())
        
        # Test basic analytics
        print(f"\nPortfolio Summary:")
        print(f"  Total Face Value: ${df['face_value'].sum():,.0f}")
        print(f"  Total Market Value: ${df['market_value'].sum():,.0f}")
        print(f"  Average Duration: {df['duration'].mean():.2f}")
        print(f"  Average Yield: {df['yield'].mean():.2f}%")
        print(f"  Average Spread: {df['spread'].mean():.0f} bps")
        
    except Exception as e:
        print(f"Error loading portfolio: {e}")

if __name__ == "__main__":
    test_fred_api()
    test_portfolio_loading()
    
    print("\n=== Next Steps ===")
    print("1. Get your FRED API key from https://fred.stlouisfed.org/")
    print("2. Upload detailed_bond_portfolio.csv to the Streamlit dashboard")
    print("3. Enter your FRED API key in the dashboard's Macroeconomic section")
    print("4. Test with series like 'DGS10' for 10-Year Treasury rates")
