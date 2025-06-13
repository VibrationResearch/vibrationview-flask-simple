import os
from flask import Flask
from routes import register_routes

def create_app():
    app = Flask(__name__)
    
    # Register all routes
    register_routes(app)
    
    return app

if __name__ == '__main__':
    # Only initialize VibrationVIEW in the main process, not reloader
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        try:
            # Import here to avoid circular imports
            from vibrationviewapi import VibrationVIEW
            
            # Check VV connection before starting server
            vv_instance = VibrationVIEW()
            if vv_instance.vv is None:
                print("Connection to VibrationVIEW failed")
                vv_instance = None  # Release the connection
                exit(-1)
            
        except ImportError as e:
            print(f"Could not import VibrationVIEW API: {e}")
            print("Make sure they are in the same directory or in your Python path.")
            exit(-1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit(-1)
    
    # Create and run app
    print("Creating Flask app...")
    app = create_app()
    print("Starting Flask server...")
    app.run(debug=True)
