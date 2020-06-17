## Вопросы и ответы из slack

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
