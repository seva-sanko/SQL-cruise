import mysql.connector
import os

db_filename = 'my_cruise_database.db'
script_dir = os.path.dirname(__file__)
db_path = os.path.join(script_dir, db_filename)

print(f"Путь к файлу БД: {db_path}")
sql_schema_code = """
PRAGMA foreign_keys = ON; 

CREATE TABLE IF NOT EXISTS CabinType (
    cabin_type_id INTEGER PRIMARY KEY,
    cabin_type_level TEXT NOT NULL UNIQUE 
);

CREATE TABLE IF NOT EXISTS VesselType (
    vessel_type_id INTEGER PRIMARY KEY,
    vessel_type_class TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS CruiseType (
    cruise_type_id INTEGER PRIMARY KEY,
    cruise_type_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS СlientCruiseCabin (
    client_cruis_cabin_id INT AUTO_INCREMENT PRIMARY KEY,
    cruise_id INT NOT NULL,
    client_id INT NOT NULL,
    cabin_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS TravelAgency (
    agency_id INTEGER PRIMARY KEY,
    agency_name TEXT NOT NULL,
    vessel_id INTEGER NULL,
    client_id INTEGER NULL,
    cruise_id INTEGER NULL
);

CREATE TABLE IF NOT EXISTS TourOperator (
    tour_operator_id INTEGER PRIMARY KEY,
    agency_id INTEGER NULL,
    tour_operator_name TEXT NOT NULL,
    FOREIGN KEY (agency_id) REFERENCES TravelAgency(agency_id) on delete no action on update no action
);

CREATE TABLE IF NOT EXISTS TourAgency (
    tour_agency_id INTEGER PRIMARY KEY,
    tour_agency_name TEXT NOT NULL,
    agency_id INTEGER NULL,
    FOREIGN KEY (agency_id) REFERENCES TravelAgency(agency_id) on delete no action on update no action
);

CREATE TABLE IF NOT EXISTS Client (
    client_id INTEGER PRIMARY KEY,
    client_full_name TEXT NOT NULL,
    client_history TEXT NULL,
    client_personal_data TEXT NULL,
    client_cabin_number TEXT NULL
);

CREATE TABLE IF NOT EXISTS Vessel (
    vessel_id INTEGER PRIMARY KEY,
    cabin_id INTEGER NULL, 
    vessel_capacity INTEGER NOT NULL,
    vessel_name TEXT NOT NULL,
    vessel_cabins_count INTEGER NOT NULL,
    agency_id INTEGER NULL,
    vessel_type_id INTEGER NOT NULL,
    FOREIGN KEY (agency_id) REFERENCES TravelAgency(agency_id) on delete no action on update no action,
    FOREIGN KEY (vessel_type_id) REFERENCES VesselType(vessel_type_id) on delete no action on update no action
);

CREATE TABLE IF NOT EXISTS Cabin (
    cabin_id INTEGER PRIMARY KEY,
    cabin_type_id INTEGER NOT NULL,
    vessel_id INTEGER NOT NULL,
    FOREIGN KEY (cabin_type_id) REFERENCES CabinType(cabin_type_id) on delete no action on update no action,
    FOREIGN KEY (vessel_id) REFERENCES Vessel(vessel_id) on delete no action on update no action
);

CREATE TABLE IF NOT EXISTS Cruise (
    cruise_id INTEGER PRIMARY KEY,
    cruise_type_id INTEGER NOT NULL,
    cruise_date TEXT NOT NULL, 
    cruise_name TEXT NOT NULL,
    vessel_id INTEGER NOT NULL,
    cruise_capacity INTEGER NULL,
    tour_operator_id INTEGER NOT NULL,
    FOREIGN KEY (cruise_type_id) REFERENCES CruiseType(cruise_type_id) on delete no action on update no action,
    FOREIGN KEY (vessel_id) REFERENCES Vessel(vessel_id) on delete no action on update no action,
    FOREIGN KEY (tour_operator_id) REFERENCES TourOperator(tour_operator_id) on delete no action on update no action
);

CREATE TABLE IF NOT EXISTS ClientTourAgency (
    client_tour_agency_id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    tour_agency_id INTEGER NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id) on delete no action on update no action,
    FOREIGN KEY (tour_agency_id) REFERENCES TourAgency(tour_agency_id) on delete no action on update no action,
    UNIQUE (client_id, tour_agency_id)
);

CREATE TABLE IF NOT EXISTS CruiseTourAgency (
    cruise_tour_agency_id INTEGER PRIMARY KEY,
    cruise_id INTEGER NOT NULL,
    tour_agency_id INTEGER NOT NULL,
    FOREIGN KEY (cruise_id) REFERENCES Cruise(cruise_id) on delete no action on update no action,
    FOREIGN KEY (tour_agency_id) REFERENCES TourAgency(tour_agency_id) on delete no action on update no action,
    UNIQUE (cruise_id, tour_agency_id)
);

"""

try:

    with mysql.connector.connect(db_path) as conn:
        cursor = conn.cursor()

        try:
            cursor.executescript(sql_schema_code)
            print("Схема БД успешно создана/обновлена.")
        except mysql.connector.Error as e:
            print(f"Ошибка при выполнении скрипта создания схемы: {e}")

        initial_cabin_types = [('Стандарт',), ('Люкс',), ('Премиум',)]
        try:
            cursor.executemany("INSERT OR IGNORE INTO CabinType (cabin_type_level) VALUES (?)", initial_cabin_types)
            print(f"Начальные данные в CabinType добавлены (или уже существовали). Вставлено строк: {cursor.rowcount}")
        except mysql.connector.Error as e:
            print(f"Ошибка при вставке начальных данных в CabinType: {e}")

        try:
            cursor.execute("SELECT cabin_type_id, cabin_type_level FROM CabinType")
            all_cabin_types = cursor.fetchall()
            print("\nТекущие типы кают в базе:")
            if not all_cabin_types:
                print("Таблица CabinType пуста.")
            else:
                for row in all_cabin_types:
                    print(row)
        except mysql.connector.Error as e:
            print(f"Ошибка при выборке данных из CabinType: {e}")

except mysql.connector.Error as e:
    print(f"Ошибка при подключении или работе с БД SQLite: {e}")

print("\nРабота с БД завершена.")