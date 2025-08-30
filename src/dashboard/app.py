import streamlit as st
import pandas as pd
from bond_analytics import calculate_duration, calculate_convexity
from rag_ai import retrieve_insights
from n8n_automation import fetch_bond_data
from knowledge_graph import build_relationships, visualize_knowledge_graph

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

    if bond_ticker:
        # Fetch bond data
        bond_data = fetch_bond_data(bond_ticker)

        if bond_data is not None:
            st.subheader("Bond Data")
            st.write(bond_data)

            # Calculate analytics
            duration = calculate_duration(bond_data, discount_rate)
            convexity = calculate_convexity(bond_data)

            st.subheader("Bond Analytics")
            st.write(f"**Duration:** {duration}")
            st.write(f"**Convexity:** {convexity}")

            # Predictive analytics and risk alerts
            insights = retrieve_insights(bond_data)
            st.subheader("AI Insights")
            if isinstance(insights, list):
                for insight in insights:
                    st.info(insight)
            else:
                st.info(insights)

            # Stress testing
            st.subheader("Stress Testing Results")
            stress_results = perform_stress_testing(bond_data, stress_test)
            st.write(stress_results)

            # Knowledge graph visualization
            st.subheader("Knowledge Graph Relationships")
            st.markdown("Visualizes how the bond's issuer, sector, and rating are interconnected. Useful for contagion analysis.")
            relationships = build_relationships(bond_data)
            visualize_knowledge_graph(relationships)
        else:
            st.warning("No data found for this bond ticker.")
    else:
        st.info("Please enter a bond ticker in the sidebar to begin.")

def perform_stress_testing(bond_data, stress_test):
    # Placeholder for stress testing logic
    return {"Stress Test Scenario": stress_test, "Impact": "To be calculated"}

if __name__ == "__main__":
    main()