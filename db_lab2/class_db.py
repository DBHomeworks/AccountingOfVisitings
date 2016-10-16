import sys
import MySQLdb as mydb
import xml.etree.ElementTree as ET
import pymongo
from pymongo import MongoClient


class MyDataDase:

    host = 'localhost'
    db_user_name = 'root'
    password = '852456aaa'
    db_name = 'mydb'


    # def ShowAllInfo(self):
    #     con = None
    #     rows = []
    #
    #     try:
    #         con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
    #
    #         cur = con.cursor()
    #         cur.execute("SELECT EmployeeInfo.employee_id, EmployeeInfo.employee_name, EmployeeInfo.date_of_birthday, EmployeeInfo.family, WorkPlace.position, WorkPlace.salary, WorkPlace.comp_auto, WorkPlace.start_of_working, Company.company_name "
    #                     "FROM EmployeeInfo JOIN WorkPlace ON EmployeeInfo.workplace_id=WorkPlace.workplace_id "
    #                     "JOIN Company ON WorkPlace.company_id=Company.company_id "
    #                     "ORDER BY EmployeeInfo.employee_id;")
    #
    #
    #         rows = cur.fetchall()
    #         print rows
    #
    #     except mydb.Error, e:
    #
    #         print "Error %d: %s" % (e.args[0],e.args[1])
    #         sys.exit(1)
    #
    #     finally:
    #         if con:
    #             con.close()
    #         return rows


    def ShowAllInfo(self):
        rows = []
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        db = client.attendance_records
        employees = db.employee_info
        for employee in employees.find().sort('id'):
            rows.append(employee)
        return rows

    def ShowTableCompanies(self):
        con = None
        rows = []

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM Company;")

            rows = cur.fetchall()
            print 'Big type: ', type(rows)

            for row in rows:
                print type(row), ' : ', row

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    def ShowTableEmployeeInfo(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM EmployeeInfo;")


            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    def ShowTableWorkPlace(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM WorkPlace;")


            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    def ShowTableVisiting(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT * FROM Visiting;")


            rows = cur.fetchall()



        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    def Accounting(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT Visiting.visit_id, EmployeeInfo.employee_name, Visiting.visit_date "
                        "FROM Visiting JOIN EmployeeInfo ON Visiting.employee_id=EmployeeInfo.employee_id;")

            rows = cur.fetchall()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    def GetVisitingById(self, _id):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);

            cur = con.cursor()
            cur.execute("SELECT Visiting.visit_id, EmployeeInfo.employee_name, Visiting.visit_date "
                        "FROM Visiting JOIN EmployeeInfo ON Visiting.employee_id=EmployeeInfo.employee_id "
                        "WHERE Visiting.visit_id='" + str(_id) +  "';")

            rows = cur.fetchone()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()
            return rows

    def AddVisiting(self, request):
        con = None

        print request["date"]

        inserted_date = str(request["date"])
        inserted_id = str(request["employee_id"])

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()
            cur.execute("""INSERT INTO Visiting(employee_id, visit_date) VALUES (%s, %s);""", (inserted_id, inserted_date))
            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close()

    def DeleteVisiting(self, request):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()
            cur.execute("DELETE FROM Visiting WHERE visit_id=" + request["visit_id"] + ";")
            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close

    def ShowEmployeeWithFamily(self ,request):
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
                        "WHERE EmployeeInfo.family=TRUE;")
            rows = cur.fetchall()

            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close
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
                        "WHERE Company.company_name LIKE '" + request["name"] + "';")
            rows = cur.fetchall()

            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close
            return rows

    def BooleanModeSearch(self, request):
        con = None
        rows = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()

            a = "+(+" + request["name"]
            a.replace(" ", " +")

            cur.execute("SELECT EmployeeInfo.employee_id, EmployeeInfo.employee_name, EmployeeInfo.date_of_birthday, EmployeeInfo.family, "
                        "WorkPlace.position, WorkPlace.salary, WorkPlace.comp_auto, WorkPlace.start_of_working, Company.company_name "
                        "FROM EmployeeInfo "
                        "JOIN WorkPlace ON EmployeeInfo.workplace_id=WorkPlace.workplace_id "
                        "JOIN Company ON WorkPlace.company_id=Company.company_id "
                        "WHERE MATCH(EmployeeInfo.employee_name) AGAINST ('" + a + ")' IN BOOLEAN MODE);")

            rows = cur.fetchall()

            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close
            return rows

    def EditVisit(self, request):
        con = None
        rows = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()
            cur.execute("UPDATE Visiting "
                        "SET employee_id='" + request["employee_id"] + "', visit_date='" + request["date"] + "' "
                        "WHERE visit_id='" + request["visit_id"] + "'")

            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close

    def ClearDB(self):
        con = None

        try:
            con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
            cur = con.cursor()
            cur.execute("DELETE FROM EmployeeInfo;")
            cur.execute("DELETE FROM Company;")
            cur.execute("DELETE FROM WorkPlace;")


            con.commit()

        except mydb.Error, e:

            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            if con:
                con.close

    def FillDB(self):
        con = None

        tree = ET.parse("/home/taras/Documents/Python/DB_LAB2/static/data.xml")
        root = tree.getroot()

        con = mydb.connect( self.host, self.db_user_name, self.password, self.db_name);
        cur = con.cursor()
        for child in root:
            if child.tag == "companies" :
                for company in child :
                    print company
                    cur.execute("INSERT INTO Company "
                                    "VALUES(" + company.attrib["company_id"] + ", '" + company.attrib["company_name"] + "');")

            if child.tag == "workplaces" :
                for workplace in child :
                    print workplace
                    cur.execute("INSERT INTO WorkPlace "
                                    "VALUES(" + workplace.attrib["workplace_id"] + ", " + workplace.attrib["company_id"] + " ,'" + workplace.attrib["position"] + "', " + workplace.attrib["salary"] + ", " + workplace.attrib["comp_auto"] + ", '" + workplace.attrib["start_of_working"] + "');")

            if child.tag == "employees" :
                for employee in child :
                    print employee
                    print "INSERT INTO EmployeeInfo VALUES(" + employee.attrib["employee_id"] + ", '" + employee.attrib["employee_name"] + "', '" + employee.attrib["date_of_birthday"] + "', " + employee.attrib["family"] + ", " + employee.attrib["workplace_id"] + ";"
                    cur.execute("INSERT INTO EmployeeInfo "
                                   "VALUES(" + employee.attrib["employee_id"] + ", '" + employee.attrib["employee_name"] + "', '" + employee.attrib["date_of_birthday"] + "', " + employee.attrib["family"] + ", " + employee.attrib["workplace_id"] + ");")

        con.commit()
