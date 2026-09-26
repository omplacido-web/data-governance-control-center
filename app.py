# Import Streamlit.
# Streamlit creates the web application.
import streamlit as st


# Import the function that creates our database tables.
from database import create_tables


# Import the functions used by the Data Owner Registry.
from owner_registry import (
    save_owner_registry,
    get_registry
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

# Configure the application page.
st.set_page_config(

    # Name displayed in the browser tab.
    page_title="Data Governance Control Center",

    # Icon displayed in the browser tab.
    page_icon="🛡️",

    # Use the full width of the browser.
    layout="wide"
)


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

# Create the database tables when the application starts.
create_tables()


# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================

# Display the portal name in the sidebar.
st.sidebar.title("🛡️ Governance Portal")


# Create the navigation menu.
page = st.sidebar.radio(

    # Label above the menu.
    "Navigate to:",

    # Pages available in our Control Center.
    [
        "Dashboard",
        "Data Owner Registry",
        "Data Catalog",
        "Classification Engine",
        "CDE Engine",
        "Policies & Standards"
    ]
)


# ==========================================================
# DASHBOARD
# ==========================================================

# Display the Dashboard page.
if page == "Dashboard":

    # Display the main title.
    st.title("🛡️ Data Governance Control Center")

    # Display a short description.
    st.write(
        "Centralized workspace for managing "
        "data governance information."
    )

    # Display an introduction.
    st.info(
        "Use the navigation menu on the left "
        "to access the Governance Control Center."
    )

    # Display the current modules.
    st.subheader("Governance Modules")

    # Create three columns.
    column1, column2, column3 = st.columns(3)

    # First module.
    with column1:

        st.metric(
            "Data Owner Registry",
            "Available"
        )

    # Second module.
    with column2:

        st.metric(
            "Classification Engine",
            "Coming Soon"
        )

    # Third module.
    with column3:

        st.metric(
            "CDE Engine",
            "Coming Soon"
        )


# ==========================================================
# DATA OWNER REGISTRY
# ==========================================================

# Display the Data Owner Registry page.
elif page == "Data Owner Registry":

    # Display the page title.
    st.title("👥 Data Owner Registry")

    # Explain the purpose of the registry.
    st.write(
        "Register and manage governance accountability "
        "for each data entity."
    )


    # ======================================================
    # ADD NEW DATA ENTITY
    # ======================================================

    # Create an expandable section for adding records.
    with st.expander(
        "➕ Add New Data Entity",
        expanded=True
    ):

        # --------------------------------------------------
        # ENTITY INFORMATION
        # --------------------------------------------------

        st.subheader("📋 Entity Information")

        # Create two columns.
        column1, column2 = st.columns(2)


        # Left column.
        with column1:

            # Entity ID.
            entity_id = st.text_input(
                "Entity ID *",
                placeholder="Example: ENT-001"
            )

            # Entity Name.
            entity_name = st.text_input(
                "Entity Name *",
                placeholder="Example: Customer"
            )

            # Data Domain.
            data_domain = st.text_input(
                "Data Domain",
                placeholder="Example: Customer"
            )


        # Right column.
        with column2:

            # Data Classification.
            data_classification = st.selectbox(

                "Data Classification",

                [
                    "Not Classified",
                    "Public",
                    "Internal",
                    "Confidential",
                    "Restricted"
                ]
            )


        # Description.
        description = st.text_area(
            "Description",
            placeholder="Describe the data entity."
        )


        # ==================================================
        # DATA OWNER
        # ==================================================

        st.subheader("👤 Data Owner")

        # Create two columns.
        column1, column2 = st.columns(2)


        # Division Head information.
        with column1:

            data_owner_division_head = st.text_input(
                "Data Owner Name (Division Head)"
            )

            data_owner_division = st.text_input(
                "Data Owner Division"
            )


        # Department Head information.
        with column2:

            data_owner_department_head = st.text_input(
                "Data Owner Name (Department Head)"
            )

            data_owner_department = st.text_input(
                "Data Owner Department"
            )


        # ==================================================
        # NUMBER OF DATA STEWARDS
        # ==================================================

        st.subheader("📊 Data Stewards")

        # Let the user choose how many stewards are needed.
        number_of_stewards = st.selectbox(

            "Number of Data Stewards",

            [1, 2, 3],

            index=0
        )


        # --------------------------------------------------
        # DATA STEWARD 1
        # --------------------------------------------------

        st.markdown("### Data Steward 1")

        column1, column2 = st.columns(2)


        with column1:

            data_steward_1_division_head = st.text_input(
                "Data Steward 1 Name (Division Head)"
            )

            data_steward_1_division = st.text_input(
                "Data Steward 1 Division"
            )


        with column2:

            data_steward_1_department_head = st.text_input(
                "Data Steward 1 Name (Department Head)"
            )

            data_steward_1_department = st.text_input(
                "Data Steward 1 Department"
            )


        # --------------------------------------------------
        # DATA STEWARD 2
        # --------------------------------------------------

        # Create empty values first.
        data_steward_2_division_head = ""
        data_steward_2_division = ""
        data_steward_2_department_head = ""
        data_steward_2_department = ""


        # Only display Steward 2 if selected.
        if number_of_stewards >= 2:

            st.markdown("### Data Steward 2")

            column1, column2 = st.columns(2)


            with column1:

                data_steward_2_division_head = st.text_input(
                    "Data Steward 2 Name (Division Head)"
                )

                data_steward_2_division = st.text_input(
                    "Data Steward 2 Division"
                )


            with column2:

                data_steward_2_department_head = st.text_input(
                    "Data Steward 2 Name (Department Head)"
                )

                data_steward_2_department = st.text_input(
                    "Data Steward 2 Department"
                )


        # --------------------------------------------------
        # DATA STEWARD 3
        # --------------------------------------------------

        # Create empty values first.
        data_steward_3_division_head = ""
        data_steward_3_division = ""
        data_steward_3_department_head = ""
        data_steward_3_department = ""


        # Only display Steward 3 if selected.
        if number_of_stewards >= 3:

            st.markdown("### Data Steward 3")

            column1, column2 = st.columns(2)


            with column1:

                data_steward_3_division_head = st.text_input(
                    "Data Steward 3 Name (Division Head)"
                )

                data_steward_3_division = st.text_input(
                    "Data Steward 3 Division"
                )


            with column2:

                data_steward_3_department_head = st.text_input(
                    "Data Steward 3 Name (Department Head)"
                )

                data_steward_3_department = st.text_input(
                    "Data Steward 3 Department"
                )


        # ==================================================
        # NUMBER OF DATA CUSTODIANS
        # ==================================================

        st.subheader("💻 Data Custodians")

        # Let the user choose how many custodians are needed.
        number_of_custodians = st.selectbox(

            "Number of Data Custodians",

            [1, 2, 3],

            index=0
        )


        # --------------------------------------------------
        # DATA CUSTODIAN 1
        # --------------------------------------------------

        st.markdown("### Data Custodian 1")

        column1, column2 = st.columns(2)


        with column1:

            data_custodian_1_division_head = st.text_input(
                "Data Custodian 1 Name (Division Head)"
            )

            data_custodian_1_division = st.text_input(
                "Data Custodian 1 Division"
            )


        with column2:

            data_custodian_1_department_head = st.text_input(
                "Data Custodian 1 Name (Department Head)"
            )

            data_custodian_1_department = st.text_input(
                "Data Custodian 1 Department"
            )


        # --------------------------------------------------
        # DATA CUSTODIAN 2
        # --------------------------------------------------

        # Create empty values first.
        data_custodian_2_division_head = ""
        data_custodian_2_division = ""
        data_custodian_2_department_head = ""
        data_custodian_2_department = ""


        # Only display Custodian 2 if selected.
        if number_of_custodians >= 2:

            st.markdown("### Data Custodian 2")

            column1, column2 = st.columns(2)


            with column1:

                data_custodian_2_division_head = st.text_input(
                    "Data Custodian 2 Name (Division Head)"
                )

                data_custodian_2_division = st.text_input(
                    "Data Custodian 2 Division"
                )


            with column2:

                data_custodian_2_department_head = st.text_input(
                    "Data Custodian 2 Name (Department Head)"
                )

                data_custodian_2_department = st.text_input(
                    "Data Custodian 2 Department"
                )


        # --------------------------------------------------
        # DATA CUSTODIAN 3
        # --------------------------------------------------

        # Create empty values first.
        data_custodian_3_division_head = ""
        data_custodian_3_division = ""
        data_custodian_3_department_head = ""
        data_custodian_3_department = ""


        # Only display Custodian 3 if selected.
        if number_of_custodians >= 3:

            st.markdown("### Data Custodian 3")

            column1, column2 = st.columns(2)


            with column1:

                data_custodian_3_division_head = st.text_input(
                    "Data Custodian 3 Name (Division Head)"
                )

                data_custodian_3_division = st.text_input(
                    "Data Custodian 3 Division"
                )


            with column2:

                data_custodian_3_department_head = st.text_input(
                    "Data Custodian 3 Name (Department Head)"
                )

                data_custodian_3_department = st.text_input(
                    "Data Custodian 3 Department"
                )


        # ==================================================
        # SAVE RECORD
        # ==================================================

        st.divider()

        # Create the Save button.
        if st.button(
            "💾 Save Data Owner Registry",
            type="primary"
        ):

            # Check Entity ID.
            if entity_id == "":

                st.error(
                    "Please enter an Entity ID."
                )


            # Check Entity Name.
            elif entity_name == "":

                st.error(
                    "Please enter an Entity Name."
                )


            else:

                # Save the complete governance record.
                save_owner_registry(

                    # Entity information.
                    entity_id,
                    entity_name,
                    description,
                    data_domain,
                    data_classification,

                    # Data Owner.
                    data_owner_division_head,
                    data_owner_division,
                    data_owner_department_head,
                    data_owner_department,

                    # Data Steward 1.
                    data_steward_1_division_head,
                    data_steward_1_division,
                    data_steward_1_department_head,
                    data_steward_1_department,

                    # Data Steward 2.
                    data_steward_2_division_head,
                    data_steward_2_division,
                    data_steward_2_department_head,
                    data_steward_2_department,

                    # Data Steward 3.
                    data_steward_3_division_head,
                    data_steward_3_division,
                    data_steward_3_department_head,
                    data_steward_3_department,

                    # Data Custodian 1.
                    data_custodian_1_division_head,
                    data_custodian_1_division,
                    data_custodian_1_department_head,
                    data_custodian_1_department,

                    # Data Custodian 2.
                    data_custodian_2_division_head,
                    data_custodian_2_division,
                    data_custodian_2_department_head,
                    data_custodian_2_department,

                    # Data Custodian 3.
                    data_custodian_3_division_head,
                    data_custodian_3_division,
                    data_custodian_3_department_head,
                    data_custodian_3_department
                )


                # Display a success message.
                st.success(
                    "Data Owner Registry saved successfully!"
                )


    # ======================================================
    # SEARCH AND FILTER
    # ======================================================

    st.divider()

    st.subheader("🔎 Search & Filter Registry")


    # Retrieve all records.
    registry = get_registry()


    # Check whether records exist.
    if len(registry) > 0:

        # Create three columns.
        column1, column2, column3 = st.columns(3)


        # --------------------------------------------------
        # SEARCH
        # --------------------------------------------------

        with column1:

            search_text = st.text_input(

                "Search Entity",

                placeholder="Search by ID or name"
            )


        # --------------------------------------------------
        # DOMAIN FILTER
        # --------------------------------------------------

        domains = sorted(

            registry["Data Domain"]
            .dropna()
            .unique()
            .tolist()
        )


        with column2:

            selected_domain = st.selectbox(

                "Data Domain",

                ["All"] + domains
            )


        # --------------------------------------------------
        # CLASSIFICATION FILTER
        # --------------------------------------------------

        classifications = sorted(

            registry["Data Classification"]
            .dropna()
            .unique()
            .tolist()
        )


        with column3:

            selected_classification = st.selectbox(

                "Data Classification",

                ["All"] + classifications
            )


        # Start with all records.
        filtered_registry = registry.copy()


        # --------------------------------------------------
        # APPLY SEARCH
        # --------------------------------------------------

        if search_text:

            # Convert search text to lowercase.
            search_text = search_text.lower()


            # Search Entity ID or Entity Name.
            filtered_registry = filtered_registry[

                filtered_registry["Entity ID"]
                .str.lower()
                .str.contains(
                    search_text,
                    na=False
                )

                |

                filtered_registry["Entity Name"]
                .str.lower()
                .str.contains(
                    search_text,
                    na=False
                )
            ]


        # --------------------------------------------------
        # APPLY DOMAIN FILTER
        # --------------------------------------------------

        if selected_domain != "All":

            filtered_registry = filtered_registry[

                filtered_registry["Data Domain"]
                == selected_domain
            ]


        # --------------------------------------------------
        # APPLY CLASSIFICATION FILTER
        # --------------------------------------------------

        if selected_classification != "All":

            filtered_registry = filtered_registry[

                filtered_registry["Data Classification"]
                == selected_classification
            ]


        # --------------------------------------------------
        # DISPLAY REGISTRY
        # --------------------------------------------------

        st.subheader("📊 Registered Data Entities")


        # Show record count.
        st.write(

            f"Showing {len(filtered_registry)} "
            f"of {len(registry)} registered entities."
        )


        # Display the registry.
        st.dataframe(

            filtered_registry,

            use_container_width=True,

            hide_index=True
        )


        # --------------------------------------------------
        # DOWNLOAD CSV
        # --------------------------------------------------

        # Convert the registry to CSV.
        csv_data = filtered_registry.to_csv(
            index=False
        )


        # Create the download button.
        st.download_button(

            label="📥 Download Registry as CSV",

            data=csv_data,

            file_name="data_owner_registry.csv",

            mime="text/csv"
        )


    else:

        # Display a message when there are no records.
        st.info(

            "No data entities have been registered yet. "
            "Use the form above to add your first entity."
        )
# ==========================================================
# DATA CATALOG
# ==========================================================

elif page == "Data Catalog":

    # Display the page title.
    st.title("📚 Data Catalog")

    # Explain the future module.
    st.info(
        "The Data Catalog will allow users to "
        "browse and understand registered data assets."
    )


# ==========================================================
# CLASSIFICATION ENGINE
# ==========================================================

elif page == "Classification Engine":

    # Display the page title.
    st.title("🔐 Classification Engine")

    # Explain the future module.
    st.info(
        "The Classification Engine will analyze "
        "data and suggest an appropriate classification."
    )


# ==========================================================
# CDE ENGINE
# ==========================================================

elif page == "CDE Engine":

    # Display the page title.
    st.title("⭐ CDE Engine")

    # Explain the future module.
    st.info(
        "The CDE Engine will identify and manage "
        "Critical Data Elements."
    )


# ==========================================================
# POLICIES AND STANDARDS
# ==========================================================

elif page == "Policies & Standards":

    # Display the page title.
    st.title("📄 Policies & Standards")

    # Explain the future module.
    st.info(
        "This section will contain Data Governance "
        "policies, standards, and procedures."
    )