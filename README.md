# 🚀 CreditPulse - Advanced Bond Analytics Platform

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

*A comprehensive, AI-powered analytics platform for institutional bond portfolio management, risk assessment, and market intelligence.*

</div>

## 🎯 What is CreditPulse?

CreditPulse is a sophisticated financial technology platform that transforms how institutional investors, portfolio managers, and risk analysts approach bond market analytics. By combining traditional fixed-income mathematics with cutting-edge AI and machine learning, CreditPulse provides real-time insights, predictive analytics, and automated risk management for bond portfolios of any size.

### 🏛️ Built for Financial Professionals
- **Portfolio Managers**: Comprehensive portfolio analytics, sector exposure analysis, and concentration risk assessment
- **Risk Analysts**: Advanced VaR calculations, stress testing, and scenario analysis with regulatory-grade metrics
- **Traders**: Real-time spread monitoring, liquidity analysis, and smart alert systems for market opportunities
- **Research Teams**: AI-powered market intelligence, event correlation analysis, and macroeconomic linkages

## ✨ Core Features

### 📊 **Advanced Bond Analytics Engine**
- **Duration & Convexity**: Precise Macaulay and modified duration calculations with convexity adjustments
- **Yield Curve Analysis**: Multi-curve modeling with parallel shifts and twist scenarios
- **Credit Risk Metrics**: Probability of default modeling, credit spread analysis, and rating transition matrices
- **Liquidity Assessment**: Bid-ask spread analysis, trading volume metrics, and market impact estimation

### 🤖 **RAG-Powered AI Intelligence**
- **Market Event Analysis**: AI-driven insights from regulatory filings, earnings calls, and market news
- **Natural Language Queries**: Ask complex questions about your portfolio in plain English
- **Predictive Analytics**: Machine learning models for spread prediction and default probability estimation
- **Automated Report Generation**: AI-generated executive summaries and risk reports

### 🔔 **Smart Alerts 2.0**
- **Statistical Anomaly Detection**: Z-score based alerts for abnormal spread movements
- **Multi-Channel Notifications**: Integration with n8n, Slack, Teams, and email systems
- **Customizable Thresholds**: User-defined risk parameters and escalation procedures
- **Real-Time Monitoring**: Continuous surveillance of portfolio positions and market conditions

### 🕸️ **Knowledge Graph & Event Correlation**
- **Issuer Relationship Mapping**: Visualize complex corporate structures and sector interconnections
- **Contagion Path Analysis**: Identify potential spillover effects during market stress
- **Event Impact Modeling**: Simulate sector shocks and cross-asset correlations
- **Interactive Network Visualization**: PyVis-powered interactive graphs with drill-down capabilities

### 📈 **Comprehensive Portfolio Management**
- **Multi-Format Support**: CSV, Excel, and database connectivity for portfolio uploads
- **Sector Exposure Analysis**: Detailed breakdown by industry, geography, and rating
- **Concentration Risk Metrics**: Herfindahl indices and diversification ratios
- **Performance Attribution**: Return decomposition and benchmark analysis

### 🌍 **Macroeconomic Integration**
- **FRED API Integration**: Real-time access to 800,000+ economic time series
- **Yield Curve Dynamics**: Treasury curve analysis and corporate spread relationships
- **Economic Indicator Correlation**: Link portfolio performance to macro variables
- **Central Bank Policy Impact**: Model effects of monetary policy changes

### 🎭 **Scenario Analysis & Stress Testing**
- **Historical Scenarios**: 2008 Financial Crisis, COVID-2020, Interest Rate Cycles
- **Custom Stress Tests**: User-defined shock parameters and correlation assumptions
- **Regulatory Scenarios**: CCAR, ICAAP, and Basel III compliant stress testing
- **Monte Carlo Simulation**: Probabilistic scenario generation with confidence intervals

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.12+**: Modern Python with advanced type hints and performance optimizations
- **Streamlit 1.50+**: Interactive web application framework for financial dashboards
- **Pandas 2.3+**: High-performance data manipulation and analysis
- **NumPy 2.3+**: Numerical computing for mathematical calculations
- **NetworkX 3.5+**: Graph theory and network analysis for knowledge graphs
- **PyVis 0.3+**: Interactive network visualization with D3.js backend

### Financial Libraries
- **Scikit-learn**: Machine learning for predictive analytics and clustering
- **SciPy**: Advanced statistical functions and optimization algorithms
- **OpenAI API**: Large language model integration for natural language processing

### Visualization & UI
- **Matplotlib**: Statistical plotting and chart generation
- **Seaborn**: Advanced statistical data visualization
- **Plotly**: Interactive charts and financial time series
- **Streamlit Components**: Custom HTML/JavaScript integration

### Integration & APIs
- **FRED API**: Federal Reserve Economic Data access
- **n8n**: Workflow automation and webhook management
- **Requests**: HTTP API integration and data fetching

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- Virtual environment (recommended)
- FRED API key (free registration at [fred.stlouisfed.org](https://fred.stlouisfed.org/))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Wodenvase/CreditPulse.git
   cd CreditPulse
   ```

2. **Set up Python virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python test_fred_integration.py
   ```

### Launch Dashboard

**Option 1: From src directory (Recommended)**
```bash
cd src
PYTHONPATH=. streamlit run dashboard/app.py
```

**Option 2: Direct launch**
```bash
streamlit run src/dashboard/app.py --server.port 8501
```

**Option 3: Background mode**
```bash
nohup streamlit run src/dashboard/app.py --server.headless=true &
```

The dashboard will be available at: `http://localhost:8501`

## 📊 Sample Data & Testing

### Included Sample Portfolios
- **`detailed_bond_portfolio.csv`**: 31 bonds, $34.5M portfolio across 8 sectors
- **`comprehensive_bond_portfolio.csv`**: Alternative portfolio structure
- **Sample issuers**: Apple, Microsoft, JPMorgan, Johnson & Johnson, Tesla, and more

### Portfolio Structure
```csv
bond,sector,duration,convexity,var,expectedshortfall,issuer,rating,yield,spread,
maturity_date,face_value,market_value,coupon_rate,issue_date,bid_ask_spread,trading_volume
```

### Test with Sample Data
1. **Upload Portfolio**: Use the file uploader in the dashboard
2. **Enter Bond Ticker**: Try "AAPL2025", "JPM2028", or "TSLA2026"
3. **FRED Integration**: Enter your API key and test with "DGS10" (10-Year Treasury)
4. **Scenario Testing**: Run "2008 Crisis" or "COVID-2020" scenarios

## 📈 Use Cases & Applications

### 🏦 **Institutional Asset Management**
- **Multi-billion dollar portfolios**: Scalable analytics for large institutional mandates
- **ESG Integration**: Environmental, Social, and Governance scoring and screening
- **Benchmark Analysis**: Track performance vs. Bloomberg Barclays and ICE BofA indices
- **Client Reporting**: Automated monthly and quarterly performance reports

### 🎯 **Risk Management**
- **Regulatory Compliance**: BASEL III, Solvency II, and IFRS 17 reporting
- **Stress Testing**: CCAR and ICAAP compliant scenario analysis  
- **Credit Risk Modeling**: PD, LGD, and EAD calculations with regulatory parameters
- **Market Risk**: VaR, Expected Shortfall, and sensitivity analysis

### 💼 **Trading & Research**
- **Relative Value Analysis**: Cross-sector and cross-currency bond comparison
- **New Issue Analysis**: Primary market pricing and allocation decisions
- **Credit Research**: Fundamental analysis with AI-powered insights
- **Market Making**: Liquidity provision and inventory management

### 🔍 **Due Diligence & Investment**
- **Credit Analysis**: Deep-dive issuer analysis with financial statement integration
- **Sector Rotation**: Identify attractive sectors and timing strategies
- **Yield Curve Positioning**: Duration and curve risk management
- **Event-Driven Investing**: M&A, spinoffs, and restructuring opportunities

## 🎛️ Dashboard Features

### Main Dashboard Sections

1. **🎯 Bond Analytics Hub**
   - Individual bond analysis with real-time calculations
   - Duration, convexity, and yield-to-maturity metrics
   - Credit spread analysis and historical comparisons

2. **📋 Portfolio Management**
   - Drag-and-drop CSV/Excel upload functionality
   - Aggregate portfolio metrics and sector analysis
   - Concentration risk and diversification analytics

3. **🧠 AI Intelligence Center**
   - Natural language query interface
   - Market event correlation and impact analysis
   - Automated insights and recommendation engine

4. **⚠️ Smart Alerts Dashboard**
   - Real-time anomaly detection with Z-score analysis
   - Customizable alert thresholds and notification channels
   - Historical alert tracking and performance metrics

5. **🕸️ Knowledge Graph Explorer**
   - Interactive network visualization of issuer relationships
   - Contagion path analysis and sector interconnections
   - Event correlation mapping with risk propagation

6. **📊 Macroeconomic Integration**
   - FRED API integration with 800,000+ economic series
   - Yield curve analysis and central bank policy tracking
   - Correlation analysis between macro variables and spreads

7. **🎭 Scenario Analysis Lab**
   - Historical crisis scenarios (2008, COVID-19, etc.)
   - Custom stress testing with user-defined parameters
   - Monte Carlo simulation and probabilistic analysis

## 🔧 Advanced Configuration

### Environment Variables
```bash
# Optional: Set default FRED API key
export FRED_API_KEY="your_api_key_here"

# Optional: Set n8n webhook URL for alerts
export N8N_WEBHOOK_URL="https://your-n8n-instance.com/webhook/alerts"

# Optional: Set OpenAI API key for enhanced AI features
export OPENAI_API_KEY="your_openai_key_here"
```

### Custom Configuration
Create a `config.yaml` file in the project root:
```yaml
dashboard:
  port: 8501
  theme: "light"
  
alerts:
  default_threshold: 2.5
  notification_channels: ["email", "slack"]
  
fred:
  cache_duration: 3600  # Cache FRED data for 1 hour
  
ai:
  model: "gpt-4"
  max_tokens: 1000
```

## 📚 API Reference

### Core Functions

#### Bond Analytics
```python
from bond_analytics import calculate_duration, calculate_convexity

# Calculate duration
duration = calculate_duration(bond_data, discount_rate=0.05)

# Calculate convexity
convexity = calculate_convexity(bond_data)
```

#### Portfolio Management
```python
from bond_analytics.portfolio import Portfolio

# Load portfolio
portfolio = Portfolio("path/to/portfolio.csv")

# Get aggregate metrics
metrics = portfolio.aggregate_metrics()
exposure = portfolio.sector_exposure()
```

#### Smart Alerts
```python
from bond_analytics.alerts import SmartAlert

# Set up alert system
alert = SmartAlert(spread_history, "BOND_ID", webhook_url)
is_abnormal, z_score = alert.is_abnormal_move(latest_spread)
```

