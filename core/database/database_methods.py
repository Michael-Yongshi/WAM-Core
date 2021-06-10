import os
from sqlitemanager.database import (
    Database,
    Table,
    Record,
)

def get_database_records(tablename):

    # connect_to_database
    database_path = os.path.join(os.path.dirname(__file__))
    database_filename = "database"

    database = Database(filename=database_filename, path=database_path)
    print(f"tables {database.get_tables()}")

    table = database.get_table(tablename=tablename)
    records = table.readAllRecords()

    return records

if __name__ == "__main__":

    warbanddata = get_database_records("warbands")
    print(warbanddata[0].valuepairs)