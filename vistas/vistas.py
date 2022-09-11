from flask_restful import Resource

class VistaUbicacion(Resource):
    def get(self):
        return{"ubicación":{"id":1}}
