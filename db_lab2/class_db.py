import sys
import MySQLdb as mydb
import xml.etree.ElementTree as ET
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


class MyDataDase:

    def ShowAllInfo(self):
        rows = []
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        employees = db.employee_info
        for employee in employees.find().sort('id'):
            rows.append(employee)
        return rows

    def Accounting(self):
        rows = []
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        visits = db.visiting
        for visit in visits.find():
            employee = client.attendance_records.employee_info.find_one({'_id': ObjectId(visit['employee'])})
            rows.append({'id' : visit['_id'], 'employee' : employee, 'date' : visit['date']})

        return rows

    def GetVisitingById(self, _id):
        rows = []

        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        visits = db.visiting

        for v in visits.find({'_id' : ObjectId(_id)}):
            rows.append({'visit_id' : v['_id'], 'employee' : v['employee'], 'date' : v['date']})

        print rows
        return rows

    def GetEmployeeObjectId(self, id):
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        employees = db.employee_info
        for employee in employees.find():
            if employee['id'] == id:
                inserted_id = employee['_id']
                return inserted_id

    def AddVisiting(self, request):
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        visits = db.visiting

        employee_object_id = self.GetEmployeeObjectId(int(request['employee_id']))

        date = request["date"]
        date = datetime.strptime(date, '%Y-%m-%d')

        visits.insert_one({'date' : date, 'employee' : ObjectId(employee_object_id)})

    def DeleteVisiting(self, request):
        # print request['visit_id']

        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        visits = db.visiting
        result = visits.delete_many({"_id" : ObjectId(request['visit_id'])})

    def ShowEmployeeWithFamily(self ,request):
        rows = []

        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        employees = db.employee_info
        for employee in employees.find({"family": 1}).sort('id'):
            rows.append(employee)

        return rows

    def DateSearch(self ,request):
        con = None
        rows = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()
            cur.execute("SELECT EmployeeInfo.employee_id, EmployeeInfo.employee_name, EmployeeInfo.date_of_birthday, EmployeeInfo.family, "
                        "WorkPlace.position, WorkPlace.salary, WorkPlace.comp_auto, WorkPlace.start_of_working, Company.company_name "
                        "FROM EmployeeInfo "
                        "JOIN WorkPlace ON EmployeeInfo.workplace_id=WorkPlace.workplace_id "
                        "JOIN Company ON WorkPlace.company_id=Company.company_id "
                        "WHERE DATE(EmployeeInfo.date_of_birthday) BETWEEN '" + request["from"] + "' AND '" + request["to"] + "';")
            rows = cur.fetchall()

            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close
            return rows

    def ExactlySearch(self, request):
        rows = []

        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        employees = db.employee_info
        for employee in employees.find({"workplace.company" : request['name']}).sort('id'):
            rows.append(employee)

        return rows

    def BooleanModeSearch(self, request):
        rows = []

        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        employees = db.employee_info
        for employee in employees.find({"name" : request['name']}).sort('id'):
            rows.append(employee)

        return rows

    def EditVisit(self, request):
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        visits = db.visiting

        date = datetime.strptime(request['date'], '%Y-%m-%d')
        employee_object_id = self.GetEmployeeObjectId(int(request['employee_id']))

        print request['visit_id']
        print date, ' ', type(date)
        print employee_object_id

        visit = {'employee' : ObjectId(employee_object_id), 'date' : date}
        visits.update({'_id' : ObjectId(request['visit_id'])}, {"$set" : visit}, upsert=False)