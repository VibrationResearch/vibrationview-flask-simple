def register_routes(app):
    """Register all route blueprints to the Flask app"""
    from routes.status import status_bp
    from routes.channels import channels_bp
    from routes.pretest import pretest_bp
    from routes.teds import teds_bp
    from routes.test import test_bp
    from routes.inputconfig import inputconfig_bp
    
    # Register blueprints
    app.register_blueprint(status_bp)
    app.register_blueprint(channels_bp)
    app.register_blueprint(pretest_bp)
    app.register_blueprint(teds_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(inputconfig_bp)