from app import app
from flaskext.mysql import MySQL
import pymysql
from app import app
from config import mysql
from flask import jsonify, flash, request

# ("SELECT idProducto,nombre,descripcion,marca,peso FROM producto")
@app.route("/createRegistro_inventario", methods=["POST"])
def create_registroInventario():
    try:
        _json = request.json
        _idProducto = _json["idProducto"]
        _idRegistro = _json["idRegistro"]
        _idUsuario = _json["idUsuario"]
        _fecha_de_vencimiento = _json["fecha_de_vencimiento"]
        _estado = _json["estado"]
        _cantidad = _json["cantidad"]
        if (
            _idProducto
            and _idRegistro
            and _idUsuario
            and _fecha_de_vencimiento
            and _estado
            and _cantidad
            and request.method == "POST"
        ):

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO registro_inventario(idProducto, idRegistro, idUsuario, fecha_de_vencimiento,estado,cantidad) VALUES(%s,%s,%s,%s,%s,%s)"
            bindData = (
                int(_idProducto),
                int(_idRegistro),
                int(_idUsuario),
                _fecha_de_vencimiento,
                _estado,
                int(_cantidad),
            )
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify("Registro de datos exitoso!")
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/registro_inventario")
def getRegistroInventario():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idProducto, idRegistro, idUsuario, cantidad, fecha_de_vencimiento,estado FROM registro_inventario"
        )
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/producto")
def getProducto():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idProducto, nombre, descripcion, marca, peso FROM producto"
        )
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/receta")
def getReceta():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT idReceta, nombre_receta,instruccion,imagen FROM receta")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/user")
def getUser():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idUsuario, nombre, email, apellido, edad, ubicacion FROM usuario"
        )
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        "status": 404,
        "message": "Record not found: " + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run()
