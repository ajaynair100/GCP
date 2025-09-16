#!/usr/bin/env python3
"""
Hello World Python Application for GCP
A simple Python script demonstrating basic functionality.
"""

import sys
import datetime
import os

def greet(name="World"):
    """
    Generate a greeting message
    
    Args:
        name (str): Name to greet
    
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"

def get_system_info():
    """
    Get basic system information
    
    Returns:
        dict: System information
    """
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "current_time": datetime.datetime.now().isoformat(),
        "environment": os.environ.get("ENVIRONMENT", "development")
    }

def main():
    """
    Main function
    """
    print("=" * 50)
    print("  GCP Hello World Python Application")
    print("=" * 50)
    
    # Basic greeting
    print(greet())
    print(greet("GCP Developer"))
    
    print("\n" + "-" * 30)
    print("System Information:")
    print("-" * 30)
    
    info = get_system_info()
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 50)
    print("Application completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
