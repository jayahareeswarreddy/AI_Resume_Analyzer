#!/usr/bin/env python3
"""
Status check script for AI Resume Analyzer
"""

import sys
import importlib

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def main():
    print("🔍 Checking AI Resume Analyzer Status...")
    print("=" * 50)
    
    # Core packages
    packages = [
        "streamlit",
        "langchain", 
        "langchain_groq",
        "langchain_huggingface",
        "selenium",
        "webdriver_manager",
        "PyPDF2",
        "faiss",
        "pandas",
        "numpy"
    ]
    
    all_good = True
    
    for package in packages:
        if check_package(package):
            print(f"✅ {package}")
        else:
            print(f"❌ {package} - MISSING")
            all_good = False
    
    print("=" * 50)
    
    if all_good:
        print("🎉 All packages installed! Ready to run.")
        print("\n🚀 To start the app:")
        print("   python -m streamlit run app.py")
    else:
        print("⚠️  Some packages are missing.")
        print("\n📦 To install missing packages:")
        print("   pip install -r requirements.txt")
    
    return all_good

if __name__ == "__main__":
    main() 