# FRED API Key Setup Guide

## How to Get Your FRED API Key

1. **Visit the FRED Website**: Go to https://fred.stlouisfed.org/
2. **Create an Account**: Click on "My Account" and register for a free account
3. **Request API Key**: Once logged in, go to "My Account" > "API Keys"
4. **Generate Key**: Click "Request API Key" and follow the instructions
5. **Copy Your Key**: You'll receive a 32-character API key (example format: `abcd1234efgh5678ijkl9012mnop3456`)

## Popular FRED Series IDs for Bond Analysis

### Interest Rates
- **DGS10**: 10-Year Treasury Constant Maturity Rate
- **DGS2**: 2-Year Treasury Constant Maturity Rate  
- **DGS30**: 30-Year Treasury Constant Maturity Rate
- **DFF**: Federal Funds Rate
- **TB3MS**: 3-Month Treasury Bill Rate

### Credit Spreads
- **BAMLH0A0HYM2**: ICE BofA US High Yield Index Option-Adjusted Spread
- **BAMLC0A4CBBB**: ICE BofA BBB US Corporate Index Option-Adjusted Spread
- **BAMLC0A1CAAA**: ICE BofA AAA US Corporate Index Option-Adjusted Spread

### Economic Indicators
- **UNRATE**: Unemployment Rate
- **CPIAUCSL**: Consumer Price Index for All Urban Consumers
- **GDP**: Gross Domestic Product
- **PAYEMS**: All Employees, Total Nonfarm

## Sample FRED API Key for Testing
**Note**: Replace this with your actual API key from FRED
```
Sample Key: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

## How to Use in CreditPulse Dashboard

1. **Start the Dashboard**: Run the Streamlit app
2. **Navigate to Macroeconomic Section**: Scroll down to "Macroeconomic Linkages"
3. **Enter API Key**: Paste your FRED API key in the password field
4. **Select Series**: Choose a FRED Series ID (e.g., "DGS10" for 10-year Treasury)
5. **View Data**: The dashboard will fetch and display the time series chart

## Example Usage in Dashboard:
- **FRED API Key**: `your_actual_api_key_here`
- **FRED Series ID**: `DGS10` (for 10-Year Treasury Rate)
- **Result**: Interactive line chart showing 10-year Treasury rates over time

## API Rate Limits
- FRED API allows 120 requests per minute
- No daily limit for registered users
- Keep your API key secure and don't share it publicly
