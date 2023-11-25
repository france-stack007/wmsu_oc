from gunicorn.app.base import BaseApplication
from wmsu_oc import create_app

flask_app = create_app()

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

options = {
    'bind': '0.0.0.0:5000',  # Adjust the host and port as needed
    'workers': 4,  # Adjust the number of workers based on your needs
    'timeout': 120  # Adjust the timeout if needed
}

StandaloneApplication(flask_app, options).run()
