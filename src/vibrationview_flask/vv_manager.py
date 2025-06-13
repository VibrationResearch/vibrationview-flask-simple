from functools import wraps
from flask import jsonify
from vibrationviewapi import VibrationVIEW, ExtractComErrorInfo

def extract_com_error_info(exception):
    """
    Extract information from COM errors for better error reporting
    This is a wrapper for ExtractComErrorInfo to ensure consistent error handling
    """
    try:
        return ExtractComErrorInfo(exception)
    except Exception:
        # Fallback if ExtractComErrorInfo fails
        return str(exception)

def with_vv_connection(func):
    """
    Decorator to handle VibrationVIEW connection for route handlers
    
    This decorator:
    1. Creates a VibrationVIEW connection
    2. Passes it to the route handler
    3. Handles exceptions
    4. Ensures the connection is properly released
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        vv_instance = VibrationVIEW()
        if not vv_instance:
            return jsonify({'Error': 'Could not connect to VibrationVIEW'}), 500
        
        try:
            return func(vv_instance, *args, **kwargs)
        except Exception as e:
            return jsonify(extract_com_error_info(e)), 500
        finally:
            vv_instance = None
            
    return wrapper
