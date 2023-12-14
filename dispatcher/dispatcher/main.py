import os
import pika
import tomllib
from flask import Flask
from pathlib import Path

app = Flask(__name__)
env = os.environ.get("ENV", "development")

config_file = Path(__file__).parent.joinpath(f"config_{env}.toml")
config = tomllib.load(open(config_file, "rb"))
app.config.update(config)

# Register the blueprint with the app
from dispatcher.routes.healthcheck import healthcheck_bp
from dispatcher.routes.dispatcher import dispatcher_bp

app.register_blueprint(dispatcher_bp, url_prefix="/dispatcher")
app.register_blueprint(healthcheck_bp, url_prefix="/internal")


if __name__ == '__main__':
    app.run()

