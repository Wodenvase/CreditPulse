#!/usr/bin/env python3
"""
CreditPulse Dashboard Entry Point
This script serves as the main entry point for the CreditPulse Streamlit dashboard.
It handles deployment scenarios and ensures proper module loading.
"""

import sys
import os
import subprocess

def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'networkx', 
        'matplotlib', 'seaborn', 'requests'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using: pip install " + " ".join(missing_packages))
        return False
    return True

def setup_path():
    """Set up the Python path for proper imports."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, 'src')
    
    if os.path.exists(src_dir):
        sys.path.insert(0, src_dir)
    else:
        # We're probably already in the src directory
        sys.path.insert(0, current_dir)

def main():
    """Main entry point for the CreditPulse dashboard."""
    print("🚀 Starting CreditPulse Dashboard...")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Setup Python path
    setup_path()
    
    # Import and run the dashboard
    try:
        from dashboard.app import main as dashboard_main
        dashboard_main()
    except ImportError as e:
        print(f"Error importing dashboard: {e}")
        print("Trying alternative import path...")
        try:
            # Try running with streamlit directly
            dashboard_path = os.path.join(os.path.dirname(__file__), 'src', 'dashboard', 'app.py')
            if os.path.exists(dashboard_path):
                subprocess.run([sys.executable, '-m', 'streamlit', 'run', dashboard_path])
            else:
                print("Dashboard app.py not found!")
                sys.exit(1)
        except Exception as e2:
            print(f"Failed to start dashboard: {e2}")
            sys.exit(1)

if __name__ == "__main__":
    main()
