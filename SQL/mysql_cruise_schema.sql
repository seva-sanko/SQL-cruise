{\rtf1\ansi\ansicpg1251\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 -- \uc0\u1059 \u1089 \u1090 \u1072 \u1085 \u1072 \u1074 \u1083 \u1080 \u1074 \u1072 \u1077 \u1084  \u1082 \u1086 \u1076 \u1080 \u1088 \u1086 \u1074 \u1082 \u1091  \u1089 \u1086 \u1077 \u1076 \u1080 \u1085 \u1077 \u1085 \u1080 \u1103  (\u1093 \u1086 \u1088 \u1086 \u1096 \u1072 \u1103  \u1087 \u1088 \u1072 \u1082 \u1090 \u1080 \u1082 \u1072 )\
SET NAMES utf8mb4;\
SET CHARACTER SET utf8mb4;\
\
-- \uc0\u1042 \u1082 \u1083 \u1102 \u1095 \u1072 \u1077 \u1084  \u1087 \u1088 \u1086 \u1074 \u1077 \u1088 \u1082 \u1091  \u1074 \u1085 \u1077 \u1096 \u1085 \u1080 \u1093  \u1082 \u1083 \u1102 \u1095 \u1077 \u1081  (\u1087 \u1086  \u1091 \u1084 \u1086 \u1083 \u1095 \u1072 \u1085 \u1080 \u1102  \u1086 \u1073 \u1099 \u1095 \u1085 \u1086  \u1074 \u1082 \u1083 \u1102 \u1095 \u1077 \u1085 \u1072 , \u1085 \u1086  \u1076 \u1083 \u1103  \u1085 \u1072 \u1076 \u1077 \u1078 \u1085 \u1086 \u1089 \u1090 \u1080 )\
SET FOREIGN_KEY_CHECKS=1;\
\
-- \uc0\u1057 \u1086 \u1079 \u1076 \u1072 \u1085 \u1080 \u1077  \u1090 \u1072 \u1073 \u1083 \u1080 \u1094  \u1074  \u1087 \u1086 \u1088 \u1103 \u1076 \u1082 \u1077  \u1079 \u1072 \u1074 \u1080 \u1089 \u1080 \u1084 \u1086 \u1089 \u1090 \u1077 \u1081  (\u1087 \u1086  \u1074 \u1086 \u1079 \u1084 \u1086 \u1078 \u1085 \u1086 \u1089 \u1090 \u1080 )\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1058 \u1080 \u1087  \u1082 \u1072 \u1102 \u1090 \u1099  (CabinType)\
CREATE TABLE IF NOT EXISTS CabinType (\
    cabin_type_id INT AUTO_INCREMENT PRIMARY KEY,\
    cabin_type_level VARCHAR(50) NOT NULL UNIQUE -- \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1080 \u1083 \u1080  UNIQUE\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1058 \u1080 \u1087  \u1089 \u1091 \u1076 \u1085 \u1072  (VesselType)\
CREATE TABLE IF NOT EXISTS VesselType (\
    vessel_type_id INT AUTO_INCREMENT PRIMARY KEY,\
    vessel_type_class VARCHAR(50) NOT NULL\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1058 \u1080 \u1087  \u1082 \u1091 \u1088 \u1080 \u1079 \u1072  (CruiseType)\
CREATE TABLE IF NOT EXISTS CruiseType (\
    cruise_type_id INT AUTO_INCREMENT PRIMARY KEY,\
    cruise_type_name VARCHAR(50) NOT NULL\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1083 \u1080 \u1077 \u1085 \u1090  (Client)\
CREATE TABLE IF NOT EXISTS Client (\
    client_id INT AUTO_INCREMENT PRIMARY KEY,\
    client_full_name VARCHAR(150) NOT NULL,\
    client_history TEXT NULL,\
    client_personal_data TEXT NULL,\
    client_cabin_number VARCHAR(10) NULL\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1058 \u1091 \u1088 \u1092 \u1080 \u1088 \u1084 \u1072  (TravelAgency)\
-- \uc0\u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  Client, Vessel, Cruise. \u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1103 \u1077 \u1084  \u1087 \u1086 \u1089 \u1083 \u1077  \u1085 \u1080 \u1093  \u1080 \u1083 \u1080  MySQL \u1089 \u1072 \u1084  \u1088 \u1072 \u1079 \u1073 \u1077 \u1088 \u1077 \u1090 \u1089 \u1103 .\
-- \uc0\u1055 \u1086 \u1087 \u1088 \u1086 \u1073 \u1091 \u1077 \u1084  \u1086 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1080 \u1090 \u1100  \u1089 \u1077 \u1081 \u1095 \u1072 \u1089 , MySQL \u1076 \u1086 \u1083 \u1078 \u1077 \u1085  \u1089 \u1087 \u1088 \u1072 \u1074 \u1080 \u1090 \u1100 \u1089 \u1103  \u1089  \u1086 \u1090 \u1083 \u1086 \u1078 \u1077 \u1085 \u1085 \u1086 \u1081  \u1087 \u1088 \u1086 \u1074 \u1077 \u1088 \u1082 \u1086 \u1081  FK.\
CREATE TABLE IF NOT EXISTS TravelAgency (\
    agency_id INT AUTO_INCREMENT PRIMARY KEY,\
    agency_name VARCHAR(100) NOT NULL,\
    vessel_id INT NULL,\
    client_id INT NULL,\
    cruise_id INT NULL,\
    -- \uc0\u1042 \u1085 \u1077 \u1096 \u1085 \u1080 \u1077  \u1082 \u1083 \u1102 \u1095 \u1080  \u1073 \u1091 \u1076 \u1091 \u1090  \u1076 \u1086 \u1073 \u1072 \u1074 \u1083 \u1077 \u1085 \u1099  \u1085 \u1080 \u1078 \u1077  \u1095 \u1077 \u1088 \u1077 \u1079  ALTER TABLE, \u1095 \u1090 \u1086 \u1073 \u1099  \u1080 \u1079 \u1073 \u1077 \u1078 \u1072 \u1090 \u1100  \u1087 \u1088 \u1086 \u1073 \u1083 \u1077 \u1084  \u1089  \u1087 \u1086 \u1088 \u1103 \u1076 \u1082 \u1086 \u1084 \
    INDEX idx_travelagency_client (client_id) -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089 \u1099  \u1076 \u1083 \u1103  vessel_id \u1080  cruise_id \u1076 \u1086 \u1073 \u1072 \u1074 \u1080 \u1084  \u1087 \u1086 \u1079 \u1078 \u1077 \
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1058 \u1091 \u1088 \u1086 \u1087 \u1077 \u1088 \u1072 \u1090 \u1086 \u1088  (TourOperator)\
-- \uc0\u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  TravelAgency\
CREATE TABLE IF NOT EXISTS TourOperator (\
    tour_operator_id INT AUTO_INCREMENT PRIMARY KEY,\
    agency_id INT NULL,\
    tour_operator_name VARCHAR(100) NOT NULL,\
    FOREIGN KEY (agency_id) REFERENCES TravelAgency(agency_id) ON DELETE SET NULL ON UPDATE CASCADE,\
    INDEX idx_touroperator_agency (agency_id) -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1058 \u1091 \u1088 \u1072 \u1075 \u1077 \u1085 \u1089 \u1090 \u1074 \u1086  (TourAgency)\
-- \uc0\u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  TravelAgency\
CREATE TABLE IF NOT EXISTS TourAgency (\
    tour_agency_id INT AUTO_INCREMENT PRIMARY KEY,\
    tour_agency_name VARCHAR(100) NOT NULL,\
    agency_id INT NULL,\
    FOREIGN KEY (agency_id) REFERENCES TravelAgency(agency_id) ON DELETE SET NULL ON UPDATE CASCADE,\
    INDEX idx_touragency_agency (agency_id) -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1057 \u1091 \u1076 \u1085 \u1086  (Vessel)\
-- \uc0\u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  VesselType, TravelAgency, Cabin. \u1054 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1080 \u1084  FK \u1087 \u1086 \u1079 \u1078 \u1077 .\
CREATE TABLE IF NOT EXISTS Vessel (\
    vessel_id INT AUTO_INCREMENT PRIMARY KEY,\
    cabin_id INT NULL, -- \uc0\u1054 \u1089 \u1090 \u1072 \u1074 \u1083 \u1103 \u1077 \u1084  \u1089 \u1086 \u1084 \u1085 \u1080 \u1090 \u1077 \u1083 \u1100 \u1085 \u1086 \u1077  \u1087 \u1086 \u1083 \u1077  \u1089 \u1086 \u1075 \u1083 \u1072 \u1089 \u1085 \u1086  \u1086 \u1090 \u1095 \u1077 \u1090 \u1091 \
    vessel_capacity INT NOT NULL,\
    vessel_name VARCHAR(100) NOT NULL,\
    vessel_cabins_count INT NOT NULL,\
    agency_id INT NULL,\
    vessel_type_id INT NOT NULL,\
    FOREIGN KEY (vessel_type_id) REFERENCES VesselType(vessel_type_id) ON DELETE RESTRICT ON UPDATE CASCADE, -- RESTRICT, \uc0\u1095 \u1090 \u1086 \u1073 \u1099  \u1085 \u1077 \u1083 \u1100 \u1079 \u1103  \u1073 \u1099 \u1083 \u1086  \u1091 \u1076 \u1072 \u1083 \u1080 \u1090 \u1100  \u1090 \u1080 \u1087 , \u1077 \u1089 \u1083 \u1080  \u1077 \u1089 \u1090 \u1100  \u1089 \u1091 \u1076 \u1072 \
    INDEX idx_vessel_vesseltype (vessel_type_id), -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_vessel_agency (agency_id),       -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  \u1073 \u1091 \u1076 \u1091 \u1097 \u1077 \u1075 \u1086  FK\
    INDEX idx_vessel_cabin (cabin_id)         -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  \u1073 \u1091 \u1076 \u1091 \u1097 \u1077 \u1075 \u1086  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1072 \u1102 \u1090 \u1072  (Cabin)\
-- \uc0\u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  CabinType, Vessel\
CREATE TABLE IF NOT EXISTS Cabin (\
    cabin_id INT AUTO_INCREMENT PRIMARY KEY,\
    cabin_type_id INT NOT NULL,\
    vessel_id INT NOT NULL,\
    FOREIGN KEY (cabin_type_id) REFERENCES CabinType(cabin_type_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
    FOREIGN KEY (vessel_id) REFERENCES Vessel(vessel_id) ON DELETE CASCADE ON UPDATE CASCADE, -- \uc0\u1045 \u1089 \u1083 \u1080  \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1084  \u1089 \u1091 \u1076 \u1085 \u1086 , \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1084  \u1077 \u1075 \u1086  \u1082 \u1072 \u1102 \u1090 \u1099 \
    INDEX idx_cabin_cabintype (cabin_type_id), -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_cabin_vessel (vessel_id)      -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1088 \u1091 \u1080 \u1079  (Cruise)\
-- \uc0\u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  CruiseType, Vessel, TourOperator\
CREATE TABLE IF NOT EXISTS Cruise (\
    cruise_id INT AUTO_INCREMENT PRIMARY KEY,\
    cruise_type_id INT NOT NULL,\
    cruise_date DATE NOT NULL, -- \uc0\u1048 \u1089 \u1087 \u1086 \u1083 \u1100 \u1079 \u1091 \u1077 \u1084  DATE \u1076 \u1083 \u1103  \u1076 \u1072 \u1090 \u1099 \
    cruise_name VARCHAR(100) NOT NULL,\
    vessel_id INT NOT NULL,\
    cruise_capacity INT NULL,\
    tour_operator_id INT NOT NULL,\
    FOREIGN KEY (cruise_type_id) REFERENCES CruiseType(cruise_type_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
    FOREIGN KEY (vessel_id) REFERENCES Vessel(vessel_id) ON DELETE RESTRICT ON UPDATE CASCADE, -- \uc0\u1053 \u1077 \u1083 \u1100 \u1079 \u1103  \u1091 \u1076 \u1072 \u1083 \u1080 \u1090 \u1100  \u1089 \u1091 \u1076 \u1085 \u1086 , \u1077 \u1089 \u1083 \u1080  \u1077 \u1089 \u1090 \u1100  \u1082 \u1088 \u1091 \u1080 \u1079 \u1099  \u1085 \u1072  \u1085 \u1077 \u1084 ? \u1048 \u1083 \u1080  CASCADE? \u1047 \u1072 \u1074 \u1080 \u1089 \u1080 \u1090  \u1086 \u1090  \u1083 \u1086 \u1075 \u1080 \u1082 \u1080 .\
    FOREIGN KEY (tour_operator_id) REFERENCES TourOperator(tour_operator_id) ON DELETE RESTRICT ON UPDATE CASCADE,\
    INDEX idx_cruise_cruisetype (cruise_type_id), -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_cruise_vessel (vessel_id),         -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_cruise_touroperator (tour_operator_id) -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1088 \u1091 \u1080 \u1079 _\u1082 \u1083 \u1080 \u1077 \u1085 \u1090  (CruiseClient)\
CREATE TABLE IF NOT EXISTS CruiseClient (\
    cruise_client_id INT AUTO_INCREMENT PRIMARY KEY,\
    cruise_id INT NOT NULL,\
    client_id INT NOT NULL,\
    FOREIGN KEY (cruise_id) REFERENCES Cruise(cruise_id) ON DELETE CASCADE ON UPDATE CASCADE, -- \uc0\u1045 \u1089 \u1083 \u1080  \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1090 \u1089 \u1103  \u1082 \u1088 \u1091 \u1080 \u1079 , \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1090 \u1089 \u1103  \u1089 \u1074 \u1103 \u1079 \u1100 \
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE ON UPDATE CASCADE, -- \uc0\u1045 \u1089 \u1083 \u1080  \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1090 \u1089 \u1103  \u1082 \u1083 \u1080 \u1077 \u1085 \u1090 , \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1090 \u1089 \u1103  \u1089 \u1074 \u1103 \u1079 \u1100 \
    UNIQUE KEY unique_cruise_client (cruise_id, client_id), -- \uc0\u1059 \u1085 \u1080 \u1082 \u1072 \u1083 \u1100 \u1085 \u1086 \u1089 \u1090 \u1100  \u1087 \u1072 \u1088 \u1099  M:N\
    INDEX idx_cruiseclient_cruise (cruise_id), -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_cruiseclient_client (client_id)  -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1083 \u1080 \u1077 \u1085 \u1090 _\u1090 \u1091 \u1088 \u1072 \u1075 \u1077 \u1085 \u1089 \u1090 \u1074 \u1086  (ClientTourAgency)\
CREATE TABLE IF NOT EXISTS ClientTourAgency (\
    client_tour_agency_id INT AUTO_INCREMENT PRIMARY KEY,\
    client_id INT NOT NULL,\
    tour_agency_id INT NOT NULL,\
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE ON UPDATE CASCADE,\
    FOREIGN KEY (tour_agency_id) REFERENCES TourAgency(tour_agency_id) ON DELETE CASCADE ON UPDATE CASCADE,\
    UNIQUE KEY unique_client_touragency (client_id, tour_agency_id),\
    INDEX idx_clienttouragency_client (client_id),    -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_clienttouragency_touragency (tour_agency_id) -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1088 \u1091 \u1080 \u1079 _\u1090 \u1091 \u1088 \u1072 \u1075 \u1077 \u1085 \u1089 \u1090 \u1074 \u1086  (CruiseTourAgency)\
CREATE TABLE IF NOT EXISTS CruiseTourAgency (\
    cruise_tour_agency_id INT AUTO_INCREMENT PRIMARY KEY,\
    cruise_id INT NOT NULL,\
    tour_agency_id INT NOT NULL,\
    FOREIGN KEY (cruise_id) REFERENCES Cruise(cruise_id) ON DELETE CASCADE ON UPDATE CASCADE,\
    FOREIGN KEY (tour_agency_id) REFERENCES TourAgency(tour_agency_id) ON DELETE CASCADE ON UPDATE CASCADE,\
    UNIQUE KEY unique_cruise_touragency (cruise_id, tour_agency_id),\
    INDEX idx_cruisetouragency_cruise (cruise_id),     -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_cruisetouragency_touragency (tour_agency_id) -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072 : \u1050 \u1083 \u1080 \u1077 \u1085 \u1090 _\u1082 \u1072 \u1102 \u1090 \u1072  (ClientCabin)\
CREATE TABLE IF NOT EXISTS ClientCabin (\
    client_cabin_id INT AUTO_INCREMENT PRIMARY KEY,\
    cabin_id INT NOT NULL,\
    client_id INT NOT NULL,\
    FOREIGN KEY (cabin_id) REFERENCES Cabin(cabin_id) ON DELETE CASCADE ON UPDATE CASCADE, -- \uc0\u1045 \u1089 \u1083 \u1080  \u1082 \u1072 \u1102 \u1090 \u1072  \u1091 \u1076 \u1072 \u1083 \u1077 \u1085 \u1072 , \u1089 \u1074 \u1103 \u1079 \u1100  \u1091 \u1076 \u1072 \u1083 \u1103 \u1077 \u1090 \u1089 \u1103 \
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE ON UPDATE CASCADE,\
    UNIQUE KEY unique_client_cabin (client_id, cabin_id), -- \uc0\u1054 \u1073 \u1099 \u1095 \u1085 \u1086  \u1082 \u1083 \u1080 \u1077 \u1085 \u1090  \u1074  \u1086 \u1076 \u1085 \u1086 \u1081  \u1082 \u1072 \u1102 \u1090 \u1077 ? \u1048 \u1083 \u1080  \u1085 \u1091 \u1078 \u1085 \u1072  \u1076 \u1072 \u1090 \u1072 /\u1082 \u1088 \u1091 \u1080 \u1079 ? \u1055 \u1086 \u1082 \u1072  \u1090 \u1072 \u1082 .\
    INDEX idx_clientcabin_cabin (cabin_id),    -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
    INDEX idx_clientcabin_client (client_id)   -- \uc0\u1048 \u1085 \u1076 \u1077 \u1082 \u1089  \u1076 \u1083 \u1103  FK\
);\
\
-- \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1083 \u1103 \u1077 \u1084  \u1074 \u1085 \u1077 \u1096 \u1085 \u1080 \u1077  \u1082 \u1083 \u1102 \u1095 \u1080 , \u1082 \u1086 \u1090 \u1086 \u1088 \u1099 \u1077  \u1084 \u1086 \u1075 \u1083 \u1080  \u1074 \u1099 \u1079 \u1074 \u1072 \u1090 \u1100  \u1094 \u1080 \u1082 \u1083 \u1099  \u1087 \u1088 \u1080  \u1089 \u1086 \u1079 \u1076 \u1072 \u1085 \u1080 \u1080  \u1090 \u1072 \u1073 \u1083 \u1080 \u1094 \
\
ALTER TABLE TravelAgency\
    ADD CONSTRAINT fk_travelagency_vessel FOREIGN KEY (vessel_id) REFERENCES Vessel(vessel_id) ON DELETE SET NULL ON UPDATE CASCADE,\
    ADD CONSTRAINT fk_travelagency_cruise FOREIGN KEY (cruise_id) REFERENCES Cruise(cruise_id) ON DELETE SET NULL ON UPDATE CASCADE;\
\
-- \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1083 \u1103 \u1077 \u1084  \u1089 \u1086 \u1084 \u1085 \u1080 \u1090 \u1077 \u1083 \u1100 \u1085 \u1099 \u1081  FK \u1076 \u1083 \u1103  Vessel.cabin_id\
ALTER TABLE Vessel\
    ADD CONSTRAINT fk_vessel_cabin FOREIGN KEY (cabin_id) REFERENCES Cabin(cabin_id) ON DELETE SET NULL ON UPDATE CASCADE,\
    ADD CONSTRAINT fk_vessel_agency FOREIGN KEY (agency_id) REFERENCES TravelAgency(agency_id) ON DELETE SET NULL ON UPDATE CASCADE;\
\
-- \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1083 \u1103 \u1077 \u1084  \u1080 \u1085 \u1076 \u1077 \u1082 \u1089 \u1099  \u1076 \u1083 \u1103  \u1090 \u1086 \u1083 \u1100 \u1082 \u1086  \u1095 \u1090 \u1086  \u1089 \u1086 \u1079 \u1076 \u1072 \u1085 \u1085 \u1099 \u1093  FK \u1074  TravelAgency\
ALTER TABLE TravelAgency\
    ADD INDEX idx_travelagency_vessel (vessel_id),\
    ADD INDEX idx_travelagency_cruise (cruise_id);\
\
-- \uc0\u1057 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1077  \u1086 \u1073  \u1091 \u1089 \u1087 \u1077 \u1096 \u1085 \u1086 \u1084  \u1079 \u1072 \u1074 \u1077 \u1088 \u1096 \u1077 \u1085 \u1080 \u1080  (\u1095 \u1080 \u1089 \u1090 \u1086  \u1080 \u1085 \u1092 \u1086 \u1088 \u1084 \u1072 \u1090 \u1080 \u1074 \u1085 \u1086 )\
SELECT 'Schema creation script finished.' AS status;}