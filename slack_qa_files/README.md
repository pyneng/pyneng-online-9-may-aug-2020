## Вопросы и ответы из slack

### Есть ли какие-то рекомендации по поводу расположения функций в коде?

В [PEP8](https://pep8.org/) нет рекомендаций по этому поводу.

Если скрипт в одном файле, обычно порядок такой:
1. shebang, file encoding
2. docstring модуля
3. импорт
4. константы
5. все функции в условно произвольном порядке, то есть тут уже самому надо решить как удобнее 
6. функции/код для создания CLI если есть
7. Часто, если есть код который надо писать глобально, а не в функции, создают функцию main
8. `if __name__ == "__main__":` и вызов функции main или глобального кода, который вызывает функции


При этом среди функций обычно выбирают для себя какой-то порядок, чтобы он был плюс-минус однотипным
в разных файлах. Например, сначала пишем общие функцие, которые не зависят от других функций в файле,
потом те что зависят. При этом обычно есть какой-то порядок выполнения действий: подключились на оборудование
и считали вывод, парсим его, записали результат в файл - тогда соблюдаем этот порядок в функциях.

> [О структуре больших проектов](https://docs.python-guide.org/writing/structure/). И еще одна ссылка по этой же теме, с [примерами структуры проектов Flask/Django](https://realpython.com/python-application-layouts/).

### Необходимо в Zabbix назначить имена около 300 Узлов связи

#### Первый вариант - изменение xml файла

Данные для замены replace.json:

```
replace_data = {
    "10.1.2.3": "LONDON-R1",
    "10.2.2.5": "LONDON-R5"
}
```

Узлы выгружаются в одном файле london.xml (сокращенный вывод, полный вывод в slack_qa_files/london.xml).

```
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>4.2</version>
    <date>2020-06-15T07:24:19Z</date>
    <groups>
        <group>
            <name>LONDON/Ring 6</name>
        </group>
    </groups>
    <hosts>
        <host>
            <host>10.1.2.3</host>
            <name>10.1.2.3</name>
            <description/>
            <proxy/>
         ...
        </host>
        <host>
            <host>10.2.2.5</host>
            <name>10.2.2.5</name>
            <description/>
            <proxy/>
            <status>0</status>
            <ipmi_authtype>-1</ipmi_authtype>
        </host>
    </hosts>
</zabbix_export>
```

Нужно значение ключа  <name>10.1.2.3</name> заменить на <name>LONDON-R1</name> из словаря в файле replace.json.

```python
import xml.etree.ElementTree as ET
import json

replace_dict = "replace.json"
data_file = "london.xml"

with open(replace_dict) as json_data:
    replace_from = json.load(json_data)

with open(data_file) as f:
    data = f.read()


tree = ET.fromstring(data)
for element in tree.getiterator():
    if element.tag == "name" and element.text in replace_from:
        element.text = replace_from[element.text]

with open("new_london.xml", "wb") as f:
    f.write(ET.tostring(tree, encoding="utf-8"))
```

#### Второй вариант zabbixAPI

```python
from pyzabbix.api import ZabbixAPI
import json

replace_dict = "replace.json"

with open(replace_dict) as json_data:
    replace_from = json.load(json_data)


zabbix = ZabbixAPI(url='https://zabbix.server', 
                   user='User', 
                   password='Password')
for host in zabbix.host.get():
    if replace_from.get(host['name']):
        zabbix.host.update(hostid=host['hostid'], 
                           name=replace_from[host['name']])
zabbix.user.logout()
```
