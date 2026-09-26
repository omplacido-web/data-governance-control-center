# Import Pandas.
# Pandas helps us work with and display database records.
import pandas as pd


# Import the database connection function.
from database import get_connection


# ==========================================================
# SAVE DATA OWNER REGISTRY RECORD
# ==========================================================

# This function saves a new data governance record.
# ==========================================================
# SAVE DATA OWNER REGISTRY RECORD
# ==========================================================

def save_owner_registry(
    entity_id,
    entity_name,
    description,
    data_domain,
    data_classification,

    data_owner_division_head,
    data_owner_division,
    data_owner_department_head,
    data_owner_department,

    data_steward_1_division_head,
    data_steward_1_division,
    data_steward_1_department_head,
    data_steward_1_department,

    data_steward_2_division_head,
    data_steward_2_division,
    data_steward_2_department_head,
    data_steward_2_department,

    data_steward_3_division_head,
    data_steward_3_division,
    data_steward_3_department_head,
    data_steward_3_department,

    data_custodian_1_division_head,
    data_custodian_1_division,
    data_custodian_1_department_head,
    data_custodian_1_department,

    data_custodian_2_division_head,
    data_custodian_2_division,
    data_custodian_2_department_head,
    data_custodian_2_department,

    data_custodian_3_division_head,
    data_custodian_3_division,
    data_custodian_3_department_head,
    data_custodian_3_department
):

    # Connect to the database.
    connection = get_connection()

    # Create a cursor.
    cursor = connection.cursor()

    # Insert the registry record.
    cursor.execute(
        """
        INSERT INTO data_owner_registry (
            entity_id,
            entity_name,
            description,
            data_domain,
            data_classification,

            data_owner_division_head,
            data_owner_division,
            data_owner_department_head,
            data_owner_department,

            data_steward_1_division_head,
            data_steward_1_division,
            data_steward_1_department_head,
            data_steward_1_department,

            data_steward_2_division_head,
            data_steward_2_division,
            data_steward_2_department_head,
            data_steward_2_department,

            data_steward_3_division_head,
            data_steward_3_division,
            data_steward_3_department_head,
            data_steward_3_department,

            data_custodian_1_division_head,
            data_custodian_1_division,
            data_custodian_1_department_head,
            data_custodian_1_department,

            data_custodian_2_division_head,
            data_custodian_2_division,
            data_custodian_2_department_head,
            data_custodian_2_department,

            data_custodian_3_division_head,
            data_custodian_3_division,
            data_custodian_3_department_head,
            data_custodian_3_department
        )

        VALUES (
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?, ?
        )
        """,
        (
            entity_id,
            entity_name,
            description,
            data_domain,
            data_classification,

            data_owner_division_head,
            data_owner_division,
            data_owner_department_head,
            data_owner_department,

            data_steward_1_division_head,
            data_steward_1_division,
            data_steward_1_department_head,
            data_steward_1_department,

            data_steward_2_division_head,
            data_steward_2_division,
            data_steward_2_department_head,
            data_steward_2_department,

            data_steward_3_division_head,
            data_steward_3_division,
            data_steward_3_department_head,
            data_steward_3_department,

            data_custodian_1_division_head,
            data_custodian_1_division,
            data_custodian_1_department_head,
            data_custodian_1_department,

            data_custodian_2_division_head,
            data_custodian_2_division,
            data_custodian_2_department_head,
            data_custodian_2_department,

            data_custodian_3_division_head,
            data_custodian_3_division,
            data_custodian_3_department_head,
            data_custodian_3_department
        )
    )

    # Save the record.
    connection.commit()

    # Close the database connection.
    connection.close()
# ==========================================================
# GET DATA OWNER REGISTRY
# ==========================================================

# This function retrieves all registered entities.
def get_registry():

    # Connect to the database.
    connection = get_connection()

    # Create a cursor.
    cursor = connection.cursor()


    # Retrieve all governance records.
    cursor.execute("""
        SELECT

            id,

            entity_id,
            entity_name,
            description,
            data_domain,
            data_classification,

            data_owner_division_head,
            data_owner_division,
            data_owner_department_head,
            data_owner_department,

            data_steward_1_division_head,
            data_steward_1_division,
            data_steward_1_department_head,
            data_steward_1_department,

            data_steward_2_division_head,
            data_steward_2_division,
            data_steward_2_department_head,
            data_steward_2_department,

            data_steward_3_division_head,
            data_steward_3_division,
            data_steward_3_department_head,
            data_steward_3_department,

            data_custodian_1_division_head,
            data_custodian_1_division,
            data_custodian_1_department_head,
            data_custodian_1_department,

            data_custodian_2_division_head,
            data_custodian_2_division,
            data_custodian_2_department_head,
            data_custodian_2_department,

            data_custodian_3_division_head,
            data_custodian_3_division,
            data_custodian_3_department_head,
            data_custodian_3_department

        FROM data_owner_registry

        ORDER BY entity_name
    """)


    # Retrieve all records.
    records = cursor.fetchall()


    # Close the database connection.
    connection.close()


    # ======================================================
    # FRIENDLY COLUMN NAMES
    # ======================================================

    # These are the names users will see in Streamlit.
    columns = [

        "ID",

        "Entity ID",
        "Entity Name",
        "Description",
        "Data Domain",
        "Data Classification",

        "Data Owner Name (Division Head)",
        "Data Owner Division",
        "Data Owner Name (Department Head)",
        "Data Owner Department",

        "Data Steward 1 Name (Division Head)",
        "Data Steward 1 Division",
        "Data Steward 1 Name (Department Head)",
        "Data Steward 1 Department",

        "Data Steward 2 Name (Division Head)",
        "Data Steward 2 Division",
        "Data Steward 2 Name (Department Head)",
        "Data Steward 2 Department",

        "Data Steward 3 Name (Division Head)",
        "Data Steward 3 Division",
        "Data Steward 3 Name (Department Head)",
        "Data Steward 3 Department",

        "Data Custodian 1 Name (Division Head)",
        "Data Custodian 1 Division",
        "Data Custodian 1 Name (Department Head)",
        "Data Custodian 1 Department",

        "Data Custodian 2 Name (Division Head)",
        "Data Custodian 2 Division",
        "Data Custodian 2 Name (Department Head)",
        "Data Custodian 2 Department",

        "Data Custodian 3 Name (Division Head)",
        "Data Custodian 3 Division",
        "Data Custodian 3 Name (Department Head)",
        "Data Custodian 3 Department"
    ]


    # Convert database records into a Pandas DataFrame.
    registry = pd.DataFrame(
        records,
        columns=columns
    )


    # Return the registry.
    return registry