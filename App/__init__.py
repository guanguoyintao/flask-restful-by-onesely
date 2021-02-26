from flask import Flask
from flask_cors import CORS

from App.apis import init_api
from App.exts import init_ext
from App.settings import envs



def create_app():
    app=Flask(__name__)
    CORS(app)
    app.config.from_object(envs.get('develop'))
    init_ext(app)
    init_api(app)
    return app