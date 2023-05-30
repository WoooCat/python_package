from flask import Flask
from flask_restful import Api
from .api.v1.endpoints import GroupListResource, GroupResource
from .db import engine
from .db.models.base import Base

app = Flask(__name__)
api = Api(app)

Base.metadata.create_all(engine)

api.add_resource(GroupListResource, '/groups')
api.add_resource(GroupResource, '/groups/<int:group_id>')
