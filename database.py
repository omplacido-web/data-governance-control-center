# Import SQLite.
# SQLite is the database that will store our governance information.
import sqlite3


# This is the name of our database file.
DATABASE_NAME = "governance.db"


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

# This function connects Python to our database.
def get_connection():

    # Open the governance database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Return the database connection.
    return connection


# ==========================================================
# CREATE DATA OWNER REGISTRY TABLE
# ==========================================================

# This function creates our Data Owner Registry table.
def create_tables():

    # Connect to the database.
    connection = get_connection()

    # Create a cursor.
    # The cursor allows Python to execute SQL commands.
    cursor = connection.cursor()

    # Create the Data Owner Registry table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data_owner_registry (

            -- Internal database ID.
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            -- =================================================
            -- ENTITY INFORMATION
            -- =================================================

            entity_id TEXT NOT NULL,

            entity_name TEXT NOT NULL,

            description TEXT,

            data_domain TEXT,

            data_classification TEXT,


            -- =================================================
            -- DATA OWNER
            -- =================================================

            data_owner_division_head TEXT,

            data_owner_division TEXT,

            data_owner_department_head TEXT,

            data_owner_department TEXT,


            -- =================================================
            -- DATA STEWARD 1
            -- =================================================

            data_steward_1_division_head TEXT,

            data_steward_1_division TEXT,

            data_steward_1_department_head TEXT,

            data_steward_1_department TEXT,


            -- =================================================
            -- DATA STEWARD 2
            -- =================================================

            data_steward_2_division_head TEXT,

            data_steward_2_division TEXT,

            data_steward_2_department_head TEXT,

            data_steward_2_department TEXT,


            -- =================================================
            -- DATA STEWARD 3
            -- =================================================

            data_steward_3_division_head TEXT,

            data_steward_3_division TEXT,

            data_steward_3_department_head TEXT,

            data_steward_3_department TEXT,


            -- =================================================
            -- DATA CUSTODIAN 1
            -- =================================================

            data_custodian_1_division_head TEXT,

            data_custodian_1_division TEXT,

            data_custodian_1_department_head TEXT,

            data_custodian_1_department TEXT,


            -- =================================================
            -- DATA CUSTODIAN 2
            -- =================================================

            data_custodian_2_division_head TEXT,

            data_custodian_2_division TEXT,

            data_custodian_2_department_head TEXT,

            data_custodian_2_department TEXT,


            -- =================================================
            -- DATA CUSTODIAN 3
            -- =================================================

            data_custodian_3_division_head TEXT,

            data_custodian_3_division TEXT,

            data_custodian_3_department_head TEXT,

            data_custodian_3_department TEXT

        )
    """)


    # Save the table.
    connection.commit()


    # Close the database connection.
    connection.close()