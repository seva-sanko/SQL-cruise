import mysql.connector
import random
import datetime


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1a2s3d4f5g',
    'database': 'my_cruise_db'
}

NUM_TRAVEL_AGENCIES = 30
NUM_TOUR_AGENCIES = 80
MIN_OPERATORS_PER_AGENCY = 1
MAX_OPERATORS_PER_AGENCY = 6
NUM_CLIENTS = 200
MIN_CLIENTS_PER_TOUR_AGENCY = 20
MAX_CLIENTS_PER_TOUR_AGENCY = 30
NUM_VESSELS = 50
NUM_VESSEL_TYPES = 5
NUM_CRUISE_TYPES = 4
NUM_CABIN_TYPES = 5
MIN_CABINS_PER_VESSEL = 15
MAX_CABINS_PER_VESSEL = 30
NUM_CRUISES_PER_OPERATOR = 2200
MIN_TOUR_AGENCIES_PER_CRUISE = 60
MAX_TOUR_AGENCIES_PER_CRUISE = 80
СLIENT_CRUISE_CABIN_FILL_RATE = 0.80


def generate_random_date(start_days_offset=1, end_days_offset=365):
    """Генерирует случайную дату в будущем."""
    today = datetime.date.today()
    days_to_add = random.randint(start_days_offset, end_days_offset)
    return today + datetime.timedelta(days=days_to_add)

def batch_insert(cursor, query, data_list, batch_size=100):
    """Вставляет данные пакетами."""
    if not data_list:
        return
    for i in range(0, len(data_list), batch_size):
        batch = data_list[i:i + batch_size]
        try:
            cursor.executemany(query, batch)
        except mysql.connector.Error as err:
            print(f"Ошибка при пакетной вставке: {err}")
            print(f"Запрос: {query}")


def get_ids(cursor, table_name, id_column=None):
    """Получает список ID из таблицы."""
    if id_column is None:
        id_column = table_name.lower().replace(' ', '_') + '_id'
        if table_name.lower() == 'travelagency': id_column = 'agency_id'
        if table_name.lower() == 'touragency': id_column = 'tour_agency_id'
        if table_name.lower() == 'touroperator': id_column = 'tour_operator_id'

    try:
        cursor.execute(f"SELECT {id_column} FROM {table_name}")
        return [item[0] for item in cursor.fetchall()]
    except mysql.connector.Error as err:
        print(f"Ошибка при получении ID из таблицы {table_name}: {err}")
        return []


male_first_names = ["Александр", "Дмитрий", "Максим", "Сергей", "Андрей", "Алексей", "Артем", "Илья", "Кирилл",
                     "Михаил", "Никита", "Матвей", "Роман", "Егор", "Арсений", "Иван", "Денис", "Евгений",
                     "Тимофей", "Владислав", "Игорь", "Владимир", "Павел", "Руслан", "Марк", "Олег", "Юрий",
                     "Виктор", "Василий", "Петр"]
female_first_names = ["Анастасия", "Мария", "Анна", "Виктория", "Елизавета", "Полина", "Алиса", "Дарья", "София",
                      "Александра", "Екатерина", "Ксения", "Арина", "Вероника", "Василиса", "Варвара", "Милана", "Ева",
                      "Ульяна", "Таисия", "Ольга", "Ирина", "Светлана", "Наталья", "Елена"]

last_names = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков",
              "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров", "Павлов", "Козлов",
              "Степанов", "Николаев", "Орлов", "Андреев", "Макаров", "Никитин", "Захаров", "Зайцев", "Соловьев",
              "Борисов", "Яковлев", "Григорьев"]

def generate_full_name():
    """Генерирует случайное ФИО."""
    gender = random.choice(['male', 'female'])

    if gender == 'male':
        first_name = random.choice(male_first_names)
        last_name = random.choice(last_names)
        patronymic_base = random.choice(male_first_names)
        patronymic = patronymic_base + "ович"
    else:
        first_name = random.choice(female_first_names)
        base_last_name = random.choice(last_names)
        if base_last_name.endswith("ов") or base_last_name.endswith("ев") or base_last_name.endswith("ин"):
            last_name = base_last_name + "а"
        elif base_last_name.endswith("ий"):
            last_name = base_last_name[:-2] + "ая"
        else:
            last_name = base_last_name

        patronymic_base = random.choice(male_first_names)
        patronymic = patronymic_base + "овна"

    return f"{last_name} {first_name} {patronymic}"


cnx = None
cursor = None
try:
    print("Подключение к базе данных MySQL...")
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()
    print("Подключение успешно.")

    print("Очистка существующих данных (если включено)...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    tables_to_clear = [
        'ClientCruiseCabin', 'ClientTourAgency', 'CruiseTourAgency',
        'Cruise', 'Cabin', 'TourOperator',
        'Vessel', 'TourAgency',
        'TravelAgency', 'Client',
        'CabinType', 'VesselType', 'CruiseType'
    ]
    for table in tables_to_clear:
        try:
            print(f"  Очистка таблицы {table}...")
            cursor.execute(f"DELETE FROM {table}")
            cursor.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1")
        except mysql.connector.Error as err:
            print(f"    Предупреждение: Не удалось очистить таблицу {table} (возможно, ее нет): {err}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cnx.commit()
    print("Очистка завершена.")


    print("\n--- Генерация базовых типов ---")
    # 1. типы Кают (CabinType)
    cabin_types = [('Стандарт',), ('Комфорт',), ('С окном',), ('С балконом',), ('Люкс',)]
    batch_insert(cursor, "INSERT INTO CabinType (cabin_type_level) VALUES (%s)", cabin_types)
    print(f"Добавлено {len(cabin_types)} типов кают.")
    cabin_type_ids = get_ids(cursor, 'CabinType', 'cabin_type_id')

    # 2. типы Судна (VesselType)
    vessel_types = [('Яхта',), ('Речной Лайнер',), ('Паром',), ('Морской Лайнер',), ('Круизный лайнер',)]
    batch_insert(cursor, "INSERT INTO VesselType (vessel_type_class) VALUES (%s)", vessel_types)
    print(f"Добавлено {len(vessel_types)} типов судов.")
    vessel_type_ids = get_ids(cursor, 'VesselType', 'vessel_type_id')

    # 3. типы Круиза (CruiseType)
    cruise_types = [('Речной',), ('Туристический',), ('Экскурсионный',), ('Тематический',)]
    batch_insert(cursor, "INSERT INTO CruiseType (cruise_type_name) VALUES (%s)", cruise_types)
    print(f"Добавлено {len(cruise_types)} типов круизов.")
    cruise_type_ids = get_ids(cursor, 'CruiseType', 'cruise_type_id')
    cnx.commit() # Применяем типы

    print("\n--- Генерация основных сущностей ---")
    # 4. клиенты (Client)
    clients_data = []
    for i in range(1, NUM_CLIENTS + 1):
        full_name = generate_full_name()
        history = random.choice(['Первый круиз', 'Постоянный клиент', None, 'Ездил в прошлом году'])
        passport = f"Паспорт {random.randint(1000, 9999)} {random.randint(100000, 999999)}"
        clients_data.append((full_name, history, passport))
    batch_insert(cursor, "INSERT INTO Client (client_full_name, client_history, client_personal_data) VALUES (%s, %s, %s)", clients_data)
    print(f"Добавлено {len(clients_data)} клиентов.")
    client_ids = get_ids(cursor, 'Client', 'client_id')
    cnx.commit()

    # 5. турфирмы (TravelAgency)
    agencies_data = [(f'Турфирма {i}',) for i in range(1, NUM_TRAVEL_AGENCIES + 1)]
    batch_insert(cursor, "INSERT INTO TravelAgency (agency_name) VALUES (%s)", agencies_data)
    print(f"Добавлено {len(agencies_data)} турфирм.")
    travel_agency_ids = get_ids(cursor, 'TravelAgency', 'agency_id')
    cnx.commit()

    # 6. турагентства (TourAgency)
    tour_agencies_data = []
    if travel_agency_ids:
        for i in range(1, NUM_TOUR_AGENCIES + 1):
            random_agency_id = random.choice(travel_agency_ids)
            tour_agencies_data.append((f'Турагентство {i}', random_agency_id))
        batch_insert(cursor, "INSERT INTO TourAgency (tour_agency_name, agency_id) VALUES (%s, %s)", tour_agencies_data)
        print(f"Добавлено {len(tour_agencies_data)} турагентств.")
        tour_agency_ids = get_ids(cursor, 'TourAgency', 'tour_agency_id')
    else:
        print("Нет турфирм (TravelAgency), пропускаем добавление турагентств.")
        tour_agency_ids = []
    cnx.commit()

    # 7. судна (Vessel)
    vessels_data = []
    vessels_cabins_info = {} # Словарь для хранения {vessel_id: cabins_count}
    if vessel_type_ids:
        vessel_name_parts = ["Мечта", "Звезда", "Надежда", "Орион", "Жемчуг", "Лебедь", "Бриз", "Странник", "Горизонт",
                             "Компас", "Дельфин", "Танцор", "Королева", "Принцесса", "Императрица", "Князь", "Адмирал",
                             "Исследователь", "Навигатор", "Путешественник", "Сияние", "Ветер", "Гармония", "Песня",
                             "Загадка", "Дух", "Рассвет", "Нептун", "Посейдон", "Магеллан"]
        for i in range(1, NUM_VESSELS + 1):
            name = f'"{random.choice(vessel_name_parts)}"'
            capacity = random.randint(50, 4000)
            cabins_count = random.randint(MIN_CABINS_PER_VESSEL, MAX_CABINS_PER_VESSEL)
            type_id = random.choice(vessel_type_ids)
            vessels_data.append((capacity, name, cabins_count, type_id))
        batch_insert(cursor, "INSERT INTO Vessel (vessel_capacity, vessel_name, vessel_cabins_count, vessel_type_id) VALUES (%s, %s, %s, %s)", vessels_data)
        print(f"Добавлено {len(vessels_data)} судов.")
        cursor.execute("SELECT vessel_id, vessel_cabins_count FROM Vessel")
        vessels_cabins_info = dict(cursor.fetchall())
        vessel_ids = list(vessels_cabins_info.keys())
    else:
        print("Нет типов судов (VesselType), пропускаем добавление судов.")
        vessel_ids = []
    cnx.commit()

    print("\n--- Генерация зависимых сущностей ---")

    # 8. туроператоры (TourOperator)
    operators_data = []
    if travel_agency_ids:
        for agency_id in travel_agency_ids:
            num_operators = random.randint(MIN_OPERATORS_PER_AGENCY, MAX_OPERATORS_PER_AGENCY)
            for i in range(1, num_operators + 1):
                operators_data.append((agency_id, f'Туроператор {i} для ТФ {agency_id}'))
        batch_insert(cursor, "INSERT INTO TourOperator (agency_id, tour_operator_name) VALUES (%s, %s)", operators_data)
        print(f"Добавлено {len(operators_data)} туроператоров.")
        tour_operator_ids = get_ids(cursor, 'TourOperator', 'tour_operator_id')
    else:
        print("Нет турфирм (TravelAgency), пропускаем добавление туроператоров.")
        tour_operator_ids = []
    cnx.commit()

    # 9. каюты (Cabin)
    cabins_data = []
    cabins_by_vessel = {}
    if vessel_ids and cabin_type_ids:
        print("Генерация кают (может занять время)...")
        total_cabins_added = 0
        for vessel_id, cabins_count in vessels_cabins_info.items():
            vessel_cabins_list = []
            for _ in range(cabins_count):
                type_id = random.choice(cabin_type_ids)
                vessel_cabins_list.append((type_id, vessel_id))
            batch_insert(cursor, "INSERT INTO Cabin (cabin_type_id, vessel_id) VALUES (%s, %s)", vessel_cabins_list)
            total_cabins_added += len(vessel_cabins_list)
        print(f"Добавлено {total_cabins_added} кают.")
        cursor.execute("SELECT cabin_id, vessel_id FROM Cabin")
        all_cabins_raw = cursor.fetchall()
        for c_id, v_id in all_cabins_raw:
            if v_id not in cabins_by_vessel:
                cabins_by_vessel[v_id] = []
            cabins_by_vessel[v_id].append(c_id)
        print("Информация о каютах собрана.")
    else:
        print("Нет судов или типов кают, пропускаем добавление кают.")
    cnx.commit()

    # 10. круизы (Cruise)
    cruises_data = []
    cruise_vessel_map = {}
    if cruise_type_ids and vessel_ids and tour_operator_ids:
        print("Генерация круизов (по 2000 на туроператора)...")
        cursor.execute("SELECT vessel_id, vessel_capacity FROM Vessel")
        vessel_capacities = dict(cursor.fetchall())

        cruise_names_list = [
            "Летний Бриз", "Зимняя Сказка", "Золотая Осень", "Весеннее Пробуждение",
            "Жемчужины Севера", "Сокровища Южных Морей", "По Рекам Европы",
            "Арктическая Экспедиция", "Карибский Карнавал", "Средиземноморская Ривьера",
            "Волжские просторы", "Норвежские Фьорды", "Путешествие к Айсбергам",
            "Романтика Белых Ночей", "Острова Греции", "Вино и Гастрономия",
            "Вокруг Света", "Загадки Древних Цивилизаций", "Музыкальный Вояж",
            "Полярный Экспресс", "Звездный Путь", "Тропический Рай",
            "Тихоокеанская Легенда", "Очарование Востока", "Историческое Наследие",
            "Круиз для Гурманов", "В Поисках Приключений", "Семейные Каникулы",
            "Новогоднее Чудо", "Фото-тур по Фьордам"
        ]
        cruise_name_counter = 1

        for op_id in tour_operator_ids:
            for _ in range(NUM_CRUISES_PER_OPERATOR):
                if not cruise_type_ids or not vessel_ids:
                    print("Предупреждение: отсутствуют типы круизов или суда, не могу создать круиз.")
                    continue

                type_id = random.choice(cruise_type_ids)
                v_id = random.choice(vessel_ids)
                date = generate_random_date()

                name = f'Круиз {cruise_name_counter} - {random.choice(cruise_names_list)} (Оператор {op_id})'
                cruise_name_counter += 1

                capacity = vessel_capacities.get(v_id, 100)
                cruises_data.append((type_id, date, name, v_id, capacity, op_id))

        batch_insert(cursor,
                     "INSERT INTO Cruise (cruise_type_id, cruise_date, cruise_name, vessel_id, cruise_capacity, tour_operator_id) VALUES (%s, %s, %s, %s, %s, %s)",
                     cruises_data)
        print(f"Добавлено {len(cruises_data)} круизов.")
        cursor.execute("SELECT cruise_id, vessel_id FROM Cruise")
        cruise_vessel_map = dict(cursor.fetchall())
        cruise_ids = list(cruise_vessel_map.keys())
    else:
        print("Недостаточно данных (типы круизов/суда/туроператоры) для создания круизов.")
        cruise_ids = []
    cnx.commit()

    print("\n--- Генерация связующих таблиц ---")
    # 11. связь клиент-турагенство (ClientTourAgency)
    client_agency_links = []
    if client_ids and tour_agency_ids:
        print("Генерация связей Клиент-Турагенство...")
        for agency_id in tour_agency_ids:
            num_clients_for_agency = random.randint(MIN_CLIENTS_PER_TOUR_AGENCY, MAX_CLIENTS_PER_TOUR_AGENCY)
            if len(client_ids) > 0:
                selected_clients = random.sample(client_ids, min(num_clients_for_agency, len(client_ids)))
                for client_id in selected_clients:
                    client_agency_links.append((client_id, agency_id))
        batch_insert(cursor, "INSERT IGNORE INTO ClientTourAgency (client_id, tour_agency_id) VALUES (%s, %s)",
                     client_agency_links)
        print(f"Добавлено {len(client_agency_links)} связей Клиент-Турагенство.")
    else:
        print("Нет клиентов или турагентств, пропускаем связи ClientTourAgency.")
    cnx.commit()

    # 12. связь круиз-турагенство (CruiseTourAgency)
    cruise_agency_links = []
    if cruise_ids and tour_agency_ids:
        print("Генерация связей Круиз-Турагенство (60-80 круизов на 1 турагентство)...")

        for agency_id in tour_agency_ids:
            num_cruises_for_agency = random.randint(MIN_TOUR_AGENCIES_PER_CRUISE, MAX_TOUR_AGENCIES_PER_CRUISE)

            if not cruise_ids:  # Если список круизов пуст, нет смысла продолжать для этого агентства
                print(f"  Для турагентства ID {agency_id} нет доступных круизов для связи.")
                continue

            selected_cruises = random.sample(cruise_ids, min(num_cruises_for_agency, len(cruise_ids)))

            for cruise_id in selected_cruises:
                cruise_agency_links.append((cruise_id, agency_id))

        if cruise_agency_links:
            batch_insert(cursor, "INSERT IGNORE INTO CruiseTourAgency (cruise_id, tour_agency_id) VALUES (%s, %s)",
                         cruise_agency_links)
            print(
                f"  Добавлено (или попытались добавить) {len(cruise_agency_links)} связей Круиз-Турагенство. Успешно вставлено после IGNORE: {cursor.rowcount}")
        else:
            print(
                "  Не удалось сгенерировать данные для связей Круиз-Турагенство (возможно, нет круизов или турагентств).")

    else:
        print("Нет круизов или турагентств, пропускаем связи CruiseTourAgency.")
    cnx.commit()

    # 13. бронирования (ClientCruiseCabin)
    client_cruise_cabins_data = []
    if cruise_ids and client_ids and cabins_by_vessel and cruise_vessel_map:
        print("Генерация бронирований (заполнение 80% от всех кают)...")

        all_cabin_ids_for_total_count = []
        for v_id_key in cabins_by_vessel:
            all_cabin_ids_for_total_count.extend(cabins_by_vessel[v_id_key])

        if not all_cabin_ids_for_total_count:
            print("Нет доступных кают для создания бронирований.")
        else:
            num_total_cabins = len(all_cabin_ids_for_total_count)
            target_client_cruise_cabins = int(num_total_cabins * СLIENT_CRUISE_CABIN_FILL_RATE)
            print(
                f"  Всего кают: {num_total_cabins}, Целевое кол-во бронирований ({СLIENT_CRUISE_CABIN_FILL_RATE * 100}%): {target_client_cruise_cabins}")

            if target_client_cruise_cabins <= 0:
                print("  Целевое количество бронирований равно 0, бронирования не создаются.")
            else:
                attempt_limit = target_client_cruise_cabins * 3
                generated_count = 0

                used_cruise_client_pairs = set()
                used_cruise_cabin_pairs = set()

                if not cruise_ids: print("  Нет ID круизов для генерации бронирований!");
                if not client_ids: print("  Нет ID клиентов для генерации бронирований!");

                if cruise_ids and client_ids:
                    for _ in range(attempt_limit):
                        if generated_count >= target_client_cruise_cabins:
                            break

                        random_cruise_id = random.choice(cruise_ids)
                        random_client_id = random.choice(client_ids)

                        vessel_id_for_this_cruise = cruise_vessel_map.get(random_cruise_id)

                        if not vessel_id_for_this_cruise:
                            continue

                        cabins_on_this_specific_vessel = cabins_by_vessel.get(vessel_id_for_this_cruise, [])

                        if not cabins_on_this_specific_vessel:
                            continue

                        random_cabin_id = random.choice(cabins_on_this_specific_vessel)

                        if (random_cruise_id, random_client_id) not in used_cruise_client_pairs and \
                                (random_cruise_id, random_cabin_id) not in used_cruise_cabin_pairs:
                            client_cruise_cabins_data.append((random_cruise_id, random_client_id, random_cabin_id))
                            used_cruise_client_pairs.add((random_cruise_id, random_client_id))
                            used_cruise_cabin_pairs.add((random_cruise_id, random_cabin_id))
                            generated_count += 1
                else:
                    print("  Пропуск генерации бронирований из-за отсутствия необходимых ID (круизы или клиенты).")

                if client_cruise_cabins_data:
                    batch_insert(cursor,
                                 "INSERT IGNORE INTO ClientCruiseCabin (cruise_id, client_id, cabin_id) VALUES (%s, %s, %s)",
                                 client_cruise_cabins_data)
                    print(
                        f"  Добавлено (или попытались добавить) {len(client_cruise_cabins_data)} бронирований. Успешно вставлено после IGNORE (приблизительно): {cursor.rowcount}")
                else:
                    print("  Не удалось сгенерировать данные для бронирования.")
    else:
        print("Недостаточно данных (круизы/клиенты/каюты/связь_круиз_судно) для создания бронирований.")
    cnx.commit()

    print("\n--- Генерация данных завершена успешно! ---")


    print("\n--- Подсчет общего количества строк в базе данных ---")
    total_rows = 0
    tables_for_counting = [
        'CabinType', 'VesselType', 'CruiseType', 'Client', 'TravelAgency',
        'TourAgency', 'Vessel', 'TourOperator', 'Cabin', 'Cruise',
        'ClientTourAgency', 'CruiseTourAgency', 'ClientCruiseCabin'
    ]

    if cnx and cnx.is_connected() and cursor:
        for table_name in tables_for_counting:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                print(f"Количество строк в таблице {table_name}: {count}")
                total_rows += count
            except mysql.connector.Error as err:
                print(f"Ошибка при подсчете строк в таблице {table_name}: {err}")

        print(f"\nОБЩЕЕ КОЛИЧЕСТВО СТРОК ВО ВСЕХ УЧИТЫВАЕМЫХ ТАБЛИЦАХ: {total_rows}")
        if 250000 <= total_rows <= 350000:
            print("Общее количество строк находится в ожидаемом диапазоне (250,000 - 350,000).")
        else:
            print("ВНИМАНИЕ: Общее количество строк НЕ находится в ожидаемом диапазоне (250,000 - 350,000).")


except mysql.connector.Error as err:
    print(f"Ошибка MySQL: {err}")
    if cnx and cnx.is_connected():
         print("Откатываем транзакцию...")
         cnx.rollback()
finally:
    if cursor:
        cursor.close()
        print("Курсор закрыт.")
    if cnx and cnx.is_connected():
        cnx.close()
        print("Соединение с MySQL закрыто.")