"""Main entry point for the NYT Connections Tracker application."""
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from nyt_connections_tracker.app import app

if __name__ == '__main__':
    app.run(debug=False, port=int(__import__('os').environ.get('PORT', 5000)))
