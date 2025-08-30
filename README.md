# CreditPulse Project

CreditPulse is a comprehensive analytics platform designed for bond analytics, integrating advanced AI capabilities, automation workflows, and interactive visualizations. This project aims to provide users with tools for analyzing bond performance, generating insights, and automating data workflows.

## Features

- **Bond Analytics**: Functions and classes for calculating duration, convexity, yield curve shifts, and credit risk signals.
- **RAG AI**: An AI system that retrieves insights from a knowledge base and generates human-like explanations.
- **n8n Automation**: Automation workflows for ETL processes, including data pulling, cleaning, and notifications for threshold breaches.
- **Knowledge Graph**: Constructs and manages a knowledge graph to visualize relationships between issuers, sectors, ratings, and bonds.
- **Streamlit Dashboard**: An interactive dashboard for real-time bond spread charts, predictive analytics, risk alerts, and user interaction for stress testing and custom queries.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd CreditPulse
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit dashboard, execute the following command:
```
streamlit run src/dashboard/app.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.