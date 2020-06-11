import os
from test_navigator import app, test_navigator_routes

app.register_blueprint(test_navigator_routes.bp)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
