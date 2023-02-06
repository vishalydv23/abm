from neo4j import GraphDatabase
import pandas as pd
import json

class Neo4jConnection:
    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response


def fetch_charging_point_data():
    # read the databse credentials from json file
    with open('./configs/database_credentials_git_ignored.json') as file:
        creds = json.load(file)

    conn = Neo4jConnection(uri=creds['neo4jcreds']['uri'], user=creds['neo4jcreds']['username'], pwd=creds['neo4jcreds']['password'])
    
    # query to fetch charging point list
    query_string = '''
    MATCH (c:CHARGING_STATION) 
    RETURN c.x as x, c.y as y, c.x_km as x_km, c.y_km as y_km, c.station_name as Station_Name, c.city as City
    '''
    
    cp_data_df = pd.DataFrame([dict(_) for _ in conn.query(query_string, db=creds['neo4jcreds']['db'])])
    conn.close()

    return(cp_data_df)

def fetch_point_of_interest_data():
    # read the databse credentials from json file
    with open('./configs/database_credentials_git_ignored.json') as file:
        creds = json.load(file)

    conn = Neo4jConnection(uri=creds['neo4jcreds']['uri'], user=creds['neo4jcreds']['username'], pwd=creds['neo4jcreds']['password'])
    
    # query to fetch charging point list
    query_string = '''
    MATCH (p:POI) 
    RETURN p.poi_x as poi_x, p.poi_y as poi_y, p.poi_x_km as poi_x_km, p.poi_y_km as poi_y_km, p.poi_name as poi_name, p.poi_area as poi_area, p.place_name as place_name
    '''
    
    cp_data_df = pd.DataFrame([dict(_) for _ in conn.query(query_string, db=creds['neo4jcreds']['db'])])
    conn.close()

    return(cp_data_df)

# def add_categories(list):
#     # Adds category nodes to the Neo4j graph.
#     with open(r'../configs/database_credentials_git_ignored.json') as file:
#         creds = json.load(file)

#     conn = Neo4jConnection(uri=creds['neo4jcreds']['uri'], user=creds['neo4jcreds']['username'], pwd=creds['neo4jcreds']['password'])
#     query = "CREATE (n:CHARGING_STATION {x: " + str(list.x) + ", y: " + str(list.y) +", x_km:"+ str(list.x_km) +", y_km:"+ str(list.y_km) +", station_name: '" + list.station_name + "', city: '"+ list.city +"'})"

#     return conn.query(query, db=creds['neo4jcreds']['db'])

# def temp_function_to_fill():
#     df = pd.read_csv(r'../inputs/Isle_of_Wight_charging_stations.csv')
#     df = df[29:]
#     df = df.rename(columns={"Station_Name": "station_name", "City": "city"})
#     df = df.drop('id', axis=1)
#     for i in range(29,len(df)+29,1):
#         add_categories(df.loc[i])

# temp_function_to_fill()