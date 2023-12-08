# Importing the Necessary libraries
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import mysql.connector
from git import Repo
import json
import locale


# Cloning Data from Github Repository
def github_cloning():
    Repo.clone_from("https://github.com/PhonePe/pulse.git", r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse")


# Setup Connection with MYSQL Database
my_database = mysql.connector.connect(host = "localhost",
                                      user = "root",
                                      password = "Kumar@08",
                                      database = "phonepe_db")
my_cursor = my_database.cursor()


# Getting Aggregated Transaction Data
def getting_agg_transaction():
    path = r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse\data\aggregated\transaction\country\india\state"
    state_list = os.listdir(path)
    agg_trans_data = {"State": [], "Year": [], "Quarter": [], "Transaction_type": [], "Transaction_count": [],
                      "Transaction_amount": []}

    for state in state_list:
        path1 = path + "\\" + state
        year_list = os.listdir(path1)

        for year in year_list:
            path2 = path1 + "\\" + year
            quarter_list = os.listdir(path2)

            for quarter in quarter_list:
                path3 = path2 + "\\" + quarter
                data = open(path3, "r")
                d = json.load(data)

                for i in d["data"]["transactionData"]:
                    agg_trans_data["Transaction_type"].append(i["name"])
                    agg_trans_data["Transaction_count"].append(i["paymentInstruments"][0]["count"])
                    agg_trans_data["Transaction_amount"].append(i["paymentInstruments"][0]["amount"])
                    agg_trans_data["State"].append(state)
                    agg_trans_data["Year"].append(year)
                    agg_trans_data["Quarter"].append(quarter.strip(".json"))

    agg_transaction = pd.DataFrame(agg_trans_data)
    agg_transaction["State"] = agg_transaction["State"].astype("str").str.replace("-", " ").str.title()
    return agg_transaction


# Getting Aggregated User Data
def getting_agg_user():
    path = r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse\data\aggregated\user\country\india\state"
    state_list = os.listdir(path)
    agg_user_data = {"State": [], "Year": [], "Quarter": [], "Registered_users": [], "App_opens": []}

    for state in state_list:
        path1 = path + "\\" + state
        year_list = os.listdir(path1)

        for year in year_list:
            path2 = path1 + "\\" + year
            quarter_list = os.listdir(path2)

            for quarter in quarter_list:
                path3 = path2 + "\\" + quarter
                data = open(path3, "r")
                d = json.load(data)

                agg_user_data["Registered_users"].append(d["data"]["aggregated"]["registeredUsers"])
                agg_user_data["App_opens"].append(d["data"]["aggregated"]["appOpens"])
                agg_user_data["State"].append(state)
                agg_user_data["Year"].append(year)
                agg_user_data["Quarter"].append(quarter.strip(".json"))

    agg_user = pd.DataFrame(agg_user_data)
    agg_user["State"] = agg_user["State"].astype("str").str.replace("-", " ").str.title()
    return agg_user


# Getting Map Transaction Data
def getting_map_transaction():
    path = r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse\data\map\transaction\hover\country\india\state"
    state_list = os.listdir(path)
    map_trans_data = {"State": [], "Year": [], "Quarter": [], "District": [], "Transaction_count": [],
                      "Transaction_amount": []}

    for state in state_list:
        path1 = path + "\\" + state
        year_list = os.listdir(path1)

        for year in year_list:
            path2 = path1 + "\\" + year
            quarter_list = os.listdir(path2)

            for quarter in quarter_list:
                path3 = path2 + "\\" + quarter
                data = open(path3, "r")
                d = json.load(data)

                for i in d["data"]["hoverDataList"]:
                    map_trans_data["District"].append(i["name"])
                    map_trans_data["Transaction_count"].append(i["metric"][0]["count"])
                    map_trans_data["Transaction_amount"].append(i["metric"][0]["amount"])
                    map_trans_data["State"].append(state)
                    map_trans_data["Year"].append(year)
                    map_trans_data["Quarter"].append(quarter.strip(".json"))

    map_transaction = pd.DataFrame(map_trans_data)
    map_transaction["State"] = map_transaction["State"].str.replace("-", " ").str.title()
    return map_transaction


# Getting Map User Data
def getting_map_user():
    path = r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse\data\map\user\hover\country\india\state"
    state_list = os.listdir(path)
    map_user_data = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_users": [], "App_opens": []}

    for state in state_list:
        path1 = path + "\\" + state
        year_list = os.listdir(path1)

        for year in year_list:
            path2 = path1 + "\\" + year
            quarter_list = os.listdir(path2)

            for quarter in quarter_list:
                path3 = path2 + "\\" + quarter
                data = open(path3, "r")
                d = json.load(data)

                for i in d["data"]["hoverData"].items():
                    map_user_data["District"].append(i[0])
                    map_user_data["Registered_users"].append(i[1]["registeredUsers"])
                    map_user_data["App_opens"].append(i[1]["appOpens"])
                    map_user_data["State"].append(state)
                    map_user_data["Year"].append(year)
                    map_user_data["Quarter"].append(quarter.strip(".json"))

    map_user = pd.DataFrame(map_user_data)
    map_user["State"] = map_user["State"].str.replace("-", " ").str.title()
    return map_user


# Getting Top Transaction Data
def getting_top_transaction():
    path = r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse\data\top\transaction\country\india\state"
    state_list = os.listdir(path)
    top_trans_data = {"State": [], "Year": [], "Quarter": [], "Pincode": [], "Transaction_count": [],
                      "Transaction_amount": []}

    for state in state_list:
        path1 = path + "\\" + state
        year_list = os.listdir(path1)

        for year in year_list:
            path2 = path1 + "\\" + year
            quarter_list = os.listdir(path2)

            for quarter in quarter_list:
                path3 = path2 + "\\" + quarter
                data = open(path3, "r")
                d = json.load(data)

                for i in d["data"]["pincodes"]:
                    top_trans_data["Pincode"].append(i["entityName"])
                    top_trans_data["Transaction_count"].append(i["metric"]["count"])
                    top_trans_data["Transaction_amount"].append(i["metric"]["amount"])
                    top_trans_data["State"].append(state)
                    top_trans_data["Year"].append(year)
                    top_trans_data["Quarter"].append(quarter.strip(".json"))

    top_transaction = pd.DataFrame(top_trans_data)
    top_transaction["State"] = top_transaction["State"].str.replace("-", " ").str.title()
    return top_transaction


# Getting Top User Data
def getting_top_user():
    path = r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\pulse\data\top\user\country\india\state"
    state_list = os.listdir(path)
    top_user_data = {"State": [], "Year": [], "Quarter": [], "Pincode": [], "Registered_users": []}

    for state in state_list:
        path1 = path + "\\" + state
        year_list = os.listdir(path1)

        for year in year_list:
            path2 = path1 + "\\" + year
            quarter_list = os.listdir(path2)

            for quarter in quarter_list:
                path3 = path2 + "\\" + quarter
                data = open(path3, "r")
                d = json.load(data)

                for i in d["data"]["pincodes"]:
                    top_user_data["Pincode"].append(i["name"])
                    top_user_data["Registered_users"].append(i["registeredUsers"])
                    top_user_data["State"].append(state)
                    top_user_data["Year"].append(year)
                    top_user_data["Quarter"].append(quarter.strip(".json"))

    top_user = pd.DataFrame(top_user_data)
    top_user["State"] = top_user["State"].str.replace("-", " ").str.title()
    return top_user


# Table Creation in MYSQL Database
def table_creation():
    query = '''CREATE TABLE if not exists agg_transaction(State VARCHAR(40),
                                                          Year INT,
                                                          Quarter TINYINT,
                                                          Transaction_type VARCHAR(30),
                                                          Transaction_count INT,
                                                          Transaction_amount FLOAT
                                                          )'''
    my_cursor.execute(query)

    query = '''CREATE TABLE if not exists agg_user(State VARCHAR(40),
                                                   Year INT,
                                                   Quarter TINYINT,
                                                   Registered_users INT,
                                                   App_opens BIGINT
                                                   )'''
    my_cursor.execute(query)

    query = '''CREATE TABLE if not exists map_transaction(State VARCHAR(40),
                                                          Year INT,
                                                          Quarter TINYINT,
                                                          District VARCHAR(50),
                                                          Transaction_count INT,
                                                          Transaction_amount FLOAT
                                                          )'''
    my_cursor.execute(query)

    query = '''CREATE TABLE if not exists map_user(State VARCHAR(40),
                                                   Year INT,
                                                   Quarter TINYINT,
                                                   District VARCHAR(50),
                                                   Registered_users INT,
                                                   App_opens INT
                                                   )'''
    my_cursor.execute(query)

    query = '''CREATE TABLE if not exists top_transaction(State VARCHAR(40),
                                                          Year INT,
                                                          Quarter TINYINT,
                                                          Pincode INT,
                                                          Transaction_count INT,
                                                          Transaction_amount FLOAT
                                                          )'''
    my_cursor.execute(query)

    query = '''CREATE TABLE if not exists top_user(State VARCHAR(40),
                                                   Year INT,
                                                   Quarter TINYINT,
                                                   Pincode INT,
                                                   Registered_users INT
                                                   )'''
    my_cursor.execute(query)

    return "tables created successfully"


# Insert into Aggregated Transaction Table
def insert_into_agg_transaction():
    agg_transaction = getting_agg_transaction()
    query = '''INSERT INTO agg_transaction(State,
                                           Year,
                                           Quarter,
                                           Transaction_type,
                                           Transaction_count,
                                           Transaction_amount
                                            )
                                            VALUES(%s, %s, %s, %s, %s, %s)'''
    values = zip(agg_transaction["State"],
                 agg_transaction["Year"],
                 agg_transaction["Quarter"],
                 agg_transaction["Transaction_type"],
                 agg_transaction["Transaction_count"],
                 agg_transaction["Transaction_amount"])
    for row in values:
        my_cursor.execute(query, row)
        my_database.commit()
    return "inserted successfully"


# Insert into Aggregated User Table
def insert_into_agg_user():
    agg_user = getting_agg_user()
    query = '''INSERT INTO agg_user(State,
                                    Year,
                                    Quarter,
                                    Registered_users,
                                    App_opens
                                    )
                                    VALUES(%s, %s, %s, %s, %s)'''
    values = zip(agg_user["State"],
                 agg_user["Year"],
                 agg_user["Quarter"],
                 agg_user["Registered_users"],
                 agg_user["App_opens"])
    for row in values:
        my_cursor.execute(query, row)
        my_database.commit()
    return "inserted successfully"


# Insert into Map Transaction Table
def insert_into_map_transaction():
    map_transaction = getting_map_transaction()
    query = '''INSERT INTO map_transaction(State,
                                           Year,
                                           Quarter,
                                           District,
                                           Transaction_count,
                                           Transaction_amount
                                            )
                                            VALUES(%s, %s, %s, %s, %s, %s)'''
    values = zip(map_transaction["State"],
                 map_transaction["Year"],
                 map_transaction["Quarter"],
                 map_transaction["District"],
                 map_transaction["Transaction_count"],
                 map_transaction["Transaction_amount"])
    for row in values:
        my_cursor.execute(query, row)
        my_database.commit()
    return "inserted successfully"


# Insert into Map User Table
def insert_into_map_user():
    map_user = getting_map_user()
    query = '''INSERT INTO map_user(State,
                                    Year,
                                    Quarter,
                                    District,
                                    Registered_users,
                                    App_opens
                                    )
                                    VALUES(%s, %s, %s, %s, %s, %s)'''
    values = zip(map_user["State"],
                 map_user["Year"],
                 map_user["Quarter"],
                 map_user["District"],
                 map_user["Registered_users"],
                 map_user["App_opens"])
    for row in values:
        my_cursor.execute(query, row)
        my_database.commit()
    return "inserted successfully"


# Insert into Top Transaction Table
def insert_into_top_transaction():
    top_transaction = getting_top_transaction()
    query = '''INSERT INTO top_transaction(State,
                                           Year,
                                           Quarter,
                                           Pincode,
                                           Transaction_count,
                                           Transaction_amount
                                            )
                                            VALUES(%s, %s, %s, %s, %s, %s)'''
    values = zip(top_transaction["State"],
                 top_transaction["Year"],
                 top_transaction["Quarter"],
                 top_transaction["Pincode"],
                 top_transaction["Transaction_count"],
                 top_transaction["Transaction_amount"])
    for row in values:
        my_cursor.execute(query, row)
        my_database.commit()
    return "inserted successfully"


# Insert into Top User Table
def insert_into_top_user():
    top_user = getting_top_user()
    query = '''INSERT INTO top_user(State,
                                    Year,
                                    Quarter,
                                    Pincode,
                                    Registered_users                            
                                    )
                                    VALUES(%s, %s, %s, %s, %s)'''
    values = zip(top_user["State"],
                 top_user["Year"],
                 top_user["Quarter"],
                 top_user["Pincode"],
                 top_user["Registered_users"]
                 )
    for row in values:
        my_cursor.execute(query, row)
        my_database.commit()
    return "inserted successfully"


# Calling the table Creation and Insertion functions for MYSQL Storage
def table_insertion():
    table_creation()
    insert_into_agg_transaction()
    insert_into_agg_user()
    insert_into_map_transaction()
    insert_into_map_user()
    insert_into_top_transaction()
    insert_into_top_user()
    return "inserted successfully"


# table_insertion()             --->   # this needs to be called for one time for table creation and insertion in mysql


# Transaction Aggregated details
def transaction_aggregated(state, year, quarter):
    if state == "All India":
        query = f'''SELECT Transaction_type, SUM(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount
                    FROM agg_transaction
                    WHERE Year = {year} AND Quarter = {quarter}
                    GROUP BY Transaction_type'''
    else:
        query = f'''SELECT Transaction_type, SUM(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount
                    FROM agg_transaction
                    WHERE State = "{state}" AND Year = {year} AND Quarter = {quarter}
                    GROUP BY Transaction_type'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    trans_agg = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    trans_count = int(trans_agg["Transaction_count"].sum())
    trans_amt = int(trans_agg["Transaction_amount"].sum())
    avg_trans_val = int(trans_amt / trans_count)

    trans_agg["Transaction_count"] = trans_agg["Transaction_count"].apply(format_number)
    trans_count = format_number(trans_count)
    trans_amt = format_number(trans_amt / 10 ** 7)
    avg_trans_val = format_number(avg_trans_val)
    return trans_agg, trans_count, trans_amt, avg_trans_val


# Top 10 States Under Transaction
def top_10_states_transaction(year, quarter):
    query = f'''SELECT State, SUM(Transaction_count) AS Transaction_count 
                FROM agg_transaction
                WHERE Year = {year} and Quarter = {quarter}
                GROUP BY State
                ORDER BY Transaction_count DESC
                LIMIT 10'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    top_10 = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    top_10["Transaction_count"] = top_10["Transaction_count"].astype(float).apply(format_cash)
    return top_10


# Top 10 Districts Under Transaction
def top_10_districts_transaction(state, year, quarter):
    if state == "All India":
        query = f'''SELECT District, Transaction_count 
                    FROM map_transaction
                    WHERE Year = {year} AND Quarter = {quarter}
                    ORDER by Transaction_count DESC
                    LIMIT 10'''
    else:
        query = f'''SELECT District, Transaction_count 
                    FROM map_transaction
                    WHERE State = "{state}" AND Year = {year} AND Quarter = {quarter}
                    ORDER by Transaction_count DESC
                    LIMIT 10'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    top_10 = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    top_10["District"] = top_10["District"].str.removesuffix("district").str.title()
    top_10["Transaction_count"] = top_10["Transaction_count"].apply(format_cash)
    return top_10


# Top 10 Pincode Under Transaction
def top_10_pincode_transaction(state, year, quarter):
    if state == "All India":
        query = f'''SELECT Pincode, Transaction_count 
                    FROM top_transaction
                    WHERE Year = {year} and Quarter = {quarter}
                    ORDER by Transaction_count DESC
                    LIMIT 10'''
    else:
        query = f'''SELECT Pincode, Transaction_count 
                    FROM top_transaction
                    WHERE state = "{state}" AND Year = {year} and Quarter = {quarter}
                    ORDER by Transaction_count DESC
                    LIMIT 10'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    top_10 = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    top_10["Transaction_count"] = top_10["Transaction_count"].apply(format_cash)
    return top_10


# User Aggregated Details
def user_aggregated(state, year, quarter):
    if state == "All India":
        query = f'''SELECT SUM(Registered_users) AS Registered_users, SUM(App_opens) AS App_opens 
                    FROM agg_user
                    WHERE Year = {year} and Quarter = {quarter}'''
    else:
        query = f'''SELECT SUM(Registered_users) AS Registered_users, SUM(App_opens) AS App_opens 
                    FROM agg_user
                    WHERE State = "{state}" AND Year = {year} and Quarter = {quarter}'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    user_agg = pd.DataFrame(data, columns=my_cursor.column_names)
    user_agg[["Registered_users", "App_opens"]] = user_agg[["Registered_users", "App_opens"]].applymap(format_number)
    return user_agg


# Top 10 States Under Users
def top_10_states_users(year, quarter):
    query = f'''SELECT State, SUM(Registered_users) AS Registered_users 
                FROM agg_user
                WHERE Year = {year} and Quarter = {quarter}
                GROUP BY State
                ORDER BY Registered_users DESC
                LIMIT 10 '''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    top_10 = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    top_10["Registered_users"] = top_10["Registered_users"].astype(int).apply(format_cash)
    return top_10


# Top 10 Districts Under Users
def top_10_districts_users(state, year, quarter):
    if state == "All India":
        query = f'''SELECT  District, SUM(Registered_users) AS Registered_users 
                    FROM map_user
                    WHERE Year = {year} AND Quarter = {quarter}
                    GROUP BY District
                    ORDER BY Registered_users DESC
                    LIMIT 10'''
    else:
        query = f'''SELECT  District, SUM(Registered_users) AS Registered_users 
                    FROM map_user
                    WHERE State = "{state}" AND Year = {year} AND Quarter = {quarter}
                    GROUP BY District
                    ORDER BY Registered_users DESC
                    LIMIT 10'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    top_10 = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    top_10["District"] = top_10["District"].str.removesuffix("district").str.title()
    top_10["Registered_users"] = top_10["Registered_users"].astype(int).apply(format_cash)
    return top_10


# Top 10 Pincode Under Users
def top_10_pincode_users(state, year, quarter):
    if state == "All India":
        query = f'''SELECT  Pincode, SUM(Registered_users) AS Registered_users 
                    FROM top_user
                    WHERE Year = {year} AND Quarter = {quarter}
                    GROUP BY Pincode
                    ORDER BY Registered_users DESC
                    LIMIT 10'''
    else:
        query = f'''SELECT  Pincode, SUM(Registered_users) AS Registered_users 
                    FROM top_user
                    WHERE State = "{state}" AND Year = {year} AND Quarter = {quarter}
                    GROUP BY Pincode
                    ORDER BY Registered_users DESC
                    LIMIT 10'''
    my_cursor.execute(query)
    data = [i for i in my_cursor.fetchall()]
    top_10 = pd.DataFrame(data, columns=my_cursor.column_names, index=range(1, len(data) + 1))
    top_10["Registered_users"] = top_10["Registered_users"].astype(int).apply(format_cash)
    return top_10


# Mapping Transaction Info on India Map
def mapping_transaction(year, quarter):
    file = open(r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\venv\India_States.geojson", "r")
    geo_json_data = json.load(file)

    for i, j in enumerate(geo_json_data["features"]):
        geo_json_data["features"][i]["properties"]["ST_NM"] = j["properties"]["ST_NM"].replace("-", " ")

    query = f'''SELECT State, SUM(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount,
                SUM(Transaction_amount) / SUM(Transaction_count) AS Avg_Transaction_value 
                FROM map_transaction
                WHERE Year = {year} AND Quarter = {quarter}
                GROUP BY State'''
    my_cursor.execute(query)
    map_data = [i for i in my_cursor.fetchall()]
    map_data = pd.DataFrame(map_data, columns=my_cursor.column_names)
    map_data["Transaction_count"] = map_data["Transaction_count"].astype(float)
    map_data["all_transactions"] = map_data["Transaction_count"].astype(float).apply(format_number)
    map_data["Transaction_amount"] = "₹" + map_data["Transaction_amount"].apply(lambda x: x / 10 ** 7).apply(
        format_number) + "Cr"
    map_data["Avg_Transaction_value"] = "₹" + map_data["Avg_Transaction_value"].astype(int).apply(format_number)
    index = map_data.index[map_data["State"] == st.session_state["state"]].tolist()

    fig = px.choropleth(map_data,
                        geojson = geo_json_data,
                        locations = "State",
                        featureidkey = "properties.ST_NM",
                        color = "Transaction_count",
                        color_continuous_scale = "reds",
                        hover_name = "State",
                        hover_data = {"State": False, "Transaction_count": False, "all_transactions": True,
                                    "Transaction_amount": True, "Avg_Transaction_value": True},
                        labels = {"all_transactions": "All Transactions", "Transaction_amount": "Total Payment Value"},
                        title = f"Transaction Details for States in Q{quarter} {year}")

    fig.update_geos(fitbounds = "locations", visible = False)
    fig.update_layout(geo = dict(bgcolor ='rgba(0,0,0,0)'), width = 500, height = 500)
    fig.update_layout(coloraxis_showscale = False)
    # fig.update_layout(dragmode = False)
    fig.update_layout(title_font = {"size": 30, "color": "violet"})
    fig.update_layout(hoverlabel = dict(font = dict(size = 13)))

    if st.session_state["state"] != "All India":
        fig.update_traces(selectedpoints = index,
                          selected = dict(marker_opacity = 1),      # Fully opaque for selected
                          unselected = dict(marker_opacity = 0.2),  # Dimmed for unselected
                          selector = dict(type = 'choropleth'))
    return fig


# Mapping User Info on India Map
def mapping_users(year, quarter):
    file = open(r"C:\Users\91880\PycharmProjects\phonepe pulse data visualization\venv\India_States.geojson", "r")
    geo_json_data = json.load(file)

    for i, j in enumerate(geo_json_data["features"]):
        geo_json_data["features"][i]["properties"]["ST_NM"] = j["properties"]["ST_NM"].replace("-", " ")

    query = f'''SELECT State, SUM(Registered_users) AS Registered_users , SUM(App_opens) AS App_opens 
                FROM map_user
                WHERE Year = {year} AND Quarter = {quarter}
                GROUP BY State'''
    my_cursor.execute(query)
    map_data = [i for i in my_cursor.fetchall()]
    map_data = pd.DataFrame(map_data, columns=my_cursor.column_names)
    map_data["Registered_users"] = map_data["Registered_users"].astype(int)
    map_data["Registered_Users"] = map_data["Registered_users"].astype(int).apply(format_number)
    map_data["App_opens"] = map_data["App_opens"].apply(format_number)
    index = map_data.index[map_data["State"] == st.session_state["state"]].tolist()

    fig = px.choropleth(map_data,
                        geojson = geo_json_data,
                        locations = "State",
                        featureidkey = "properties.ST_NM",
                        color = "Registered_users",
                        color_continuous_scale = "blues",
                        hover_name = "State",
                        hover_data = {"State": False, "Registered_users": False, "Registered_Users": True,
                                    "App_opens": True},
                        title = f"Users Details for States in Q{quarter} {year}")

    fig.update_geos(fitbounds = "locations", visible = False)
    fig.update_layout(geo = dict(bgcolor = 'rgba(0,0,0,0)'), width = 100, height = 500)
    fig.update_layout(coloraxis_showscale = False)
    # fig.update_layout(dragmode = False)
    fig.update_layout(title_font = {"size": 30, "color": "violet"})
    fig.update_layout(hoverlabel = dict(font = dict(size = 13)))

    if st.session_state["state"] != "All India":
        fig.update_traces(selectedpoints = index,
                          selected = dict(marker_opacity = 1),      # Fully opaque for selected
                          unselected = dict(marker_opacity = 0.2),  # Dimmed for unselected
                          selector = dict(type = 'choropleth'))
    return fig


# Formatting the given number into K(thousands), L(lakhs), and CR(crores)  (for eg : 1234.56 Cr)
def format_cash(amount):
    def truncate_float(number, places):
        return int(number * (10 ** places)) / 10 ** places

    if amount < 1e3:
        return amount

    if 1e3 <= amount < 1e5:
        return str(truncate_float((amount / 1e5) * 100, 2)) + " K"

    if 1e5 <= amount < 1e7:
        return str(truncate_float((amount / 1e7) * 100, 2)) + " L"

    if amount >= 1e7:
        return str(truncate_float(amount / 1e7, 2)) + " Cr"


# Formatting the given number with thousand separators as per Indian numbering conventions (for eg : 12,15,535)
def format_number(number):
    locale.setlocale(locale.LC_ALL, 'en_IN')
    formatted_number = locale.format_string("%d", number, grouping=True)
    return formatted_number


# Streamlit Setup
st.set_page_config(page_title = 'Phonepe Data Visualization By kishore', layout = "wide")

with st.sidebar:
    selected = option_menu(menu_title = None,
                           options = ['Menu', "Phonepe Data Visualization"],
                           icons = ['house-door-fill', 'pie-chart-fill'],
                           default_index = 0,
                           styles = {"nav-link": {"font-size": "20px", "text-align": "left", "margin": "8px"},
                                   "icon": {"color": "yellow", "font-size": "20px"},
                                   "nav-link-selected": {"background-color": "#9457eb"}})

if selected == "Menu":
    st.title(":blue[Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly]")
    st.markdown('''The aim of this project will be a live geo visualization dashboard that displays information 
                   and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner.
                   The data will be stored in a MySQL database for efficient retrieval and the dashboard will be
                   dynamically updated to reflect the latest data.''')

if selected == "Phonepe Data Visualization":
    def update_state():
        st.session_state['types'] = st.session_state['types']

    if "state" not in st.session_state:
        st.session_state["state"] = "All India"

    col11, col12, col13, col14 = st.columns([0.22, 0.21, 0.21, 0.36])
    with col11:
        st.selectbox(f":violet[{st.session_state["state"]}]", options=["Transaction", "Users"], key = "types")
    with col12:
        st.selectbox(":violet[Year]", options = ["2018", "2019", "2020", "2021", "2022", "2023"], key="year")
    with col13:
        st.selectbox(":violet[Quarter]", options = ["1", "2", "3", "4"], key="quarter")
    with col14:
        st.selectbox(":violet[State]", options = ["All India", "Andaman & Nicobar Islands", "Andhra Pradesh",
                                                    "Arunachal Pradesh","Assam", "Bihar", "Chandigarh",
                                                    "Chhattisgarh", "Dadra & Nagar Haveli & Daman & Diu",
                                                    "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
                                                    "Jammu & Kashmir","Jharkhand", "Karnataka", "Kerala",
                                                    "Ladakh", "Lakshadweep", "Madhya Pradesh","Maharashtra",
                                                    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
                                                    "Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu",
                                                    "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"],
                                                    key="state", on_change = update_state)

    col21, col22 = st.columns([0.64, 0.36])
    with col21:
        if st.session_state["types"] == "Transaction":
            transaction_plot = mapping_transaction(int(st.session_state["year"]), int(st.session_state["quarter"]))
            st.plotly_chart(transaction_plot, use_container_width=True)

        if st.session_state["types"] == "Users":
            users_plot = mapping_users(int(st.session_state["year"]), int(st.session_state["quarter"]))
            st.plotly_chart(users_plot, use_container_width=True)

    with col22:
        if st.session_state["types"] == "Transaction":
            with st.expander(":violet[**Transaction**]", expanded=True):
                categories, T_count, T_amount, T_avg_val = transaction_aggregated(st.session_state["state"], int(st.session_state["year"]),
                                                                                  int(st.session_state["quarter"]))

                st.write(f"All PhonePe transactions (UPI + Cards + Wallets) :blue[{T_count}]")
                st.write(f"Total Payment Value :blue[₹ {T_amount} Cr]")
                st.write(f"Average Transaction Value :blue[₹ {T_avg_val}]")
                st.markdown("---------------------------")

                st.markdown(":violet[**Categories**]")
                st.write(f"Recharge & bill payments :blue[{categories.loc[1, "Transaction_count"]}]")
                st.write(f"Peer-to-peer payments :blue[{categories.loc[2, "Transaction_count"]}]")
                st.write(f"Merchant payments :blue[{categories.loc[3, "Transaction_count"]}]")
                st.write(f"Financial Services :blue[{categories.loc[4, "Transaction_count"]}]")
                st.write(f"Others :blue[{categories.loc[5, "Transaction_count"]}]")
                st.markdown("---------------------------")

                if st.session_state["state"] == "All India":
                    T_tab1, T_tab2, T_tab3 = st.tabs(["**States**", "**Districts**", "**Pincode**"])
                    with T_tab1:
                        st.markdown(":violet[**Top 10 States**]")
                        T_top_states = top_10_states_transaction(int(st.session_state["year"]),
                                                                 int(st.session_state["quarter"]))
                        st.table(T_top_states)
                else:
                    T_tab2, T_tab3 = st.tabs(["**Districts**", "**Pincode**"])


                with T_tab2:
                    st.markdown(":violet[**Top 10 Districts**]")
                    T_top_district = top_10_districts_transaction(st.session_state["state"], int(st.session_state["year"]),
                                                                  int(st.session_state["quarter"]))
                    st.table(T_top_district)
                with T_tab3:
                    st.markdown(":violet[**Top 10 Postal Codes**]")
                    T_top_pincode = top_10_pincode_transaction(st.session_state["state"], int(st.session_state["year"]),
                                                               int(st.session_state["quarter"]))
                    st.table(T_top_pincode)

        if st.session_state["types"] == "Users":
            with st.expander(":violet[**Users**]", expanded=True):
                data = user_aggregated(st.session_state["state"], int(st.session_state["year"]), int(st.session_state["quarter"]))

                st.write(
                    f"Registered PhonePe users till Q{int(st.session_state["quarter"])} {int(st.session_state["year"])} :blue[{data.loc[0, "Registered_users"]}]")
                st.write(
                    f"PhonePe app opens in Q{int(st.session_state["quarter"])} {int(st.session_state["year"])} :blue[{data.loc[0, "App_opens"]}]")
                st.markdown("---------------------------")

                if st.session_state["state"] == "All India":
                    U_tab1, U_tab2, U_tab3 = st.tabs(["**States**", "**Districts**", "**Pincode**"])
                    with U_tab1:
                        st.markdown(":violet[**Top 10 States**]")
                        U_top_states = top_10_states_users(int(st.session_state["year"]), int(st.session_state["quarter"]))
                        st.table(U_top_states)
                else:
                    U_tab2, U_tab3 = st.tabs(["**Districts**", "**Pincode**"])

                with U_tab2:
                    st.markdown(":violet[**Top 10 Districts**]")
                    U_top_district = top_10_districts_users(st.session_state["state"], int(st.session_state["year"]),
                                                                int(st.session_state["quarter"]))
                    st.table(U_top_district)
                with U_tab3:
                    st.markdown(":violet[**Top 10 Postal Codes**]")
                    U_top_pincode = top_10_pincode_users(st.session_state["state"], int(st.session_state["year"]),
                                                             int(st.session_state["quarter"]))
                    st.table(U_top_pincode)


# -------------x------------------x-------------------x------------------x----------------x--------------x---------------x-----------x--------------------