#!/usr/bin/env python3
"""
RSS Article Labeling App
Run this script to start the web interface for labeling articles.
"""

import os
import sys
from app import app

def main():
    print("🎯 RSS Article Labeling App")
    print("=" * 40)
    
    # Check if data directory exists and has articles
    data_dir = 'data'
    if not os.path.exists(data_dir):
        print("❌ Data directory not found!")
        print("Please run the data collection notebook first.")
        sys.exit(1)
    
    # Check for article files
    import glob
    json_files = glob.glob(os.path.join(data_dir, 'rss_articles_*.json'))
    if not json_files:
        print("❌ No article files found!")
        print("Please run the data collection notebook first.")
        sys.exit(1)
    
    latest_file = max(json_files, key=os.path.getctime)
    print(f"✅ Found articles: {latest_file}")
    
    print("\n🚀 Starting labeling interface...")
    print("📍 Open your browser and go to: http://localhost:5001")
    print("⌨️  Use keyboard shortcuts: 1=Advertisement, 2=News, S=Skip")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        print("\n👋 Labeling session ended. Your progress has been saved!")

if __name__ == '__main__':
    main()
