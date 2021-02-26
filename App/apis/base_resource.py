from flask_restful import Resource


class TabrResource(Resource):
    pass
    #
    # def options(self):
    #     return {'Allow': '*'}, 200, {'organId':'1333333333',
    #         "Access-Control-Allow-Credentials": "true",
    #                                  'Access-Control-Allow-Origin': '*',
    #                                  'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
    #                                  'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
    #                                  }
    #
    # def post(self):
    #     return {'Allow': '*'}, 200, {'organId':'1333333333',
    #         "Access-Control-Allow-Credentials": "true",
    #                                  'Access-Control-Allow-Origin': '*',
    #                                  'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
    #                                  'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
    #                                  }