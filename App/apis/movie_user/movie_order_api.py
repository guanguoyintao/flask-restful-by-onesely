from flask import g
from flask_restful import Resource, reqparse, abort

from App.apis.movie_user.uitls import login_requied, require_permission
from App.models.user.model_constant import VIP_USER


class MovieOrdersResource(Resource):
    @login_requied
    def post(self):
        user=g.user
        return {'msg':'post order ok'}
class MovieOrderResource(Resource):
    @require_permission(VIP_USER)
    def put(self,order_id):
        return  {'msg':'变更成功'}