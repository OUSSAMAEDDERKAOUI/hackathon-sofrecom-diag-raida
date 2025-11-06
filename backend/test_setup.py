#!/usr/bin/env python3
"""
Test script to verify setup is correct.
Run this after installing dependencies to check everything works.
"""

import sys
import os

def test_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major == 3 and version.minor >= 10:
        print("  ✅ Python version is compatible")
        return True
    else:
        print("  ❌ Python 3.10+ required")
        return False

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        ('flask', 'Flask'),
        ('sklearn', 'scikit-learn'),
        ('pandas', 'pandas'),
        ('numpy', 'numpy'),
        ('joblib', 'joblib'),
        ('pytest', 'pytest')
    ]
    
    all_ok = True
    print("\n✓ Testing package imports:")
    
    for module_name, package_name in required_packages:
        try:
            __import__(module_name)
            print(f"  ✅ {package_name}")
        except ImportError:
            print(f"  ❌ {package_name} - NOT INSTALLED")
            all_ok = False
    
    return all_ok

def test_app_import():
    """Test if app can be imported"""
    print("\n✓ Testing Flask app import:")
    try:
        from app.main import create_app
        app = create_app('testing')
        print("  ✅ Flask app imports successfully")
        print(f"  ✅ App name: {app.name}")
        return True
    except Exception as e:
        print(f"  ❌ Failed to import app: {e}")
        return False

def test_routes():
    """Test if routes are registered"""
    print("\n✓ Testing routes:")
    try:
        from app.main import create_app
        app = create_app('testing')
        
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(str(rule))
        
        expected_routes = ['/health', '/', '/api/analysis/', '/api/evaluation/', '/api/recommendation/']
        
        all_ok = True
        for route in expected_routes:
            if any(route in r for r in routes):
                print(f"  ✅ {route}")
            else:
                print(f"  ❌ {route} - NOT FOUND")
                all_ok = False
        
        return all_ok
    except Exception as e:
        print(f"  ❌ Failed to test routes: {e}")
        return False

def test_config():
    """Test configuration"""
    print("\n✓ Testing configuration:")
    try:
        from app.config import config
        print(f"  ✅ Config loaded")
        print(f"  ✅ Environments available: {list(config.keys())}")
        return True
    except Exception as e:
        print(f"  ❌ Failed to load config: {e}")
        return False

def test_virtual_env():
    """Check if running in virtual environment"""
    print("\n✓ Testing virtual environment:")
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print(f"  ✅ Running in virtual environment")
        print(f"  ✅ Python path: {sys.prefix}")
        return True
    else:
        print(f"  ⚠️  NOT running in virtual environment")
        print(f"  ⚠️  This might cause issues. Activate venv first!")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🔍 Diag-Raida Setup Verification")
    print("=" * 60)
    
    results = []
    
    results.append(("Python Version", test_python_version()))
    results.append(("Virtual Environment", test_virtual_env()))
    results.append(("Package Imports", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("Flask App", test_app_import()))
    results.append(("Routes", test_routes()))
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 SUCCESS! Your setup is complete and working!")
        print("\nNext steps:")
        print("1. Run the app: python run.py (or ./start.sh on Linux/Mac)")
        print("2. Test API: curl http://localhost:5000/health")
        print("3. Run tests: pytest tests/")
        print("4. Read docs/quick_start_team.md for your assignment")
        return 0
    else:
        print("\n❌ SETUP INCOMPLETE - Please fix the issues above")
        print("\nCommon fixes:")
        print("1. Activate virtual environment:")
        print("   - Windows: venv\\Scripts\\activate")
        print("   - Linux/Mac: source venv/bin/activate")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Check Python version: python --version (need 3.10+)")
        return 1

if __name__ == "__main__":
    sys.exit(main())
