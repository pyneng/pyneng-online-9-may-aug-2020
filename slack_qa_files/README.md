# Вопросы и ответы из slack


## Почему список/словарь в который собираются данные в функции, надо создавать внутри функции

Очень часто в решении заданий встречается такой нюанс: функция должна собрать какие-то данные в список/словарь
и список создан вне функции. Тогда вроде как функция работает правильно,
 но при этом тест не проходит. Это происходит потому что в таком варианте функция
 работает неправильно и каждый вызов добавляет элементы в тот же список:

```python
In [1]: result = []

In [2]: def func(items):
   ...:     for i in items:
   ...:         result.append(i*100)
   ...:     return result
   ...:

In [3]: func([1, 2, 3])
Out[3]: [100, 200, 300]

In [4]: func([7, 8])
Out[4]: [100, 200, 300, 700, 800]
```

Исправить это можно переносом списка в функцию
```python
In [20]: def func(items):
    ...:     result = []
    ...:     for i in items:
    ...:         result.append(i*100)
    ...:     return result
    ...:

In [21]: func([1, 2, 3])
Out[21]: [100, 200, 300]

In [22]: func([7, 8])
Out[22]: [700, 800]
```

Всё, что относится к функции лучше всегда писать внутри функции.
Тест тут не проходит потому что внутри файла задания функция вызывается первый раз - всё ок, а потом тест вызывает её второй раз и там вдруг в два раза больше данных чем нужно.

## Как делать get/post запросы в API

С get/post можно работать с помощью requests. Мы его не рассматриваем,
но есть [небольшой пример по запросу данных из github api с помощью requests](https://pyneng.github.io/pyneng-3/GitHub-API-JSON-example/).

Часто если есть API, то есть и модуль который позволяет из Python работать с api вместо написания запросов через requests.
Например, для Github API:
* [так работаем в лоб через requests](https://pyneng.github.io/pyneng-3/GitHub-API-JSON-example/)
* [так через модуль](https://github.com/pyneng/pyneng-online-9-may-aug-2020/blob/master/scripts/submit_tasks.py)


## Как работать с xml

Про работу с json говорить будем, xml - нет, но в Python есть встроенный модуль для работы с xml.
Микропример тут есть ниже, побольше примеров [тут](https://pymotw.com/3/xml.etree.ElementTree/index.html).

## Как работать с COM-портами

Для подключения к com-портам есть модуль pyserial, [тут есть пример](https://codecamp.ru/documentation/python/5744/python-serial-communication-pyserial).

## Нужен инструмент, который позволил бы отправить верный набор байтов, как низкоуровневую команду, и получить ответ - ок, не ок.

Можно смотреть в сторону socket - это низкоуровневый модуль (встроенный) который позволяет отправлять что угодно

## a == b или a is b

## Есть ли какие-то рекомендации по поводу расположения функций в коде?

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

## Необходимо в Zabbix назначить имена около 300 Узлов связи

### Первый вариант - изменение xml файла

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

### Второй вариант zabbixAPI

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


## Что проверяет isinstance

isinstance Это функция, которая похожа на type. Только, например, с type  можно проверить только то что объект имеет такой-то тип (является экземпляром конкретного класса), а с isinstance проверяется не только конкретный класс, но и те классы, которые наследовались.
Например, с type мы можем проверить, что тип a это класс A
```python
In [2]: class B:
   ...:     pass
   ...:

In [3]: class A(B):
   ...:     pass
   ...:

In [4]: a = A()

In [5]: type(a)
Out[5]: __main__.A

In [7]: type(a) == A
Out[7]: True
```

Не можем проверить, что он также является экземпляром класса B из-за наследования
```python
In [8]: type(a) == B
Out[8]: False
```

isinstance умеет это проверять
```python
In [9]: isinstance(a, B)
Out[9]: True

In [10]: isinstance(a, A)
Out[10]: True
```

Поэтому с помощью isinstance можно проверять такие вещи
```python
In [11]: from collections.abc import Iterable, Iterator

In [12]: a = [1, 2, 3]

In [13]: isinstance(a, Iterable)
Out[13]: True

In [15]: result = map(str.lower, ["A", "B"])

In [16]: result
Out[16]: <map at 0xb3580e2c>

In [17]: isinstance(result, Iterator)
Out[17]: True
```

## Нюанс работы с D-Link при подключении telnetlib

> [Источник решения](https://forum.dlink.ru/viewtopic.php?f=2&t=143853&hilit=telnetlib#p764356)

```python
def bulk(self, cmd, opt):
   pass


def send_command_telnetlib(ip_address, command, username, password):
    with telnetlib.Telnet(ip_address) as t:
        t.set_option_negotiation_callback(bulk)
        ...
```
