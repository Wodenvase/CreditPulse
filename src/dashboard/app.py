import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import networkx as nx
import streamlit.components.v1 as components

# Add the src directory to the Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Import modules with comprehensive error handling
import_errors = []

try:
    from pyvis.network import Network
    PYVIS_AVAILABLE = True
except ImportError as e:
    PYVIS_AVAILABLE = False
    import_errors.append(f"PyVis: {e}")

try:
    from bond_analytics import calculate_duration, calculate_convexity
    BOND_ANALYTICS_AVAILABLE = True
except ImportError as e:
    BOND_ANALYTICS_AVAILABLE = False
    import_errors.append(f"Bond Analytics: {e}")

try:
    from rag_ai import retrieve_insights
    RAG_AI_AVAILABLE = True
except ImportError as e:
    RAG_AI_AVAILABLE = False
    import_errors.append(f"RAG AI: {e}")

try:
    from n8n_automation import fetch_bond_data
    N8N_AVAILABLE = True
except ImportError as e:
    N8N_AVAILABLE = False
    import_errors.append(f"N8N Automation: {e}")

try:
    from knowledge_graph import build_relationships, visualize_knowledge_graph
    from knowledge_graph.event_correlation import EventCorrelationEngine
    KNOWLEDGE_GRAPH_AVAILABLE = True
except ImportError as e:
    KNOWLEDGE_GRAPH_AVAILABLE = False
    import_errors.append(f"Knowledge Graph: {e}")

try:
    from bond_analytics.portfolio import Portfolio
    from bond_analytics.alerts import SmartAlert
    from bond_analytics.liquidity import calculate_liquidity_metrics
    from bond_analytics.macro_api import MacroAPI
    from bond_analytics.scenarios import apply_scenario, PREBUILT_SCENARIOS
    ADVANCED_ANALYTICS_AVAILABLE = True
except ImportError as e:
    ADVANCED_ANALYTICS_AVAILABLE = False
    import_errors.append(f"Advanced Analytics: {e}")

# Display import status
if import_errors:
    with st.sidebar:
        st.warning("⚠️ Some modules could not be imported:")
        for error in import_errors:
            st.text(f"• {error}")
        st.info("Some features may be limited. Check requirements.txt and installation.")

def main():
    st.title("CreditPulse Dashboard")
    st.markdown("""
    Welcome to **CreditPulse**!  
    This dashboard provides real-time analytics, insights, and risk alerts for government and corporate bonds using advanced AI and knowledge graph technology.
    - **Bond Analytics**: Duration, convexity, and spread analysis.
    - **RAG AI**: Retrieve and summarize key events and regulatory changes.
    - **ETL & Alerts**: Automated data pipelines and breach notifications.
    - **Knowledge Graph**: Visualize relationships and contagion paths.
    """)

    # Sidebar for user inputs
    st.sidebar.header("User Inputs")
    bond_ticker = st.sidebar.text_input("Enter Bond Ticker (e.g., ACME2025 or XYZ2030):")
    stress_test = st.sidebar.slider("Stress Test Scenario", 0, 100, 50)
    discount_rate = st.sidebar.number_input("Discount Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)

    # Smart Alerts 2.0
    st.sidebar.header("Smart Alerts 2.0")
    alert_threshold = st.sidebar.slider("Alert Z-score Threshold", 1.0, 5.0, 2.5, 0.1)
    default_webhook = os.getenv("N8N_WEBHOOK_URL", "")
    n8n_webhook_url = st.sidebar.text_input("n8n Webhook URL (for alerts)", default_webhook)

    if bond_ticker:
        # Fetch bond data
        if N8N_AVAILABLE:
            bond_data = fetch_bond_data(bond_ticker)
        else:
            # Fallback: Create sample bond data
            bond_data = {
                "bond_id": bond_ticker,
                "issuer": "Sample Corp",
                "sector": "Technology",
                "rating": "A",
                "yield": 4.5,
                "spread": 85,
                "cash_flows": [5, 5, 105],
                "spread_history": [80, 82, 79, 85, 87, 84, 86, 83, 88, 85],
                "latest_spread": 85
            }
            st.info("Using sample data - n8n_automation module not available")

        if bond_data is not None:
            st.subheader("Bond Data")
            st.write(bond_data)

            # Calculate analytics
            if BOND_ANALYTICS_AVAILABLE:
                duration = calculate_duration(bond_data, discount_rate)
                convexity = calculate_convexity(bond_data)

                st.subheader("Bond Analytics")
                st.write(f"**Duration:** {duration}")
                st.write(f"**Convexity:** {convexity}")
            else:
                st.warning("Bond analytics calculations not available - bond_analytics module missing")

            # Predictive analytics and risk alerts
            if RAG_AI_AVAILABLE:
                insights = retrieve_insights(bond_data)
                st.subheader("AI Insights")
                if isinstance(insights, list):
                    for insight in insights:
                        st.info(insight)
                else:
                    st.info(insights)
            else:
                st.subheader("AI Insights")
                st.info("AI insights not available - rag_ai module missing")

            # Stress testing
            st.subheader("Stress Testing Results")
            stress_results = perform_stress_testing(bond_data, stress_test)
            st.write(stress_results)

            # Knowledge graph visualization
            st.subheader("Knowledge Graph Relationships")
            st.markdown("Visualizes how the bond's issuer, sector, and rating are interconnected. Useful for contagion analysis.")
            if KNOWLEDGE_GRAPH_AVAILABLE:
                relationships = build_relationships(bond_data)
                visualize_knowledge_graph(relationships)
            else:
                st.warning("Knowledge graph visualization not available - knowledge_graph module missing")
                st.info("Install required dependencies: pip install networkx matplotlib")

            # Smart Alerts 2.0
            if n8n_webhook_url and ADVANCED_ANALYTICS_AVAILABLE:
                # Extract spread history and latest spread robustly
                spread_history = bond_data.get('spread_history')
                latest_spread = bond_data.get('latest_spread')

                # Validate data types
                if isinstance(spread_history, (list, np.ndarray)) and len(spread_history) > 2 and isinstance(latest_spread, (int, float)):
                    alert = SmartAlert(spread_history, bond_ticker, n8n_webhook_url)
                    abnormal, z_score = alert.is_abnormal_move(latest_spread, threshold=alert_threshold)
                    if abnormal:
                        sent = alert.send_alert(f"Abnormal spread move detected for {bond_ticker}! Z-score: {z_score:.2f}")
                        if sent:
                            st.warning(f"Alert sent! Abnormal spread move detected (Z-score: {z_score:.2f})")
                        else:
                            st.error("Failed to send alert via n8n. Please check your webhook URL and network connection.")
                    else:
                        st.success(f"No abnormal spread move detected (Z-score: {z_score:.2f})")
                else:
                    st.info("Spread history or latest spread data is missing or invalid for this bond.")
            elif n8n_webhook_url and not ADVANCED_ANALYTICS_AVAILABLE:
                st.warning("Smart Alerts not available - advanced analytics modules missing")
        else:
            st.warning("No data found for this bond ticker.")
    else:
        st.info("Please enter a bond ticker in the sidebar to begin.")

    st.title("Portfolio View")

    uploaded_file = st.file_uploader("Upload your bond portfolio (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file:
        try:
            with open("temp_uploaded_file", "wb") as f:
                f.write(uploaded_file.getbuffer())
            portfolio = Portfolio("temp_uploaded_file")
            st.subheader("Aggregate Metrics")
            st.write(portfolio.aggregate_metrics())
            st.subheader("Sector Exposure")
            st.write(portfolio.sector_exposure())
            st.subheader("Concentration Risk")
            st.write(portfolio.concentration_risk())
            st.subheader("Liquidity Risk Indicators")
            liquidity_metrics = calculate_liquidity_metrics(portfolio.df)
            st.dataframe(liquidity_metrics)

            # Event Correlation Engine
            df = portfolio.df
            st.subheader("Event Correlation Engine")
            sector_event = st.selectbox("Select sector event to simulate", df['sector'].unique())
            if sector_event:
                engine = EventCorrelationEngine(df)
                affected_bonds = engine.propagate_event(sector_event)
                st.write(f"Bonds potentially affected by a shock in {sector_event} sector:")
                st.write(affected_bonds)

                # Draw networkx graph
                draw_networkx_graph(engine.graph)

            # Scenario Analysis
            st.subheader("Scenario Library")
            scenario = st.selectbox("Select Scenario", list(PREBUILT_SCENARIOS.keys()))
            if uploaded_file and scenario:
                stressed_df = apply_scenario(portfolio.df, scenario)
                st.write("Scenario Impact:")
                st.dataframe(stressed_df)
        except Exception as e:
            st.error(f"Portfolio upload failed: {e}")

    # Macroeconomic Linkages
    st.subheader("Macroeconomic Linkages")
    fred_api_key = st.text_input("FRED API Key", type="password")
    fred_series = st.text_input("FRED Series ID (e.g., DGS10 for 10Y Treasury):", "DGS10")
    if fred_api_key and fred_series:
        macro = MacroAPI()
        fred_df = macro.fetch_fred(fred_series, fred_api_key)
        st.line_chart(fred_df.set_index('date')['value'])
        # Optionally, show correlation with bond spreads if bond data is loaded

    st.subheader("Interactive Knowledge Graph")
    if uploaded_file:
        engine = EventCorrelationEngine(portfolio.df)
        net = Network(height="500px", width="100%", notebook=False)
        net.from_nx(engine.graph)
        # Color-code contagion paths
        for path in engine.contagion_paths('SomeSector', risk_level='high'):
            net.add_edge(path['from'], path['to'], color=path['color'])
        net.show("graph.html")
        with open("graph.html", "r") as f:
            html = f.read()
        components.html(html, height=550)

def perform_stress_testing(bond_data, stress_test):
    # Placeholder for stress testing logic
    return {"Stress Test Scenario": stress_test, "Impact": "To be calculated"}

def draw_networkx_graph(G):
    net = Network(notebook=False, height="500px", width="100%")
    net.from_nx(G)
    net.show("graph.html")
    with open("graph.html", "r") as f:
        html = f.read()
    components.html(html, height=550)

if __name__ == "__main__":
    main()