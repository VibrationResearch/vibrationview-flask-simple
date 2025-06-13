from functools import wraps
from flask import jsonify

def with_vibrationview(func):
    """Decorator that provides VibrationVIEW instance to route functions"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Import here to avoid circular imports
        from app import get_vv_instance
        
        vv_instance = get_vv_instance()
        if vv_instance is None:
            return jsonify({"error": "VibrationVIEW not available"}), 503
        
        # Pass vv_instance as the first argument to the decorated function
        return func(vv_instance, *args, **kwargs)
    return wrapper