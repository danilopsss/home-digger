import os
import tomllib
from flask import Flask
from pathlib import Path
from .routes.upload import upload_bp
from .routes.healthcheck import healthcheck_bp

app = Flask(__name__)
env = os.environ.get("ENV", "development")

config_file = Path(__file__).parent.joinpath(f"config_{env}.toml")
config = tomllib.load(open(config_file, "rb"))
app.config.update(config)

# Register the blueprint with the app
app.register_blueprint(upload_bp)
app.register_blueprint(healthcheck_bp)

if __name__ == '__main__':
    app.run()

