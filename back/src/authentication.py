from functools import wraps
import jwt 
from flask import request, jsonify, current_app
from models.entidades import Usuario
from config import DevelopmentConfig as dbConfig

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, ** kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']            

        if not token:
            return jsonify({"error": "Sem Authorização." }), 403               

        if not "Bearer" in token:
            return    jsonify({"error": "Token Inválido."}), 401 

        try:
            token_puro = token.replace("Bearer ", "")            
            decoded = jwt.decode(token_puro, dbConfig.SECRET_KEY, algorithms=["HS256"])
            print(decoded)
            usuario_logado = Usuario.query.get(decoded['id'])
            
        except:
            return jsonify({"error": " O Token é Inválido."}), 403

        return f(current_user=usuario_logado, *args, **kwargs)

    return wrapper    


