# 📚 Заметки по курсу DevSecOps

↩️ [К оглавлению проекта](../README.md)

## Тема 4. 🐍 Автоматизация на Python

**Статус:** 🟡 Продолжаем тему; JSON-валидатор и проверка диапазона порта работают. Проверку порта вынесли в функцию; следующий шаг — подготовить программу к автоматическим тестам.

### 🎯 Цели занятия

- Освоить базовый синтаксис Python: переменные, условия, циклы, списки и словари.
- Писать небольшие скрипты для проверки URL и анализа данных.
- Передавать аргументы командной строки и возвращать полезные коды завершения.
- Читать JSON и проверять данные перед обработкой.



## Проверка Python и первый запуск

Проверили доступность Python 3 и версию интерпретатора:

```bash
python3 --version
```

Результат: `Python 3.15.2`. Команда `python3` запускает Python 3, а `--version` печатает его версию.

Затем передали простой код через ключ `-c`:

```bash
python3 -c 'print("Hello, DevSecOps!")'
```

```text
Hello, DevSecOps!
```

`-c` запускает код из строки без создания отдельного `.py`-файла. `print()` выводит значение в терминал.

## Переменные, строки и числа

Создали строковые переменные и подставили их в f-строку:

```bash
python3 -c 'name = "Learner"; course = "DevSecOps"; print(f"Hello, {name}!"); print(f"Course: {course}")'
```

```text
Hello, Learner!
Course: DevSecOps
```

Знак `=` присваивает значение переменной; f-строка подставляет значения выражений внутри `{}`. В первой попытке ввели `name - "Learner"` вместо `name = "Learner"`; Python сообщил `NameError`, потому что переменная `name` ещё не была задана. `-` — оператор вычитания, а не присваивания.

Создали числовые переменные и умножили их:

```bash
python3 -c 'attempts = 3; timeout = 15; print(f"Attempts: {attempts}"); print(f"Total wait: {attempts * timeout} seconds")'
```

```text
Attempts:3
Total wait: 45 seconds
```

Числа записываются без кавычек; `*` выполняет умножение. В `Attempts:3` после двоеточия не хватает пробела — это только оформление вывода.

## Сравнения и условие `if/else`

Сравнили количество попыток с лимитом:

```bash
python3 -c 'attempts = 3; max_attempts = 5; can_retry = attempts < max_attempts; print(f"Retry allowed: {can_retry}")'
```

```text
Retry allowed: True
```

Оператор `<` сравнивает числа. Результат сравнения — логическое значение `True` или `False`; `3 < 5` даёт `True`.

Для ветвления создали `retry-check.py`:

```python
attempts = 3
max_attempts = 5

if attempts < max_attempts:
    print("Retry allowed")
else:
    print("Stop")
```

При `attempts = 3` программа вывела `Retry allowed`. Затем заменили значение на `attempts = 5`; условие `5 < 5` стало ложным, и программа вывела `Stop`. Отступы показывают, какие строки входят в блоки `if` и `else`.

Состояние файла `retry-check.py` после упражнения: `attempts = 5`, поэтому при запуске он выводит `Stop`.

## Циклы и списки

С помощью `range` выполнили действие три раза:

```bash
python3 -c 'for attempt in range(1, 4): print(f"Attempt {attempt}")'
```

```text
Attempt 1
Attempt 2
Attempt 3
```

`range(1, 4)` выдаёт числа `1`, `2`, `3`; верхняя граница `4` не включается.

Создали список сервисов в `check-services.py` и перебрали его циклом:

```python
services = ["ssh", "https", "dns"]

for service in services:
    print(f"Checking {service}")
```

Результат:

```text
Checking ssh
Checking https
Checking dns
```

Затем добавили условие внутрь цикла:

```python
services = ["ssh", "https", "dns"]

for service in services:
    if service == "https":
        print(f"{service}: web traffic")
    else:
        print(f"{service}: other service")
```

```text
ssh: other service
https: web traffic
dns: other service
```

`==` проверяет равенство, а `=` присваивает значение. Для каждого элемента списка цикл выполняет одну из веток.

Первый вариант команды с `for` в одну строку завершился `SyntaxError`: в Python составной оператор `for` нельзя поставить после обычного выражения через `;`. Перенесли цикл в многострочный `.py`-файл; он успешно выполнился.

## Следующий шаг: HTTP-запрос из Python

Проверим HTTP-статус GitHub через стандартный модуль `urllib.request`:

```bash
python3 -c 'from urllib.request import urlopen; response = urlopen("https://github.com", timeout=10); print(f"HTTP status: {response.status}"); response.close()'
```

`urlopen()` открывает URL и возвращает объект ответа; `response.status` содержит HTTP-статус. `timeout=10` задаёт ограничение ожидания в секундах ([документация Python 3.15](https://docs.python.org/3/library/urllib.request.html)).

Выполнили команду и получили:

```text
HTTP status: 200
```

Это подтверждает, что запрос из Python получил успешный HTTP-ответ от GitHub.

**Следующий шаг:** перенести проверку в многострочный `.py`-скрипт и управлять ответом через контекстный менеджер `with`.

## HTTP-проверка в Python-файле

Создали `http-check.py`:

```python
from urllib.request import urlopen

url = "https://github.com"

with urlopen(url, timeout=10) as response:
    print(f"URL: {url}")
    print(f"HTTP status: {response.status}")
```

Запустили командой `python3 http-check.py` и получили:

```text
URL: https://github.com
HTTP status: 200
```

`urlopen()` выполнил HTTP-запрос. `with` автоматически закрывает объект ответа после выхода из блока; `response.status` содержит HTTP-код.

**Следующий шаг:** добавить обработку HTTP-ошибки, сетевой ошибки и тайм-аута.

## Обработка ошибок HTTP-запроса

Добавили обработчики исключений в `http-check.py`:

```python
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

url = "https://github.com"

try:
    with urlopen(url, timeout=10) as response:
        print(f"URL: {url}")
        print(f"HTTP status: {response.status}")
except HTTPError as error:
    print(f"HTTP error: {error.code}")
except TimeoutError as error:
    print(f"Timeout: {error}")
except URLError as error:
    print(f"Network error: {error.reason}")
```

При запуске `python3 http-check.py` получили:

```text
URL: https://github.com
HTTP status: 200
```

Успешный запрос прошёл через `try`; обработчики ошибок в этом запуске не сработали. `HTTPError` обрабатывается раньше `URLError`, потому что это более конкретный HTTP-ответ с ошибочным статусом. `TimeoutError` проверяется отдельно.

Проверили обработчик HTTP-ошибки на отсутствующем файле в репозитории: скрипт вывел `HTTP error: 404` вместо необработанной трассировки.

## Проверка нескольких URL

Объединили список, цикл и обработку исключений в `http-check.py`:

```python
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

urls = [
    "https://github.com",
    "https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/this-file-does-not-exist-20261124.txt",
]

for url in urls:
    try:
        with urlopen(url, timeout=10) as response:
            print(f"{url} -> HTTP {response.status}")
    except HTTPError as error:
        print(f"{url} -> HTTP error: {error.code}")
    except TimeoutError as error:
        print(f"{url} -> Timeout: {error}")
    except URLError as error:
        print(f"{url} -> Network error: {error.reason}")
```

Результат:

```text
https://github.com -> HTTP 200
https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/this-file-does-not-exist-20261124.txt -> HTTP error: 404
```

Цикл проверил каждый URL отдельно; HTTP 404 одного адреса не остановил обработку списка. Внутри цикла ошибки каждого запроса перехватываются и выводятся вместе с его URL.

## Аргументы командной строки

Заменили встроенный список на `urls = sys.argv[1:]`, чтобы передавать адреса после имени файла. Запустили скрипт с GitHub и отсутствующим README-файлом:

```text
https://github.com -> HTTP 200
https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/this-file-does-not-exist-20261124.txt -> HTTP error: 404
```

`sys.argv[0]` содержит имя скрипта, а `sys.argv[1:]` — все переданные ему аргументы.

В коде обработчик тайм-аута сначала был введён с опечаткой `TiemoutError` вместо `TimeoutError`. Исправили строку командой `sed -i '' 's/TiemoutError/TimeoutError/' http-check.py`, проверили её через `grep`, затем повторно запустили скрипт. Результат остался ожидаемым: GitHub вернул `200`, а отсутствующий файл — `404`. Ветка тайм-аута пока не вызывалась.

Запустили `python3 http-check.py` без аргументов. Скрипт показал:

```text
Usage: http-check.py URL [URL ...]
```

Затем `echo $?` вывел `2`. Так скрипт сообщает об ошибочном вызове без URL отдельным кодом завершения.

Запустили скрипт с GitHub и отсутствующим файлом, затем проверили код через `echo $?`:

```text
https://github.com -> HTTP 200
https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/this-file-does-not-exist-20261124.txt -> HTTP error: 404
0
```

Хотя скрипт распознал и напечатал HTTP 404, код завершения оказался `0`: перехваченное исключение само по себе не завершает Python-программу с ошибкой. Для использования в shell и CI/CD скрипту нужно явно сохранить признак ошибки и завершиться с ненулевым кодом.

## Коды завершения для автоматизации

Добавили `exit_code = 0` перед циклом, присваивали `1` при HTTP-, сетевой ошибке или тайм-ауте, а после цикла завершали программу через `raise SystemExit(exit_code)`. При отсутствии URL сохранили отдельный код `2`.

Запуск с одним успешным и одним ошибочным URL вывел:

```text
https://github.com -> HTTP 200
https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/this-file-does-not-exist-20261124.txt -> HTTP error: 404
1
```

Теперь shell или CI/CD может определить, что хотя бы одна проверка завершилась ошибкой. Успешный ответ для одного URL не скрывает ошибку другого.

**Следующий шаг:** проверить, что только успешный URL возвращает `0`, а запуск без URL — `2`.

Проверили оба случая:

```text
https://github.com -> HTTP 200
0
Usage: http-check.py URL [URL ...]
2
```

Один успешный URL завершил программу с кодом `0`; отсутствие аргументов вывело подсказку и завершило программу с кодом `2`.

**Следующий шаг:** изучить функции и вынести повторяемую проверку URL в отдельную функцию.

## Функции: параметры и `return`

Создали `function-practice.py`:

```python
def calculate_total_wait(attempts, timeout):
    return attempts * timeout

total = calculate_total_wait(3, 15)
print(f"Total wait: {total} seconds")
```

Запустили командой `python3 function-practice.py`:

```text
Total wait: 45 seconds
```

`def` объявляет функцию, `attempts` и `timeout` — её параметры. При вызове функции передали значения `3` и `15`; `return` вернул результат умножения вызывающему коду.

## Функция `check_url` в HTTP-чекере

Вынесли обработку одного URL в `check_url(url)`. Функция возвращает `0`, если запрос успешен, и `1`, если возникла обработанная HTTP-, сетевая ошибка или тайм-аут. Основная часть скрипта перебирает URL, собирает общий код завершения и возвращает его через `SystemExit`.

Текущая версия `http-check.py`:

```python
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

def check_url(url):
    try:
        with urlopen(url, timeout=10) as response:
            print(f"{url} -> HTTP {response.status}")
        return 0
    except HTTPError as error:
        print(f"{url} -> HTTP error: {error.code}")
    except TimeoutError as error:
        print(f"{url} -> Timeout: {error}")
    except URLError as error:
        print(f"{url} -> Network error: {error.reason}")

    return 1

urls = sys.argv[1:]

if not urls:
    print(f"Usage: {sys.argv[0]} URL [URL ...]")
    raise SystemExit(2)

exit_code = 0

for url in urls:
    if check_url(url) != 0:
        exit_code = 1

raise SystemExit(exit_code)
```

Запустили скрипт с GitHub и отсутствующим файлом:

```text
https://github.com -> HTTP 200
https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/this-file-does-not-exist-20261124.txt -> HTTP error: 404
1
```

Ошибка одного URL не прервала проверку следующего; общий код `1` показывает, что хотя бы одна проверка завершилась ошибкой.

**Следующий шаг:** проверить, что единственный успешный URL после рефакторинга даёт код завершения `0`.

Запустили рефакторенный скрипт с одним URL `https://github.com`:

```text
https://github.com -> HTTP 200
0
```

Функция вернула `0`, и главный цикл завершил программу с кодом `0`, так как ошибок не было.

**Следующий шаг:** убедиться, что запуск без URL по-прежнему показывает подсказку и возвращает `2`.

Повторили запуск без аргументов после добавления функции:

```text
Usage: http-check.py URL [URL ...]
2
```

Проверка подтвердила, что сценарий неверного вызова по-прежнему возвращает код `2` после рефакторинга. Три основных результата `http-check.py` теперь проверены: успешный URL даёт `0`, хотя бы один HTTP/сетевой сбой — `1`, отсутствие URL — `2`.

**Следующий шаг:** изучить словари Python и хранение данных по ключам.

## Словари: пары «ключ — значение»

Создали файл `service-info.py` со словарём:

```python
service = {
    "name": "https",
    "port": 443,
    "encrypted": True,
}

print("Service:", service["name"])
print("Port:", service["port"])
print("Encrypted:", service["encrypted"])
```

Результат:

```text
Service: https
Port: 443
Encrypted: True
```

Словарь хранит пары «ключ — значение». Значение получают по ключу в квадратных скобках, например `service["port"]`.

**Следующий шаг:** пройти циклом по всем парам словаря через `.items()`.

Перебрали словарь `service` методом `.items()`:

```python
for key, value in service.items():
    print(f"{key}: {value}")
```

Результат:

```text
name: https
port: 443
encrypted: True
```

В каждой итерации `key` получает ключ, а `value` — соответствующее ему значение.

**Следующий шаг:** проверить значение `encrypted` через `if/else`.

Создали словарь для сервиса `http` и проверили флаг шифрования:

```python
service = {
    "name": "http",
    "port": 80,
    "encrypted": False,
}

if service["encrypted"]:
    print(f"{service['name']} uses encryption")
else:
    print(f"Review: {service['name']} traffic is unecrypted")
```

Результат:

```text
Review: http traffic is unecrypted
```

Так как значение `encrypted` равно `False`, выполнилась ветка `else`. В строке сообщения была опечатка `unecrypted`; правильное написание — `unencrypted`.

**Следующий шаг:** объединить список словарей с циклом и проверкой, чтобы отметить незашифрованные сервисы.

## Список словарей с проверкой флага

Создали список словарей для трёх учебных записей и прошли по нему циклом:

```python
services = [
    {"name": "http", "port": 80, "encrypted": False},
    {"name": "https", "port": 443, "encrypted": True},
    {"name": "ssh", "port": 22, "encrypted": True},
]

for service in services:
    if service["encrypted"]:
        print(f"OK: {service['name']} on port {service['port']} is encrypted")
    else:
        print(f"REVIEW: {service['name']} on port {service['port']} is unecrypted")
```

Результат:

```text
REVIEW: http on port 80 is unecrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
```

Цикл обработал каждую запись; `if/else` выбрал сообщение по значению `encrypted`. В тексте предупреждения сначала была опечатка `unecrypted`; исправили её командой `sed -i '' 's/unecrypted/unencrypted/g' service-info.py`.

После исправления получили:

```text
REVIEW: http on port 80 is unencrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
```

Исправление текста не изменило логику классификации записей.

**Следующий шаг:** добавить счётчик и вывести общее число незашифрованных сервисов.

Добавили `unencrypted_count`, увеличивали его на единицу в ветке незашифрованного сервиса и вывели итог:

```text
REVIEW: http on port 80 is unencrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
Unencrypted services found: 1
```

Оператор `+= 1` увеличил счётчик для записи `http`; итоговое значение равно `1`.

**Следующий шаг:** добавить ещё одну незашифрованную запись и проверить, что итоговый счётчик станет `2`.

Добавили запись `telnet` с `encrypted: False`. После повторного запуска получили:

```text
REVIEW: http on port 80 is unencrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
REVIEW: telnet on port 23 is unencrypted
Unencrypted services found: 2
```

Счётчик увеличился для обеих записей, где `encrypted` равно `False`, и вывел итог `2`.

## Загрузка списка сервисов из JSON

Изменили `service-info.py`, чтобы он загружал список из файла `services.json` с помощью стандартного модуля `json`:

```python
import json

with open("services.json", encoding="utf-8") as file:
    services = json.load(file)
```

Остальная проверка осталась прежней: цикл выводит состояние каждого сервиса, а счётчик суммирует записи, у которых `encrypted` равно `False`. Запустили `python3 service-info.py` и получили:

```text
REVIEW: http on port 80 is unencrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
REVIEW: telnet on port 23 is unencrypted
Unencrypted services found: 2
```

Результат совпал с предыдущим: данные теперь поступают из JSON-файла, а не заданы списком прямо в программе. `json.load(file)` читает JSON из открытого файлового объекта и превращает JSON-массив в список Python, а JSON-объекты — в словари. Параметр `encoding="utf-8"` явно задаёт кодировку файла.

## Обработка ошибок при чтении JSON

Добавили обработчики для двух ожидаемых проблем при загрузке `services.json`:

```python
try:
    with open("services.json", encoding="utf-8") as file:
        services = json.load(file)
except FileNotFoundError:
    print("ERROR: services.json was not found")
    raise SystemExit(1)
except json.JSONDecodeError as error:
    print(f"ERROR: Invalid JSON on line {error.lineno}")
    raise SystemExit(1)
```

`FileNotFoundError` обрабатывает случай, когда файл не найден. `json.JSONDecodeError` возникает, если содержимое файла не соответствует синтаксису JSON; `error.lineno` указывает номер строки с ошибкой. `SystemExit(1)` завершает программу с ненулевым кодом, сообщая оболочке о неуспешном запуске.

Проверили обычный запуск с корректным JSON. Программа продолжила работу и вывела прежний результат:

```text
REVIEW: http on port 80 is unencrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
REVIEW: telnet on port 23 is unencrypted
Unencrypted services found: 2
```

Проверили обработчик отсутствующего файла: временно переименовали `services.json` в `services.json.bak` и запустили скрипт. Он вывел `ERROR: services.json was not found` и завершился с кодом `1`. После этого вернули исходное имя файла командой `mv services.json.bak services.json`.

Проверили обработчик некорректного JSON: сохранили копию файла, записали в него незавершённый массив `[` и запустили скрипт. Получили `ERROR: Invalid JSON on line 2` и код завершения `1`. Парсер указал следующую строку, где обнаружил неожиданное окончание документа. Затем восстановили копию и повторно запустили скрипт: все четыре сервиса обработаны, итог — `Unencrypted services found: 2`.

Эти обработчики обнаруживают отсутствие файла и ошибки синтаксиса JSON. Они пока не проверяют, что корректный JSON имеет ожидаемую структуру и содержит ключи `name`, `port` и `encrypted`.

Добавили проверку типа верхнего уровня до цикла:

```python
if not isinstance(services, list):
    print("ERROR: expected a JSON list of services")
    raise SystemExit(1)
```

`isinstance(services, list)` проверяет, что после загрузки JSON переменная `services` содержит список Python. Оператор `not` меняет результат проверки: блок ошибки выполняется, если `services` не является списком. Проверили программу на исходном файле — список прошёл проверку, все четыре сервиса обработаны, итог остался `2`.

Проверили защиту на синтаксически корректном JSON-объекте `{"name":"demo"}`. Скрипт вывел `ERROR: expected a JSON list of services` и завершился с кодом `1`. Вернули резервную копию `services.json`; обычный запуск снова обработал четыре записи и вывел итог `2`.

Проверка верхнего уровня не гарантирует, что каждый элемент списка является словарём. Например, допустимый JSON-массив может содержать строку или число, и попытка обращаться к такому элементу как к `service["encrypted"]` вызовет ошибку.

Добавили нумерацию элементов и проверку типа перед чтением полей:

```python
for index, service in enumerate(services, start=1):
    if not isinstance(service, dict):
        print(f"ERROR: service #{index} must be a JSON object")
        raise SystemExit(1)

    if service["encrypted"]:
        # дальнейшая обработка сервиса
        ...
```

`enumerate(services, start=1)` возвращает для каждого элемента его порядковый номер, начиная с `1`, и само значение. Это позволяет сообщить, какая запись неверна. На исходном `services.json` все элементы оказались словарями: программа прошла все четыре записи и вывела итог `Unencrypted services found: 2`.

Проверили защиту, временно заменив содержимое на JSON-массив со строкой `["not-a-service"]`. Скрипт вывел `ERROR: service #1 must be a JSON object` и завершился с кодом `1`. Восстановили `services.json`; штатный запуск снова обработал четыре сервиса и вывел итог `2`.

Проверка типа записи не гарантирует, что в словаре присутствуют все используемые поля. Если ключа `encrypted`, `name` или `port` не будет, обращение к нему завершится `KeyError`.

Добавили проверку обязательных ключей `name`, `port` и `encrypted` для каждой записи:

```python
required_keys = {"name", "port", "encrypted"}
missing_keys = required_keys - service.keys()

if missing_keys:
    print(
        f"ERROR: service #{index} is missing keys: "
        f"{', '.join(sorted(missing_keys))}"
    )
    raise SystemExit(1)
```

`service.keys()` возвращает ключи словаря, а разность множеств находит обязательные ключи, которых не хватает. Перед этой проверкой отдельно проверяется, что элемент является словарём. Сначала проверочный блок по ошибке поместили внутрь условия `if not isinstance(service, dict)`, из-за чего для обычных словарей он пропускался. Перенесли блок на один уровень отступа наружу и сохранили отдельную проверку типа.

Повторный запуск с исходным JSON прошёл обе проверки; все четыре сервиса обработаны, итог — `Unencrypted services found: 2`.

Проверили отсутствие обязательного ключа на временной записи `{"name":"demo","port":443}`. Скрипт вывел `ERROR: service #1 is missing keys: encrypted` и завершился с кодом `1`. Восстановили резервную копию `services.json`; повторный запуск обработал четыре исходные записи и вывел итог `2`.

Проверка ключей пока не убеждается, что значения имеют правильные типы. Например, JSON допускает строку в поле `port` или число в поле `encrypted`; такие данные могут привести к некорректному результату.

Добавили таблицу ожидаемых типов и проверку каждого поля:

```python
expected_types = {
    "name": str,
    "port": int,
    "encrypted": bool,
}

for field, expected_type in expected_types.items():
    if type(service[field]) is not expected_type:
        print(
            f"ERROR: service #{index} field '{field}' must be of type "
            f"{expected_type.__name__}"
        )
        raise SystemExit(1)
```

Словарь `expected_types` связывает имя поля с ожидаемым Python-типом. Цикл проходит по парам «поле — тип», а `type(value) is expected_type` требует точного совпадения типа. Это, например, не позволяет принять `True` за целое число, хотя в Python `bool` связан с `int`.

Запустили проверку на исходных данных: все четыре записи прошли, итог — `Unencrypted services found: 2`.

Проверили неверный тип порта на временной записи `{"name":"demo","port":"443","encrypted":true}`. Скрипт вывел `ERROR: service #1 field 'port' must be of type int` и завершился с кодом `1`. Восстановили исходный `services.json`; обычный запуск снова вывел четыре результата и итог `2`.

Проверка типа подтверждает, что `port` — целое число, но ещё не проверяет допустимость значения. Например, порт `70000` — целое число, но находится за пределами диапазона TCP/UDP-портов.

## Проверка диапазона порта

Добавили функцию, которая возвращает логическое значение и проверяет, что целочисленный номер порта находится в диапазоне от `1` до `65535`:

```python
def is_valid_port(port):
    return type(port) is int and 1 <= port <= 65535
```

Вызвали её внутри цикла обработки записей:

```python
if not is_valid_port(service["port"]):
    print(f"ERROR: service #{index} port must be between 1 and 65535")
    raise SystemExit(1)
```

Функция возвращает `True`, если аргумент является целым числом в допустимом диапазоне, иначе `False`. Границы `1` и `65535` включены. Дополнительная проверка точного типа внутри функции не позволяет принять `True` или `False` за число порта.

Запустили скрипт на исходном `services.json`. Все четыре записи прошли проверку диапазона; результат остался прежним: два незашифрованных сервиса.

```text
REVIEW: http on port 80 is unencrypted
OK: https on port 443 is encrypted
OK: ssh on port 22 is encrypted
REVIEW: telnet on port 23 is unencrypted
Unencrypted services found: 2
```

Проверили порт за пределами диапазона на временной записи с `port: 70000`. Скрипт вывел `ERROR: service #1 port must be between 1 and 65535` и завершился с кодом `1`. Восстановили резервную копию JSON и повторно запустили программу: все четыре записи обработаны, итог — `Unencrypted services found: 2`.

При первом вызове случайно записали `if not not is_valid_port(...)`. Два оператора `not` отменили отрицание: для корректного порта функция возвращала `True`, и условие ошибочно срабатывало. Убрали лишний `not`; после исправления нормальные записи прошли, а `70000` был отклонён.

Проверка значения диапазона теперь охватывает обе стороны: корректный исходный файл проходит, а недопустимый порт отклоняется с ненулевым кодом завершения.

## Защита точки входа скрипта

Создали отдельный `main_guard_practice.py`, чтобы проверить поведение конструкции:

```python
def main():
    print("Main function runs")

if __name__ == "__main__":
    main()
```

При запуске `python3 main_guard_practice.py` программа вывела `Main function runs`. Команда `python3 -c 'import main_guard_practice'` не вывела ничего: при импорте переменная `__name__` содержит имя модуля, поэтому условие `__name__ == "__main__"` ложно и `main()` не вызывается. При прямом запуске файла Python присваивает `__name__` значение `"__main__"`.

Перенесли загрузку JSON и обработку сервисов в функцию `main()`, оставив `is_valid_port()` на уровне модуля, и добавили:

```python
if __name__ == "__main__":
    main()
```

После рефакторинга запустили `python3 service-info.py`. Все четыре записи обработаны, итог остался `Unencrypted services found: 2`. Это показывает, что обёртывание основной логики в `main()` не изменило поведение скрипта.

Получили функцию из файла через `runpy.run_path()` и проверили её без запуска `main()`:

```bash
python3 -c 'import runpy; is_valid_port = runpy.run_path("service-info.py")["is_valid_port"]; print([is_valid_port(port) for port in (1, 65535, 0, 70000, True)])'
```

Результат:

```text
[True, True, False, False, False]
```

Порты `1` и `65535` допустимы, `0` и `70000` находятся за диапазоном. `True` отклонено, потому что функция требует точный тип `int`. Вызов `runpy.run_path()` выполнил определения на уровне модуля, но условие `__name__ == "__main__"` не сработало, поэтому скрипт не читал JSON и не запускал основную обработку.

Создали `test_service_info.py` на стандартном модуле `unittest`. Тесты проверяют допустимые порты (включая обе границы), значения вне диапазона и булево значение `True`:

```python
class IsValidPortTests(unittest.TestCase):
    def test_valid_ports(self):
        for port in (1, 443, 65535):
            with self.subTest(port=port):
                self.assertTrue(is_valid_port(port))

    def test_ports_outside_range(self):
        for port in (0, 70000, -1):
            with self.subTest(port=port):
                self.assertFalse(is_valid_port(port))

    def test_boolean_is_not_a_port(self):
        self.assertFalse(is_valid_port(True))
```

Импортировали функцию через `runpy.run_path("service-info.py")`; благодаря защите точки входа импорт не запускает `main()`. Команда `python3 -m unittest test_service_info.py` выполнила три теста и вывела `OK`.

`unittest.TestCase` содержит проверки, `assertTrue` и `assertFalse` сравнивают ожидаемое логическое значение с результатом функции, а `subTest` показывает, какое конкретно значение проверялось при сбое.

Запустили автоматическое обнаружение:

```bash
python3 -m unittest discover -v
```

`unittest` нашёл те же три метода и завершился сообщением `Ran 3 tests ... OK`. Шаблон `test*.py` позволяет обнаруживать тестовые файлы без перечисления каждого файла в команде.

При импорте тестового модуля Python создал папку `__pycache__/`. Добавили `__pycache__/` и `*.py[cod]` в `.gitignore`; после этого кэш не отображается как неотслеживаемый объект.

Вынесли проверку одной записи в отдельную функцию `validate_service()`. Она возвращает текст ошибки при неверных данных и `None`, если запись корректна:

```python
def validate_service(service, index):
    if not isinstance(service, dict):
        return f"ERROR: service #{index} must be a JSON object"

    required_keys = {"name", "port", "encrypted"}
    missing_keys = required_keys - service.keys()
    if missing_keys:
        return (
            f"ERROR: service #{index} is missing keys: "
            f"{', '.join(sorted(missing_keys))}"
        )

    expected_types = {"name": str, "port": int, "encrypted": bool}
    for field, expected_type in expected_types.items():
        if type(service[field]) is not expected_type:
            return (
                f"ERROR: service #{index} field '{field}' "
                f"must be of type {expected_type.__name__}"
            )

    if not is_valid_port(service["port"]):
        return f"ERROR: service #{index} port must be between 1 and 65535"

    return None
```

В `main()` цикл вызывает валидатор один раз; если вернулась ошибка, печатает её и завершает программу с кодом `1`. Изначально после вызова `validate_service()` в `main()` остались старые проверки ключей, типов и порта. Удалили дублирующийся блок, оставив только вывод статуса шифрования и подсчёт. Также исправили пробел после двоеточия в сообщении о пропущенных ключах.

После правки `python3 service-info.py` обработал четыре записи и вывел итог `Unencrypted services found: 2`. Затем `python3 -m unittest discover -v` нашёл и выполнил три теста `is_valid_port()`; результат — `OK`.

Расширили `test_service_info.py`: загрузили обе функции из `service-info.py` через `runpy.run_path()` и добавили `ValidateServiceTests`:

```python
class ValidateServiceTests(unittest.TestCase):
    def test_valid_service(self):
        service = {"name": "https", "port": 443, "encrypted": True}
        self.assertIsNone(validate_service(service, 1))

    def test_non_object_is_rejected(self):
        self.assertEqual(
            validate_service("not an object", 1),
            "ERROR: service #1 must be a JSON object",
        )

    def test_missing_key_is_reported(self):
        service = {"name": "https", "port": 443}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 is missing keys: encrypted",
        )

    def test_wrong_field_type_is_reported(self):
        service = {"name": "https", "port": "443", "encrypted": True}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 field 'port' must be of type int",
        )

    def test_out_of_range_port_is_reported(self):
        service = {"name": "https", "port": 70000, "encrypted": True}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 port must be between 1 and 65535",
        )
```

`self.assertIsNone()` проверяет корректную запись, а `self.assertEqual()` сравнивает возвращённый текст ошибки с ожидаемым. Команда `python3 -m unittest discover -v` нашла все тесты: три для `is_valid_port()` и пять для `validate_service()`. Все восемь завершились `ok`; итоговый вывод — `Ran 8 tests ... OK`.

## Путь к JSON-файлу как параметр `main()`

Изменили функцию так, чтобы путь к данным можно было передать аргументом, сохранив `services.json` как значение по умолчанию:

```python
def main(services_path="services.json"):
    try:
        with open(services_path, encoding="utf-8") as file:
            services = json.load(file)
    except FileNotFoundError:
        print(f"ERROR: {services_path} was not found")
        raise SystemExit(1)
```

Обычный вызов `main()` по-прежнему читает `services.json`; тест может вызвать `main("путь-к-временному-файлу.json")`, не переименовывая и не перезаписывая рабочие данные. Для проверки сообщения об ошибке путь теперь включается в вывод.

Запустили `python3 service-info.py`: все четыре записи обработаны, итог `Unencrypted services found: 2`. Повторно выполнили `python3 -m unittest discover -v`: все восемь существующих тестов завершились `ok`.

Добавили интеграционный тест, который запускает `main()` с путём к файлу, которого нет во временной папке:

```python
class MainFileErrorTests(unittest.TestCase):
    def test_missing_file_prints_error_and_exits_with_one(self):
        with TemporaryDirectory() as temp_dir:
            missing_path = Path(temp_dir) / "missing.json"
            output = StringIO()

            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as error:
                    main(str(missing_path))

            self.assertEqual(error.exception.code, 1)
            self.assertEqual(
                output.getvalue().strip(),
                f"ERROR: {missing_path} was not found",
            )
```

`TemporaryDirectory` создаёт изолированную временную папку; `redirect_stdout` сохраняет напечатанное сообщение в `StringIO`; `assertRaises(SystemExit)` перехватывает завершение программы и позволяет проверить код `1`. Команда `python3 -m unittest discover -v` нашла девять тестов: три для `is_valid_port()`, пять для `validate_service()` и один для отсутствующего файла. Все завершились `ok`; итог — `Ran 9 tests ... OK`.

Добавили второй интеграционный тест для некорректного JSON. Временный файл содержит незавершённый массив; тест проверяет сообщение с номером строки и код завершения:

```python
    def test_invalid_json_prints_error_and_exits_with_one(self):
        with TemporaryDirectory() as temp_dir:
            invalid_path = Path(temp_dir) / "invalid.json"
            invalid_path.write_text("[\n", encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as error:
                    main(str(invalid_path))

            self.assertEqual(error.exception.code, 1)
            self.assertEqual(
                output.getvalue().strip(),
                "ERROR: Invalid JSON on line 2",
            )
```

После `python3 -m unittest discover -v` обнаружено десять тестов: все завершились `ok`, итог — `Ran 10 tests ... OK`. Рабочий `services.json` не изменялся: тест создаёт и использует отдельный временный файл.

Добавили тест для корректного JSON-объекта, хотя скрипт ожидает список сервисов:

```python
    def test_json_object_is_rejected_when_list_is_expected(self):
        with TemporaryDirectory() as temp_dir:
            object_path = Path(temp_dir) / "object.json"
            object_path.write_text('{"name":"https"}', encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as error:
                    main(str(object_path))

            self.assertEqual(error.exception.code, 1)
            self.assertEqual(
                output.getvalue().strip(),
                "ERROR: expected a JSON list of services",
            )
```

Первая попытка запуска тестов завершилась `TabError: inconsistent use of tabs and spaces in indentation`: в новом методе использовались табы, тогда как соседние методы класса были отступлены пробелами. Команда `Path.read_text().expandtabs(4)` заменила табы четырьмя пробелами; заодно исправили опечатку `excpected` в имени метода.

После исправления `python3 -m unittest discover -v` нашёл одиннадцать тестов. Все завершились `ok`; итог — `Ran 11 tests ... OK`. Тест подтвердил, что корректный JSON-объект отвергается на проверке типа верхнего уровня, выводится ожидаемая ошибка, а программа завершается с кодом `1`.

Добавили интеграционный тест успешной обработки JSON из временного файла:

```python
    def test_valid_json_prints_service_results_and_summary(self):
        with TemporaryDirectory() as temp_dir:
            valid_path = Path(temp_dir) / "services.json"
            valid_path.write_text(
                '[{"name":"https","port":443,"encrypted":true},'
                '{"name":"http","port":80,"encrypted":false}]\n',
                encoding="utf-8",
            )
            output = StringIO()

            with redirect_stdout(output):
                main(str(valid_path))

            self.assertEqual(
                output.getvalue().strip(),
                "OK: https on port 443 is encrypted\n"
                "REVIEW: http on port 80 is unencrypted\n"
                "Unencrypted services found: 1",
            )
```

Первая попытка не загрузила тестовый модуль из-за табов; после их замены четырьмя пробелами обнаружились опечатки `output - StringIO()` и `uncrypted` в ожидаемом выводе. Исправили присваивание на `output = StringIO()` и сообщения на `unencrypted`. Затем `python3 -m unittest discover -v` обнаружил двенадцать тестов, все завершились `ok`; итог — `Ran 12 tests ... OK`. Тест подтвердил обработку обеих записей и счётчик `1`, не затрагивая основной `services.json`.

## Проверка непустого имени сервиса

Добавили в `ValidateServiceTests` случай, где поле `name` содержит только пробелы:

```python
    def test_blank_name_is_rejected(self):
        service = {"name": "   ", "port": 443, "encrypted": True}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 name must not be empty",
        )
```

Проверку добавили внутрь `validate_service()` после проверки типов: имя уже гарантированно является строкой, поэтому можно безопасно вызвать `.strip()`.

```python
    if not service["name"].strip():
        return f"ERROR: service #{index} name must not be empty"
```

`strip()` удаляет пробельные символы по краям. Если после этого строка пуста, валидатор возвращает понятную ошибку.

Во время редактирования сначала вставили `return` в тестовый файл вместо `service-info.py`, а затем в обоих файлах появились табы, смешанные с пробелами. Это вызвало сначала `SyntaxError: 'return' outside function`, затем `TabError`. Переместили проверку внутрь `validate_service()` и заменили табы четырьмя пробелами через `expandtabs(4)`. После исправлений `python3 -m unittest discover -v` выполнил тринадцать тестов; все завершились `ok`, итог — `Ran 13 tests ... OK`.

Сохранили проверку непустого имени, тесты и конспект коммитом `4817827` и отправили его на GitHub. `git status` подтвердил, что рабочее дерево чистое.

**Следующий шаг:** настроить GitHub Actions, чтобы тесты автоматически запускались при push в `main` и при pull request в `main`.

## 💡 Что важно запомнить

1. Переменные хранят значения; f-строки подставляют их в текст.
2. `if/else` выбирает ветку по условию, а отступы задают границы блоков.
3. `for` перебирает элементы списка; `enumerate` добавляет к элементу порядковый номер.
4. Словарь хранит пары «ключ — значение», а список может содержать словари записей.
5. Функции принимают аргументы и возвращают результаты через `return`.
6. `sys.argv` содержит аргументы командной строки; `SystemExit` задаёт код завершения программы.
7. `try/except` позволяет обработать ожидаемые ошибки, например HTTP-ошибку, отсутствие файла и некорректный JSON.
8. `json.load()` преобразует JSON из файла в объекты Python.
9. Перед обработкой внешних данных полезно проверить структуру, обязательные поля, типы и допустимые значения.
10. Небольшую проверку с одним понятным результатом удобно вынести в функцию и повторно использовать.
11. Защита `if __name__ == "__main__"` запускает `main()` только при прямом запуске файла, а не при импорте модуля.
12. `unittest` позволяет сохранять проверки в файлах и повторно запускать их после изменений кода.
13. Функция-валидатор может возвращать сообщение об ошибке или `None`, оставляя печать и завершение программы вызывающему коду.
14. Проверка `if not name.strip()` отклоняет пустую строку и строку, состоящую только из пробелов.

## 📝 Контрольные вопросы

1. Чем список отличается от словаря?
2. Что возвращает `json.load(file)`?
3. Зачем проверять обязательные ключи перед обращением к ним?
4. Почему `type(value) is expected_type` здесь строже, чем `isinstance(value, int)` для поля `port`?
5. Что сообщает ненулевой код завершения скрипта?

**🟡 Прогресс темы:** базовые выражения, условия и циклы; функции; HTTP-запросы и обработка ошибок; аргументы командной строки и коды завершения; словари и списки; чтение JSON; обработка ошибок файла и JSON; проверка структуры, обязательных полей, типов значений, диапазона порта и непустого имени; валидатор `validate_service()`; применение `main()` и защиты точки входа; тринадцать автоматических тестов для порта, записей, ошибок JSON и успешного вывода. Следующий шаг — автоматический запуск тестов через GitHub Actions.
