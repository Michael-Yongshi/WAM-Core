import os
import datetime

from pathlib import Path

from shutil import copyfile

import sqlite3
from sqlite3 import Error


# https://stackoverflow.com/questions/2047814/is-it-possible-to-store-python-class-objects-in-sqlite

def get_localpath():
    """set the paths to the users documents folder"""

    local_path = os.path.join("~", "Documents", "OWB")
    path = os.path.expanduser(local_path)

    return path

def show_files(path = ""):
    """Show all files in a folder"""

    if path == "":
        path = get_localpath()

    # Create file list
    filelist = []
    # check if directory already exists, if not cancel opening
    if not os.path.exists(path):
        print(f"couldnt find path: {path}")
        return filelist
        
    # Iterate over sqlite files
    for filename in os.listdir(path):
        if filename.endswith(".sqlite"): 
            name = os.path.splitext(filename)[0]
            filelist.append(name)

    return path, filelist

def saveas_file(srcfile, dstfile, srcpath = "", dstpath = "", extension = ".sqlite"):

    if srcpath == "":
        srcpath = get_localpath()
    
    if dstpath == "":
        dstpath = get_localpath()
    
    srcfile = srcfile + extension
    dstfile = dstfile + extension

    src = os.path.join(srcpath, srcfile)
    dst = os.path.join(dstpath, dstfile)

    if os.path.exists(src):
        if os.path.exists(dst):
            print(f"error path destination: {dst} already exists")

        else:
            print(f"copying file: {src} to {dst}")
            copyfile(src, dst)

    else:
        print(f"Source path does not exist: {src}")

def check_existance(filename, path = "", extension = ".sqlite"):

    if path == "":
        path = get_localpath()

    destination = os.path.join(path, filename + extension)
    if os.path.exists(destination):
        # print(f"destination: {destination} already exists")
        return True
    else:
        # print(f"destination: {destination} doesnt exist")
        return False

class Database(object):
    def __init__(self, filename, path=""):

        self.filename = filename

        if path == "":
            path = get_localpath()
        self.path = path

        self.connection = None
        self.tables = []
        
        existance = check_existance(path=path, filename=filename)
        self.connect_database()

        if existance == True:
            print(f"Database with path {path} and filename {filename} already exists, connection opened to existing database")
            
            # pull all sql tables and records
            self.get_tables()
        else:
            print(f"Database with path {path} and filename {filename} could not be found, connection opened to new database")

    def delete_database(self):

        self.connection.close()

        completepath = os.path.join(self.path, self.filename + ".sqlite")
        os.remove(completepath)

        print(f"Database deleted!")

    def saveas_database(self, filename, path=""):

        if path == "":
            path = get_localpath()
        self.path = path

        existance = check_existance(path=path, filename=filename)

        if existance == True:
            print(f"Database with path {path} and filename {filename} already exists, connection refused!")
            
        else:
            print(f"Database with path {path} and filename {filename} is free, saving database to the new file")

            saveas_file(
                srcfile = self.filename, 
                dstfile = filename,
                srcpath = self.path,
                dstpath = path,
                )

            new_database = Database(
                filename=filename, 
                path=path,
            )

            return new_database

    def connect_database(self):

        try:
            destination = os.path.join(self.path, f"{self.filename}.sqlite")

            # check if directory already exists, if not create it
            if not os.path.exists(self.path):
                os.makedirs(self.path)

            self.connection = sqlite3.connect(destination)
            print("Connection to SQLite DB successful")

        except Error as e:

            print(f"The error '{e}' occurred")

    def close_database(self):
        self.connection.close()

    def delete_table(self, table):

        query = f"DROP TABLE {table.name}"
        self.execute_query(query)

        index = self.tables.index(table)
        self.tables.pop(index)

        print(f"table {table.name} deleted and removed from table list!")

    def delete_records(self, table, records):
        
        parameters = []
        for record in records:
            parameters += [record.primarykey]

        placeholders = ', '.join('?' for _ in parameters)

        query = f"DELETE FROM {table.name} WHERE id IN ({placeholders})"

        self.execute_parameterised_query(query, parameters)

        table.readAllRecords()

    def get_tables(self):
        """
        Refresh all tables
        """

        # get existing tables
        self.tables = []
        tablenames = self.read_table_names()
        tablenames.sort()
        # print(f"getting tablenames for database {self.filename}")

        for tablename in tablenames:
            if tablename != 'sqlite_sequence':
                tableobject = Table.open_existing_table(self, tablename)
                self.tables += [tableobject]

    def get_table(self, tablename):

        for table in self.tables:
            if table.name == tablename:
                retrieved_table = table
                break

        return retrieved_table

    def execute_query(self, query):
        cursor = self.connection.cursor()

        try:
            print(f"--------------------\n{query}\n")
            cursor.execute(query)
            self.connection.commit()
            print("Success!\n--------------------")

            return cursor

        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_parameterised_query(self, query, parameters):
        """
        build a parameterised query:
        for a parameter list of 3 length like below
        -parameters = [1,2,3]
        -placeholders = ', '.join('?' for _ in parameters)
        this results in '?, ?, ?'

        meaning
        for each (_ denotes an unused variable) in parameters, join the strings ('?') with a comma and a space (', ') in order to not have to remove a trailing comma

        then merge with query
        -query= 'SELECT name FROM students WHERE id IN (%s)' % placeholders

        meaning
        this replaces the "%s with our placeholders ('?, ?, ?' in our case)
        """

        cursor = self.connection.cursor()

        try:
            print(f"--------------------query\n{query}\n")
            print(f"--------------------parameters\n{parameters}\n")
            cursor.execute(query, parameters)
            self.connection.commit()
            print("Success!\n--------------------")

            return cursor

        except Error as e:
            print(f"The error '{e}' occurred")

    def read_table_names(self):

        query = f"SELECT name FROM sqlite_master WHERE type='table';"
        
        cursor = self.execute_query(query=query)
        data = cursor.fetchall()
        # print(tables)

        tables = []
        for datapoint in data:
            tables += [datapoint[0]]

        return tables

    def read_column_names(self, table):

        query = f"SELECT * FROM {table};"
        
        cursor = self.execute_query(query=query)
        description = cursor.description
        # print(description)
        
        # print(description)
        columns = []
        for record in description:
            # print(record[0])
            columns += [record[0]]
        
        # print(columns)
        return columns

    def read_column_metadata(self, table):
        
        # print(table)
        cursor = self.execute_query(f'PRAGMA table_info({table})')
        data = cursor.fetchall()

        column_order = []
        column_names = []
        column_types = []

        for datapoint in data:
            # print(f"{datapoint[0]} {datapoint[1]} {datapoint[2]}")
            column_order += [datapoint[0]]
            column_names += [datapoint[1]]
            column_types += [datapoint[2]]

        metadata = {
            "column_order": column_order,
            "column_names": column_names,
            "column_types": column_types,
        }
        # print(metadata)

        return metadata

    def read_column_types(self, table):

        cursor = self.execute_query(f'PRAGMA table_info({table})')
        data = cursor.fetchall()

        columns = []
        for datapoint in data:
            # print(f"{datapoint[0]} {datapoint[1]} {datapoint[2]}")
            columns += [datapoint[2]]

        # print(columns)
        return columns

    def read_records(self, table, columns=[], where = []):

        if columns == []:
            column_line = "*"

        else:
            column_line = ', '.join(columns)
        
        parameters = tuple()
        
        # where can be collected as [[column name, [values]], [column name2, [values2]]]
        # print(f"where {where}")
        if where == []:
            whereline = ""

        else:
            whereline = "WHERE "
            for statement in where:
                parameters += tuple(statement[1])
                # print(f"statement {statement}")
                # print(f"statement0 {statement[0]}")
                # print(f"statement1 {statement[1]}")
                whereline += f"{statement[0]}"
                whereline += " IN ("
                whereline += ', '.join('?' for _ in statement[1])
                whereline += ') AND '
            whereline = whereline[:-5]
            # print(f"whereline {whereline}")
        # print(f"parameters = {parameters}")

        query = f"SELECT {column_line} from {table} {whereline}"

        cursor = self.execute_parameterised_query(query, parameters)
        records = self.get_records_array(cursor.fetchall())

        # print(f"sqlrecords {records}")
        return records

    def create_table(self, name, record_name="", column_names = [], column_types = [], column_placement=[], defaults=[]):
        """
        collects input of table name and column information
        builds a single query and 
        forwards to execute_query
        """

        # add the primary key
        column_names = ["id"] + column_names
        column_types = ["INTEGER PRIMARY KEY AUTOINCREMENT"] + column_types

        columns = []
        # enumerate over column names and types
        for index, column_name in enumerate(column_names):
            columns += [f"{column_name} {column_types[index]}"]

        # transform variables to string format
        valuetext = ',\n'.join(columns)

        # create variables text
        query = f"CREATE TABLE IF NOT EXISTS {name} (\n{valuetext}\n);"
        self.execute_query(query)

        tableobject = Table(
            db = self,
            name = name,
            record_name=record_name,
            column_names = column_names,
            column_types = column_types,
            column_placement=column_placement,
            defaults = [],
        )

        self.tables += [tableobject]
        return tableobject

    def create_records(self, table, column_names, valuepairs):
        
        # print(f"create records database with table {table}, columns {column_names} and valuepairs {valuepairs}")

        # transform column names to a string
        column_text = ', '.join(column_names)

        # create placeholders
        placeholders = ""
        parameters = ()
        for valuepair in valuepairs:
            valuepair_parameters = tuple(valuepair)
            parameters += valuepair_parameters
            valuepair_placeholders = '(' + ','.join('?' for value in valuepair) + '),\n'
            placeholders += valuepair_placeholders
        placeholders = placeholders[:-2]
        # print(f"placeholders = {placeholders}")
        # print(f"parameters = {parameters}")

        query = f"INSERT INTO {table}\n({column_text})\nVALUES\n{placeholders}\n;"
        self.execute_parameterised_query(query, parameters)

    def update_records(self, table, valuepairs = [["integer", 3], ["text",'test']], where=[["integer", 5]]):

        parameters = tuple()

        # create set_placeholders
        set_placeholders = ""
        for valuepair in valuepairs:
            parameters += tuple([valuepair[1]])
            set_placeholders += valuepair[0] + ' = ?, '
        set_placeholders = set_placeholders[:-2]
        # print(f"set_placeholders = {set_placeholders}")
        # print(f"parameters = {parameters}")

        # create where_placeholders
        where_placeholders = ""
        for statement in where:
            parameters += tuple(statement[1])
            where_placeholders += statement[0] + ' = ? AND '
        where_placeholders = where_placeholders[:-5]
        # print(f"where_placeholders = {where_placeholders}")
        # print(f"parameters = {parameters}")

        query = f"UPDATE {table} SET\n{set_placeholders}\nWHERE\n{where_placeholders}\n;"
        self.execute_parameterised_query(query, parameters)

    def get_records_array(self, sqlrecords):

        recordarrays = []

        for sqlrecord in sqlrecords:
            recordarray = []

            for value in sqlrecord:
                recordarray += [value]

            recordarrays += [recordarray]

        return recordarrays

    def get_max_row(self, table):

        cursor = self.execute_query(f"SELECT COUNT(id) FROM {table}")
        lastrow = cursor.fetchall()[0][0]

        return lastrow

    def get_max_columncontent(self, table, column):

        query = f"SELECT MAX({column}) FROM {table}"

        cursor = self.execute_query(query)
        max_columncontent = cursor.fetchall()
        if max_columncontent[0][0] == None:
            max_columncontent = [(0,)]

        return max_columncontent[0][0]

    def transform_boolean(self, value):
        if value == True:
            value = 1
        elif value == False:
            value = 0
        return value

class Table(object):
    def __init__(self, db, name, column_names, column_types, column_placement = [], defaults = [], record_name = ""):
        super().__init__()

        # set table and record names
        self.name = name
        if record_name == "":
            self.record_name = self.name[:-1]
        else:
            self.record_name = record_name

        # set column names and types
        self.column_names = column_names
        self.column_types = column_types

        self.set_defaults(defaults)
        self.set_column_placement(column_placement)

        # set connection to database
        self.db = db
        self.readAllRecords()

    @staticmethod
    def open_existing_table(database, tablename):
        
        metadata = database.read_column_metadata(tablename)
        column_order = metadata["column_order"]
        column_names = metadata["column_names"]
        column_types = database.read_column_types(tablename)

        # print(metadata)
        table = Table(database, tablename, column_names, column_types)
        table.readAllRecords()

        return table

    def set_defaults(self, defaults):
        if defaults != []:
            self.defaults = [-1] + defaults
        else:
            self.defaults = []

            self.defaults += [-1]
            for index, value in enumerate(self.column_types[1:]):
                ctype = value.split(' ', 1)[0].upper()

                if ctype == "INTEGER":
                    default = [0]
                elif ctype == "BOOL":
                    default = [False]
                elif ctype == "DATE":
                    default = [datetime.date.today]
                else:
                    default = [""]

                self.defaults += default

            # print(f"defaults set are {self.defaults}")
        
    def set_column_placement(self, column_placement):

        if column_placement != []:
            id_placement = [0,0,1,1]
            self.column_placement = [id_placement] + column_placement

        else:
            self.column_placement = []

            for index, value in enumerate(self.column_names):
                indexconfig = [index,0,1,1]
                self.column_placement += [indexconfig]

        # print(f"column_placement set are {self.column_placement}")

    def readColumnCount(self, includepk=True):
        """including private key column"""

        if includepk == True:
            return len(self.column_names)
        else:
            return len(self.column_names) - 1

    def readMaxRow(self):
        
        return self.db.get_max_row(table=self.name)

    def transform_sql_to_record(self, sqlrecords):

        # print(sqlrecords)

        records = []
        for record in sqlrecords:

            valuearray = []
            for value in record:
                valuearray += [value]

            recordobject = Record(self, valuearray)
            # print(f"recordarray: {recordobject.recordarray}")

            records += [recordobject]

        return records

    def readAllRecords(self):

        sqlrecords = self.db.read_records(table=self.name, columns=self.column_names, where="")

        self.records = self.transform_sql_to_record(sqlrecords)
        # print(f"{self.name} records retrieved: {self.records}")

        return self.records

    def readRecords(self, where=[]):

        # only do something with where if its given
        if where != []:
            if isinstance(where, int):
                where = [["id", [where]]]
            else:
                for statement in where:
                    # if column is a number, get the column name
                    if isinstance(statement[0], int):
                        statement[0] = self.column_names[statement[0]]

        # print(f"function {self.readRecords.__name__}: where = {where}")

        sqlrecords = self.db.read_records(table=self.name, columns=self.column_names, where=where)
        records = self.transform_sql_to_record(sqlrecords)

        return records

    def readForeignValues(self, column):
        """
        collects foreign values for a foreign key of this table
        checks if the given column is a foreign key
        checks what table and column this foreign key is pointing to
        checks the table and retrieves the column values
        creates recordarrays of these values
        returns the recordarrays
        """

        columnindex = self.column_names.index(column)
        split = self.column_types[columnindex].split(' ', 3)
        if len(split) != 3:
            return
        
        if split[1].upper() != "REFERENCES":
            return
        
        ftable = split[2].split('(',1)[0]
        print(f"foreign table {ftable}")

        # fcolumn = split[2].split('(',1)[1][:-1]
        # print(f"foreign column {fcolumn}")

        fcolumn_names = self.db.read_column_names(table=ftable)
        print(f"fcolumn names {fcolumn_names}")

        sqltable = self.db.read_records(table=ftable, columns = [])
        print(f"all table records {sqltable}")

        # by default just assuming we are pointing to primary key in first column and third column contains something meaningfull
        fcolumns = [fcolumn_names[0], fcolumn_names[2]]
        sqlcolumns = self.db.read_records(table=ftable, columns = fcolumns)

        print(f"all table records with foreign key column {sqlcolumns}")

        return sqlcolumns

    def createTabledepreciated(self):
        pass

        #     """
        #     gathers the table name and the column info and then forwards them to
        #     create_table method of the Database object
        #     """

        #     # columns = [f"id INTEGER PRIMARY KEY AUTOINCREMENT", f"ordering INTEGER"]
        #     columns = []

        #     # get column info without primary key
        #     column_names = self.column_names
        #     column_types = self.column_types

        #     # print(columns)

        #     # print(f"query create table {columns}")
        #     self.db.create_table(name=self.name, column_names=column_names, column_types=column_types)

    def create_draft_record(self):

        record = Record(self, self.defaults)

        return record

    def createRecord(self, values):
        """
        collects an array of values for a single record
        package it in an array of 1 record and then
        forwards it to the create_records method of Database

        It returns the last row as a Record object
        """
        # print(f"createRecord self.column_names {self.column_names}")
        self.db.create_records(table=self.name, column_names=self.column_names[1:], valuepairs=[values])

        records = self.readAllRecords()

        newrows_last = self.db.get_max_row(self.name)

        for record in records:
            if record.primarykey == newrows_last:
                recordobject = record
                break

        # print(f"Record created: {recordobject.recordarray}")

        return recordobject

    def createRecords(self, records):

        # print(f"createRecords {records}")

        if len(records) == 1:
            records = [self.createRecord(records[0])]
            return records

        else:

            newrows_first = self.db.get_max_row(self.name) + 1
            
            self.db.create_records(table=self.name, column_names=self.column_names[1:], valuepairs=records)

            records = self.readAllRecords()

            recordobjects = []
            for record in records:
                if record.primarykey >= newrows_first:
                    recordobjects += [record]

            for record in recordobjects:
                # print(f"Records created: {record.recordarray}")
                pass

            return recordobjects

    def deleteRecords(self, records):

        self.db.delete_records(self, records)

    def updateRecordbyID(self, rowid, valuepairs):

        # get a wherestatement from just the rowid
        where = [["id",[rowid]]]

        # get record before updating
        record_before = self.readRecords(where=where)[0]
        # print(f"record before = {record_before}")

        # update the record
        # print(valuepairs)
        self.db.update_records(table=self.name, valuepairs=valuepairs, where=where)

        # get record after updating
        record_after = self.readRecords(where=where)[0]
        # print(f"record after = {record_after}")

        if record_before.primarykey != record_after.primarykey:
            # print(f"Update messed up the table!!!")
            return

        record_object = record_after
        if record_before.values != record_after.values:
            # print(f"updated record {record_object.recordarray}")
            pass
        else:
            print(f"update record was not necessary")

        return record_object

    def updateRecords(self, valuepairs, where):

        table_before = self.readRecords()
        # print(f"table before = {table_before}")

        # # print(f"valueparis = {valuepairs}")
        # for valuearray in valuepairs:
        #     valuearray[1] = self.transform_boolean(valuearray[1])
        # # print(f"valuepairs = {valuepairs}")

        if isinstance(where, int):
            where = [["id", [where]]]
        else:
            if where != []:
                for statement in where:
                    # if column is a number, get the column name
                    if isinstance(statement[0], int):
                        statement[0] = self.column_names[statement[0]]

        # print(f"where {where}, valuepairs {valuepairs}")
        self.db.update_records(table=self.name, valuepairs=valuepairs, where=where)
                    
        table_after = self.readRecords()
        # print(f"table after = {table_after}")

        record_objects = []
        for index, record in enumerate(table_after):
            if table_before[index].primarykey != record.primarykey:
                print(f"Update messed up the table!!!")
                return
            if table_before[index].values != record.values:
                record_objects += [table_after[index]]
                for row in record_objects:
                    # print(f"updated row {row.recordarray}")
                    pass
                return record_objects

    # def transform_boolean(self, value):
    #     if value == True:
    #         value = 1
    #     elif value == False:
    #         value = 0
    #     return value

class Record(object):
    def __init__(self, table, recordarray):
        super().__init__()

        """
        Primarykey: 
        primary key of this record

        Recordarray: 
        array of values
        including the primary key

        Recordpairs: 
        array of column - value pairs
        including the primary key column
        
        Values: 
        array of all values
        excluding the primary key
        
        Valuepairs: 
        array of column - value pairs
        excluding the primary key column

        With Record.get_dict() command you get the record in dictionary format where
        you can search easily based on column name
        """

        self.table = table
        self.primarykey = recordarray[0]
        self.name = ""

        self.recordarray = recordarray
        self.values = recordarray[1:]
        self.setrecordpairs()
        self.setvaluepairs()

    def setrecordpairs(self):
        self.recordpairs = []
        # print(f"Record setting column names {self.table.column_names}")
        # print(f"Record setting record array {self.recordarray}")
        for index, name in enumerate(self.table.column_names):
            
            recordpair = [name, self.recordarray[index]]
            self.recordpairs += [recordpair]

            if name == "name":
                self.name = self.recordarray[index]
        # print(f"set recordpairs {self.recordpairs}")

    def setvaluepairs(self):
        self.valuepairs = []
        for index, name in enumerate(self.table.column_names[1:]):
            valuepair = [name, self.recordarray[1:][index]]
            self.valuepairs += [valuepair]
        # print(f"set valuepairs {self.valuepairs}")


def print_records(records):
    for record in records:
        print(f"-table: {record.table}, primarykey: {record.primarykey}, recordpairs: {record.recordpairs}")

if __name__ == "__main__":

    filename = "backup"

    db = Database(path="", filename=filename)
    db.delete_database()
    print(f"deleted database {filename}")

    filename = "science"

    db = Database(path="", filename=filename)
    db.delete_database()
    print(f"deleted database {filename}")

    db = Database(filename=filename)

    sciencetbl = db.create_table(
        name="scientists",
        column_names = ["ordering", "name", "age", "nobelprizewinner"],
        column_types = ["INTEGER", "Text", "Integer", "Bool"],
    )
    print(f"read table names: {db.read_table_names()}")

    values = [
        [1, "Hawking", 68, True],
        [2, "Edison's child said \"Apple!\"", 20, True],
    ]
    records = sciencetbl.createRecords(values)
    print(f"creating initial records")
    print_records(records)
    
    #test functions of table
    print(f"read column names: {db.read_column_names(sciencetbl.name)}")
    print(f"read column types: {db.read_column_types(sciencetbl.name)}")
    print(f"read column metadata: {db.read_column_metadata(sciencetbl.name)}")

    values = [3, "Einstein", 100, False]
    record = sciencetbl.createRecord(values)
    print(f"create single record")
    print_records([record])

    values = [
        [4, "Rosenburg", 78, False],
        [5, "Neil dGrasse Tyson", 57, True],
    ]
    records = sciencetbl.createRecords(values)
    print(f"create multiple records")
    print_records(records)

    # columns = ["name", "age"]
    # records = sciencetbl.readRecords(columns=columns)
    # print(f"read only name and age columns for all records")
    # print_records(records)

    where = [["nobelprizewinner", [True]]]
    records = sciencetbl.readRecords(where=where)
    print(f"read where")
    print_records(records)

    valuepairs = [["nobelprizewinner", False]]
    where = [["nobelprizewinner", [True]], ["name", ["Hawking"]]]
    records = sciencetbl.updateRecords(valuepairs=valuepairs, where=where)
    print(f"update true to false")
    print_records(records)

    valuepairs = [["name", "Neil de'Grasse Tyson"], ["age", 40]]
    rowid = 5
    record = sciencetbl.updateRecordbyID(valuepairs = valuepairs, rowid=rowid)
    print(f"update record 'id = 5'")
    print_records([record])

    records = sciencetbl.readRecords()
    print(f"read all records")
    print_records(records)

    reltbl = db.create_table(
        name = "relationships",
        column_names=["charid1", "charid2", "description"],
        column_types=["INTEGER REFERENCES scientists(id)", "INTEGER REFERENCES scientists(id)", "TEXT"],
    )

    reltbl.db.read_column_metadata(reltbl.name)

    values = [1, 2, "hawking and edison"]
    record = reltbl.createRecord(values)
    print(f"create single record")
    print_records([record])

    records = reltbl.readRecords()
    print(f"read all records")
    print_records(records)

    records = reltbl.readForeignValues('charid1')

    db.saveas_database(filename="backup")
    db.close_database()

    filename = "science"

    db = Database(filename=filename)

    teachertbl = db.create_table(
        name="teachers",
        column_names = ["ordering", "name", "age", "active"],
        column_types = ["INTEGER", "Text", "Integer", "Bool"],
    )

    db.delete_table(teachertbl)

    sciencetbl = db.get_table("scientists")

    where = [["nobelprizewinner", [True]]]
    records = sciencetbl.readRecords(where=where)

    sciencetbl.deleteRecords(records)

    for table in db.tables:
        print(f"printing for table: {table.name}")
        print_records(table.records)