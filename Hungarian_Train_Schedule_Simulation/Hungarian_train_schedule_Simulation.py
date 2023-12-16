trains_info = [
    ("Bács-Kiskun", "Kecskemét", 59, 50),
    ("Baranya", "Pécs", 137, 47),
    ("Békés", "Békéscsaba", 139, 60),
    ("Borsod-Abaúj-Zemplén", "Miskolc", 127, 55),
    ("Csongrád-Csanád", "Szeged", 113, 35),
    ("Fejér", "Székesfehérvár", 43, 56),
    ("Győr-Moson-Sopron", "Győr", 83, 20),
    ("Hajdú-Bihar", "Debrecen", 157, 41),
    ("Heves", "Eger", 89, 45),
    ("Jász-Nagykun-Szolnok", "Szolnok", 73, 30),
    ("Komárom-Esztergom", "Tatabánya", 41, 51),
    ("Nógrád", "Salgótarján", 79, 46),
    ("Somogy", "Kaposvár", 131, 38),
    ("Szabolcs-Szatmár-Bereg", "Nyíregyháza", 151, 22),
    ("Tolna", "Szekszárd", 101, 52),
    ("Vas", "Szombathely", 149, 38),
    ("Veszprém", "Veszprém", 67, 40),
    ("Zala", "Zalaegerszeg", 163, 19)
]

target_timestamp = 200000

def calculate_next_departure_modular(first_departure, return_time, current_timestamp):
    cycles = (current_timestamp - first_departure + return_time - 1) // return_time 
    next_departure = first_departure + cycles * return_time 
    return next_departure

def find_next_train_modular(trains, timestamp):
    earliest_departure = float('inf')
    next_destination = None

    for county, seat, return_time, first_departure in trains:
        next_departure = calculate_next_departure_modular(first_departure, return_time, timestamp)
        if next_departure < earliest_departure:
            earliest_departure = next_departure
            next_destination = (county, seat)

    waiting_time = earliest_departure - timestamp
    return next_destination[0], next_destination[1], waiting_time

next_destination_county_modular, next_destination_city_modular, waiting_time_modular = find_next_train_modular(trains_info, target_timestamp)
print(next_destination_county_modular, next_destination_city_modular, waiting_time_modular)
