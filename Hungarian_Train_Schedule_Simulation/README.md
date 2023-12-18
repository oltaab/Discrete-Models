# Hungarian Train Schedule Simulation 

## Task Overview
This task is about simulating a train schedule system in a parallel universe. All trains depart from Budapest Central Train Station and make round trips to various counties in Hungary, following a strict timetable based on an epoch timestamp.

**Note**: This task was not written by me.

## Train Schedule
The task covers each county in Hungary with specified departure and return times. It is structured to show when the first train departs after the epoch and when it returns to Budapest.

### Counties and Train Timetables

| County | Seat | Return Time | First Departure |
|--------|------|-------------|-----------------|
| Bács-Kiskun | Kecskemét | 59 | 50 |
| Baranya | Pécs | 137 | 47 |
| Békés | Békéscsaba | 139 | 60 |
| Borsod-Abaúj-Zemplén | Miskolc | 127 | 55 |
| Csongrád-Csanád | Szeged | 113 | 35 |
| Fejér | Székesfehérvár | 43 | 56 |
| Győr-Moson-Sopron | Győr | 83 | 20 |
| Hajdú-Bihar | Debrecen | 157 | 41 |
| Heves | Eger | 89 | 45 |
| Jász-Nagykun-Szolnok | Szolnok | 73 | 30 |
| Komárom-Esztergom | Tatabánya | 41 | 51 |
| Nógrád | Salgótarján | 79 | 46 |
| Pest | Budapest | N/A | N/A |
| Somogy | Kaposvár | 131 | 38 |
| Szabolcs-Szatmár-Bereg | Nyíregyháza | 151 | 22 |
| Tolna | Szekszárd | 101 | 52 |
| Vas | Szombathely | 149 | 38 |
| Veszprém | Veszprém | 67 | 40 |
| Zala | Zalaegerszeg | 163 | 19 |

### Example
- For Miskolc in Borsod-Abaúj-Zemplén county, the first train departs at timestamp 55, with subsequent departures at 182, 309, etc.

## Simulation Features
- **Strict Timetable**: Every train departs and returns precisely on schedule.
- **Centralized System**: All trains start and end at Budapest Central Station.

## License
This task is part of an academic course and is used for educational purposes only.
