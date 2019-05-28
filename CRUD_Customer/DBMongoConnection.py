import json
import jsonschema
from pymongo import MongoClient
from jsonschema import ValidationError
from jsonschema import SchemaError

class connectionCustomerMongoDB():

    functionActions = {'POST':1, 'GET':2, 'DELETE':3,'PUT':4}

    def __init__(self, ip, port, user, password, db, col):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.col = col
        self.p1 = MongoClient("mongodb://"+ip+":"+port)
        with open('configuration/configConnectionDB.json','r') as self.f:
            self.config = json.load(self.f)

    def openConnection(self):
        #self.p1 = pymongo.MongoClient("mongodb://"+self.ip+":"+self.port+"/")
        #self.p1 = MongoClient("mongodb://"self.user+":"+self.ip+":"+self.port+"/")
        self.db = self.p1[self.db]
        #print("Connected successfully!!!")
        self.col = self.db[self.col]

    def SchemaValidation(self, typeValidation, data):
        try:
            if typeValidation == self.functionActions["POST"]:
                schema = open(self.config["SCHEMAS_VALIDATION"]["PATH_INSERT"]+'/'+
                                            self.config["SCHEMAS_VALIDATION"]["FILENAME_INSERT"]).read()
            elif typeValidation == self.functionActions["GET"]:
                schema = open(self.config["SCHEMAS_VALIDATION"]["PATH_SELECT"]+'/'+
                                            self.config["SCHEMAS_VALIDATION"]["FILENAME_SELECT"]).read()
            elif typeValidation == self.functionActions["PUT"]:
                schema = open(self.config["SCHEMAS_VALIDATION"]["PATH_INSERT"]+'/'+
                                            self.config["SCHEMAS_VALIDATION"]["FILENAME_INSERT"]).read()
            elif typeValidation == self.functionActions["DELETE"]:
                schema = open(self.config["SCHEMAS_VALIDATION"]["PATH_DELETE"]+'/'+
                                            self.config["SCHEMAS_VALIDATION"]["FILENAME_DELETE"]).read()
            schema = json.loads(schema)

            jsonschema.Draft4Validator.check_schema(schema)
            jsonschema.Draft4Validator(schema).validate(data)
        except ValidationError as valiError:
            raise valiError
        except SchemaError as sch_err:
            raise sch_err
        except Exception as other:
            raise other

    def calcSalarioPagar(self,valorh, horasT):
        return valorh * horasT

    def insertCustomer(self,data):
        try:
            docu_inserted = 0
            self.SchemaValidation(self.functionActions["POST"], data)
            DatoInsert = data
            DatoInsert["salariopagar"] = self.calcSalarioPagar(data["valorhora"],data["horastrabajadas"])
            self.db = self.p1[str(self.db)]
            self.col = self.db[str(self.col)]
            docu_inserted = self.col.insert_one(DatoInsert)
            self.closeConnection
        except ValidationError as valiError:
            #print('exception ValidationError'+str(valiError))
            raise valiError
        except SchemaError as sch_err:
            #print('exception SchemaError'+str(sch_err))
            raise sch_err
        except Exception as other:
            #print('exception OtherError'+str(other))
            raise other
        finally:
            return docu_inserted

    def SelectCustomer(self,dataFind):
        #self.openConnection
        try:
            self.SchemaValidation(self.functionActions["GET"],dataFind)
            self.db = self.p1[str(self.db)]
            self.col = self.db[str(self.col)]
            CustomersCli = []
            dataJson = {"Customers":{}}
            for data in self.col.find({},dataFind):
                CustomersCli.append(data)
            dataJson["Customers"] = CustomersCli
            self.closeConnection
            return dataJson
        except Exception as e:
            raise e

    def UpdateCustomer(self,data):
        try:
            docu_updated = 0
            self.SchemaValidation(self.functionActions["PUT"], data)
            DatoUpdate = data
            DatoUpdate["salariopagar"] = self.calcSalarioPagar(data["valorhora"],data["horastrabajadas"])

            self.db = self.p1[str(self.db)]
            self.col = self.db[str(self.col)]
            query = {"cedula":data["cedula"]}
            del DatoUpdate['cedula'] 
            #DatoUpdate["cedula"].remove(0)
            DatoUpdate = {"$set":DatoUpdate}

            docu_updated = self.col.update_many(query, DatoUpdate)
            self.closeConnection
        except ValidationError as valiError:
            #print('exception ValidationError'+str(valiError))
            raise valiError
        except SchemaError as sch_err:
            #print('exception SchemaError'+str(sch_err))
            raise sch_err
        except Exception as other:
            #print('exception OtherError'+str(other))
            raise other
        finally:
            return docu_updated

    def DeleteCustomer(self,data):
        try:
            docu_deleted = 0
            self.SchemaValidation(self.functionActions["DELETE"], data)
            self.db = self.p1[str(self.db)]
            self.col = self.db[str(self.col)]
            query = {"cedula":data["cedula"]}

            docu_deleted = self.col.delete_many(query)
            self.closeConnection
        except ValidationError as valiError:
            #print('exception ValidationError'+str(valiError))
            raise valiError
        except SchemaError as sch_err:
            #print('exception SchemaError'+str(sch_err))
            raise sch_err
        except Exception as other:
            #print('exception OtherError'+str(other))
            raise other
        finally:
            return docu_deleted

    def closeConnection(self):
        self.p1.close
