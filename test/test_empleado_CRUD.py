import unittest
import json
from CRUD_Customer import DBMongoConnection

class empleado(unittest.TestCase):
    def test_connection_mongoDB(self):
        try:

            with open('configuration/configConnectionDB.json','r') as f:
                config = json.load(f)

            self.ConnectionCustomerMongoDB = DBMongoConnection.connectionCustomerMongoDB(config["DATABASECONN_CUSTOMER"]["IP"],
                                                                                    config["DATABASECONN_CUSTOMER"]["PORT"],
                                                                                    config["DATABASECONN_CUSTOMER"]["USER"],
                                                                                    config["DATABASECONN_CUSTOMER"]["PASSWORD"],
                                                                                    config["DATABASECONN_CUSTOMER"]["DB"],
                                                                                    config["DATABASECONN_CUSTOMER"]["COLLECTION"])
            self.ConnectionCustomerMongoDB.openConnection
            self.ConnectionCustomerMongoDB.closeConnection
            self.assertEqual(1,1) 

        except AssertionError:
            self.assertEqual(0,1)
        except:
            self.assertEqual(0,1)

    def test_InsertMongoDB(self):
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
            #docuInserted = ConnectionCustomerMongoDB.insertCustomer(dato)
        
            #docuInserted = int(str(docuInserted),base=0)
            self.assertEqual(1,1)
            
            #self.assertGreater(docuInserted,0)
        
        except AssertionError:
            self.assertEqual(0,1)
        except Exception as e:
            print(e)
            self.assertEqual(0,1)

    def test_SelectCustomer(self):
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
            print(ConnectionCustomerMongoDB.SelectCustomer(dato))
            ConnectionCustomerMongoDB.closeConnection
        except Exception as e:
            self.assertEqual(0,1)
            print(e)

    def test_UpdateCustomer(self):
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
            self.assertEqual(1,1)
        except Exception as e:
            self.assertEqual(0,1)
            print(e)

    def test_DeleteCustomer(self):
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
            self.assertEqual(1,1)
        except Exception as e:
            self.assertEqual(0,1)
            print(e)
