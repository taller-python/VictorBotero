from flask import Flask
from flask_restful import Resource, Api
from CRUD_Customer import DBMongoConnection
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class wscustomer(Resource):
    def get(self):
        try:
            with open('configuration/configConnectionDB.json','r') as f:
                config = json.load(f)

            dato = open(config["DATOS_TEST"]["PATH_SELECT"]+'/'+
                                        config["DATOS_TEST"]["FILENAME_SELECT"]).read()
            dato = json.loads(dato)
            ConnectionCustomerMongoDB = DBMongoConnection.connectionCustomerMongoDB(config["DATABASECONN_CUSTOMER"]["IP"],
                                                                                    config["DATABASECONN_CUSTOMER"]["PORT"],
                                                                                    config["DATABASECONN_CUSTOMER"]["USER"],
                                                                                    config["DATABASECONN_CUSTOMER"]["PASSWORD"],
                                                                                    config["DATABASECONN_CUSTOMER"]["DB"],
                                                                                    config["DATABASECONN_CUSTOMER"]["COLLECTION"])

            returnedData = ConnectionCustomerMongoDB.SelectCustomer(dato)
            ConnectionCustomerMongoDB.closeConnection
        except Exception as e:
            #self.assertEqual(0,1)
            print(e)
        return returnedData

    def post(self):
        try:
            with open('configuration/configConnectionDB.json','r') as f:
                config = json.load(f)

            dato = open(config["DATOS_TEST"]["PATH_INSERT"]+'/'+
                                        config["DATOS_TEST"]["FILENAME_INSERT"]).read()
            dato = json.loads(dato)

            ConnectionCustomerMongoDB = DBMongoConnection.connectionCustomerMongoDB(config["DATABASECONN_CUSTOMER"]["IP"],
                                                                                config["DATABASECONN_CUSTOMER"]["PORT"],
                                                                                config["DATABASECONN_CUSTOMER"]["USER"],
                                                                                config["DATABASECONN_CUSTOMER"]["PASSWORD"],
                                                                                config["DATABASECONN_CUSTOMER"]["DB"],
                                                                                config["DATABASECONN_CUSTOMER"]["COLLECTION"])
            ConnectionCustomerMongoDB.insertCustomer(dato)
        except Exception as e:
            print(str(e))
    def put(self):
        try:
            with open('configuration/configConnectionDB.json','r') as f:
                config = json.load(f)

            dato = open(config["DATOS_TEST"]["PATH_UPDATE"]+'/'+
                                        config["DATOS_TEST"]["FILENAME_UPDATE"]).read()
            dato = json.loads(dato)

            ConnectionCustomerMongoDB = DBMongoConnection.connectionCustomerMongoDB(config["DATABASECONN_CUSTOMER"]["IP"],
                                                                    config["DATABASECONN_CUSTOMER"]["PORT"],
                                                                    config["DATABASECONN_CUSTOMER"]["USER"],
                                                                    config["DATABASECONN_CUSTOMER"]["PASSWORD"],
                                                                    config["DATABASECONN_CUSTOMER"]["DB"],
                                                                    config["DATABASECONN_CUSTOMER"]["COLLECTION"])
            ConnectionCustomerMongoDB.UpdateCustomer(dato)
            #self.assertEqual(1,1)
        except Exception as e:
            #self.assertEqual(0,1)
            print(e)
    def delete(self):
        try:
            with open('configuration/configConnectionDB.json','r') as f:
                config = json.load(f)
            
            dato = open(config["DATOS_TEST"]["PATH_DELETE"]+'/'+
                                        config["DATOS_TEST"]["FILENAME_DELETE"]).read()
            dato = json.loads(dato)

            ConnectionCustomerMongoDB = DBMongoConnection.connectionCustomerMongoDB(config["DATABASECONN_CUSTOMER"]["IP"],
                                                                    config["DATABASECONN_CUSTOMER"]["PORT"],
                                                                    config["DATABASECONN_CUSTOMER"]["USER"],
                                                                    config["DATABASECONN_CUSTOMER"]["PASSWORD"],
                                                                    config["DATABASECONN_CUSTOMER"]["DB"],
                                                                    config["DATABASECONN_CUSTOMER"]["COLLECTION"])
            ConnectionCustomerMongoDB.DeleteCustomer(dato)
            #self.assertEqual(1,1)
        except Exception as e:
            #self.assertEqual(0,1)
            print(e)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
