from flask import Flask

from flask_cors import CORS 
from routes import createRoute

app = Flask(__name__)
CORS(app)

## reginster the blueprints
app.register_blueprint(createRoute)

if __name__ == "__main__":
    app.run(debug=True)