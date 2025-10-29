import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import networkx as nx
import streamlit.components.v1 as components

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import modules with error handling
import_errors = []

try:
    from pyvis.network import Network
    PYVIS_AVAILABLE = True
except ImportError as e:
    PYVIS_AVAILABLE = False
    import_errors.append(f"PyVis: {str(e)}")

try:
    from bond_analytics import calculate_duration, calculate_convexity
    BOND_ANALYTICS_AVAILABLE = True
except ImportError as e:
    BOND_ANALYTICS_AVAILABLE = False
    import_errors.append(f"Bond Analytics: {str(e)}")

try:
    from rag_ai import retrieve_insights
    RAG_AI_AVAILABLE = True
except ImportError as e:
    RAG_AI_AVAILABLE = False
    import_errors.append(f"RAG AI: {str(e)}")

try:
    from n8n_automation import fetch_bond_data
    N8N_AVAILABLE = True
except ImportError as e:
    N8N_AVAILABLE = False
    import_errors.append(f"N8N Automation: {str(e)}")

try:
    from knowledge_graph import build_relationships, visualize_knowledge_graph
    KNOWLEDGE_GRAPH_AVAILABLE = True
except ImportError as e:
    KNOWLEDGE_GRAPH_AVAILABLE = False
    import_errors.append(f"Knowledge Graph: {str(e)}")

try:
    from bond_analytics.portfolio import Portfolio
    PORTFOLIO_AVAILABLE = True
except ImportError as e:
    PORTFOLIO_AVAILABLE = False
    import_errors.append(f"Portfolio: {str(e)}")

try:
    from bond_analytics.alerts import SmartAlert
    ALERTS_AVAILABLE = True
except ImportError as e:
    ALERTS_AVAILABLE = False
    import_errors.append(f"Smart Alerts: {str(e)}")

try:
    from knowledge_graph.event_correlation import EventCorrelationEngine
    EVENT_CORRELATION_AVAILABLE = True
except ImportError as e:
    EVENT_CORRELATION_AVAILABLE = False
    import_errors.append(f"Event Correlation: {str(e)}")

try:
    from bond_analytics.liquidity import calculate_liquidity_metrics
    LIQUIDITY_AVAILABLE = True
except ImportError as e:
    LIQUIDITY_AVAILABLE = False
    import_errors.append(f"Liquidity: {str(e)}")

try:
    from bond_analytics.macro_api import MacroAPI
    MACRO_API_AVAILABLE = True
except ImportError as e:
    MACRO_API_AVAILABLE = False
    import_errors.append(f"Macro API: {str(e)}")

try:
    from bond_analytics.scenarios import apply_scenario, PREBUILT_SCENARIOS
    SCENARIOS_AVAILABLE = True
except ImportError as e:
    SCENARIOS_AVAILABLE = False
    import_errors.append(f"Scenarios: {str(e)}")

def main():
    st.set_page_config(
        page_title="CreditPulse - Bond Analytics Platform",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("📊 CreditPulse Dashboard")
    
    # Show import errors if any (for debugging)
    if import_errors:
        with st.expander("⚠️ Module Import Status", expanded=False):
            st.warning("Some modules couldn't be imported. The app will work with limited functionality.")
            for error in import_errors:
                st.text(f"❌ {error}")
    
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
        if N8N_AVAILABLE:
            # Fetch bond data
            bond_data = fetch_bond_data(bond_ticker)

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
                    st.warning("Bond analytics module not available")

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
                    st.warning("RAG AI module not available")

                # Stress testing
                st.subheader("Stress Testing Results")
                stress_results = perform_stress_testing(bond_data, stress_test)
                st.write(stress_results)

                # Knowledge graph visualization
                if KNOWLEDGE_GRAPH_AVAILABLE:
                    st.subheader("Knowledge Graph Relationships")
                    st.markdown("Visualizes how the bond's issuer, sector, and rating are interconnected. Useful for contagion analysis.")
                    relationships = build_relationships(bond_data)
                    visualize_knowledge_graph(relationships)
                else:
                    st.warning("Knowledge graph module not available")

                # Smart Alerts 2.0
                if ALERTS_AVAILABLE and n8n_webhook_url:
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
            else:
                st.warning("No data found for this bond ticker.")
        else:
            st.error("N8N automation module not available. Cannot fetch bond data.")
    else:
        st.info("Please enter a bond ticker in the sidebar to begin.")

    # Portfolio View
    st.title("Portfolio View")

    uploaded_file = st.file_uploader("Upload your bond portfolio (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file and PORTFOLIO_AVAILABLE:
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
            
            if LIQUIDITY_AVAILABLE:
                st.subheader("Liquidity Risk Indicators")
                liquidity_metrics = calculate_liquidity_metrics(portfolio.df)
                st.dataframe(liquidity_metrics)

            # Event Correlation Engine
            if EVENT_CORRELATION_AVAILABLE:
                df = portfolio.df
                st.subheader("Event Correlation Engine")
                sector_event = st.selectbox("Select sector event to simulate", df['sector'].unique())
                if sector_event:
                    engine = EventCorrelationEngine(df)
                    affected_bonds = engine.propagate_event(sector_event)
                    st.write(f"Bonds potentially affected by a shock in {sector_event} sector:")
                    st.write(affected_bonds)

                    # Draw networkx graph
                    if PYVIS_AVAILABLE:
                        draw_networkx_graph(engine.graph)

            # Scenario Analysis
            if SCENARIOS_AVAILABLE:
                st.subheader("Scenario Library")
                scenario = st.selectbox("Select Scenario", list(PREBUILT_SCENARIOS.keys()))
                if uploaded_file and scenario:
                    stressed_df = apply_scenario(portfolio.df, scenario)
                    st.write("Scenario Impact:")
                    st.dataframe(stressed_df)
        except Exception as e:
            st.error(f"Portfolio upload failed: {e}")
    elif uploaded_file and not PORTFOLIO_AVAILABLE:
        st.error("Portfolio module not available")

    # Macroeconomic Linkages
    st.subheader("Macroeconomic Linkages")
    fred_api_key = st.text_input("FRED API Key", type="password")
    fred_series = st.text_input("FRED Series ID (e.g., DGS10 for 10Y Treasury):", "DGS10")
    if fred_api_key and fred_series and MACRO_API_AVAILABLE:
        macro = MacroAPI()
        try:
            fred_df = macro.fetch_fred(fred_series, fred_api_key)
            st.line_chart(fred_df.set_index('date')['value'])
        except Exception as e:
            st.error(f"Error fetching FRED data: {e}")
    elif fred_api_key and fred_series and not MACRO_API_AVAILABLE:
        st.error("Macro API module not available")

    # Interactive Knowledge Graph
    if uploaded_file and EVENT_CORRELATION_AVAILABLE and PYVIS_AVAILABLE:
        st.subheader("Interactive Knowledge Graph")
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
    if PYVIS_AVAILABLE:
        net = Network(notebook=False, height="500px", width="100%")
        net.from_nx(G)
        net.show("graph.html")
        with open("graph.html", "r") as f:
            html = f.read()
        components.html(html, height=550)
    else:
        st.warning("PyVis not available for network visualization")

if __name__ == "__main__":
    main()
