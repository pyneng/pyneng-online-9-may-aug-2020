## Пример csv файла с большим количеством строк

Скачать файл:

```
wget https://github.com/intrig-unicamp/ALTO-as-a-Service/raw/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz
```

Распаковать

```
gunzip rib.table.lg.ba.ptt.br-BGP.csv.gz
```


Затем открываем БД:

```
sqlite3 rib_database.db
```

И импортируем строки из csv файла в таблицу rib:

```
sqlite> .mode csv
sqlite> .import rib.table.lg.ba.ptt.br-BGP.csv rib
```

Проверка схемы

```
sqlite> .schema rib
CREATE TABLE rib(
  "status" TEXT,
  "network" TEXT,
  "netmask" TEXT,
  "nexthop" TEXT,
  "metric" TEXT,
  "locprf" TEXT,
  "weight" TEXT,
  "path" TEXT,
  "origin" TEXT
);

```
