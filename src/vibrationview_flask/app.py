from flask import Flask
from routes import register_routes

def get_vv_instance():
    """Get VibrationVIEW instance - thread-safe internally"""
    try:
        from vibrationviewapi import VibrationVIEW
        vv_instance = VibrationVIEW()
        
        if vv_instance.vv is None:
            print("Failed to connect to VibrationVIEW")
            return None
            
        return vv_instance
        
    except ImportError as e:
        print(f"Could not import VibrationVIEW API: {e}")
        return None
    except Exception as e:
        print(f"Error connecting to VibrationVIEW: {e}")
        return None

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == '__main__':
    # Simple connection test
    print("Testing VibrationVIEW connection...")
    test_instance = get_vv_instance()
    if test_instance is None:
        print("Failed to initialize VibrationVIEW. Exiting.")
        exit(-1)
    else:
        print("VibrationVIEW connection test successful")
    
    # Create and run app
    print("Starting Flask server...")
    app = create_app()
    
    try:
        app.run(debug=True, threaded=True)
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Server error: {e}")
        raise