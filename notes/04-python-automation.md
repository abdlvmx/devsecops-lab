# 04. Python-автоматизация

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
