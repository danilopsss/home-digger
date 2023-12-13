import os
import toml
from flask import Flask
from pathlib import Path
from .routes.upload import upload_bp
from .routes.healthcheck import healthcheck_bp

app = Flask(__name__)
env = os.environ.get("FLASK_ENV", "dev")
# todo: check why from_file is not working directly
config_file = Path(__file__).parent.joinpath(f"config_{env}.toml")
config = toml.load(config_file)
app.config.update(config)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


# Register the blueprint with the app
app.register_blueprint(upload_bp)
app.register_blueprint(healthcheck_bp)

if __name__ == '__main__':
    app.run()

