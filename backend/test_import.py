#!/usr/bin/env python3
"""
Simple script to test if Flask app can be imported.
Used in CI/CD to verify app structure is correct.
"""

import sys
import os

# Ensure current directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app.main import create_app
    
    # Try to create app
    app = create_app('testing')
    
    # Verify it's a Flask app
    if app is None:
        print("❌ create_app() returned None")
        sys.exit(1)
    
    if not hasattr(app, 'config'):
        print("❌ App doesn't have config attribute")
        sys.exit(1)
    
    print("✅ Flask app imports successfully")
    print(f"✅ App name: {app.name}")
    print(f"✅ Testing mode: {app.config.get('TESTING', False)}")
    sys.exit(0)
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error creating app: {e}")
    sys.exit(1)
