import json
#from CRUD_Customer import DBMongoConnection
import DBMongoConnection
#import CRUD_Customer.DBMongoConnection

def test_InsertCustomer():
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

def test_SelectCustomer():
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

def test_UpdateCustomer():
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

def test_DeleteCustomer():
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

#print (test_SelectCustomer())
test_DeleteCustomer()