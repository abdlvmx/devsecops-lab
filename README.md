<p align="center">
  <img src="assets/readme-banner.jpg" alt="DevSecOps Lab — Security Engineering Portfolio" width="100%">
</p>

<p align="center">
  <a href="#english">English</a> · <a href="#русский">Русский</a>
</p>

# 🛡️ DevSecOps Lab

## English

A hands-on learning portfolio for DevSecOps and security engineering. This repository brings together study notes, command-line practice, and small automation scripts.

### 📚 Study Notes

The notes capture commands, observed output, explanations, and lessons learned. They are currently written in Russian.

| 📚 Module | Topics | Progress |
| --- | --- | --- |
| [Git and GitHub](notes/01-git-basics.md) | Repositories, commits, branches, remotes, and GitHub workflow | ✅ Complete |
| [Linux and Bash](notes/02-linux-terminal.md) | Terminal navigation, permissions, search, redirection, and shell scripting | ✅ Complete |
| [Networking](notes/03-networking-basics.md) | DNS, TCP, HTTP/HTTPS, TLS, caching, and network diagnostics | ✅ Complete |
| [Python automation](notes/04-python-automation.md) | Python basics, functions, URL checks, JSON, data validation, and exit codes | 🟡 In progress |

### 🧪 Hands-on Exercises

| File | What it demonstrates |
| --- | --- |
| [`http-check.py`](http-check.py) | Checks multiple URLs, handles HTTP and connection errors, and returns useful exit codes for shell or CI use |
| [`service-info.py`](service-info.py) | Reviews service records and counts entries marked as unencrypted |
| [`grep-check.sh`](grep-check.sh) | Searches a file for a pattern and distinguishes matches, no matches, and errors |
| [`permission-practice.sh`](permission-practice.sh) | Practices executable file permissions |
| [`check-services.py`](check-services.py) | Practices iterating over a list and applying a condition |
| [`retry-check.py`](retry-check.py) | Practices `if/else` decisions using an attempt limit |
| [`branch-practice.md`](branch-practice.md) | Records a Git branch and merge exercise |

### 🚀 Run an Example

Check URLs from Python:

```bash
python3 http-check.py https://github.com https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/README.md
```

Search the project README:

```bash
./grep-check.sh Linux README.md
```

### 🗺️ Learning Roadmap

- [x] Git and GitHub fundamentals
- [x] Linux and Bash fundamentals
- [x] Networking fundamentals
- [ ] Python automation
- [ ] Docker security
- [ ] SAST and SCA
- [ ] CI/CD security
- [ ] OWASP and web application security

The scripts are small learning exercises; the repository will grow as new topics are studied and practiced.

---

## Русский

Практическая лаборатория и портфолио по DevSecOps и инженерии безопасности. Здесь собраны конспекты, упражнения в командной строке и небольшие скрипты автоматизации.

### 📚 Конспекты

В конспектах сохранены команды, полученные результаты, объяснения и выводы по урокам.

| 📚 Раздел | Темы | Прогресс |
| --- | --- | --- |
| [Git и GitHub](notes/01-git-basics.md) | Репозитории, коммиты, ветки, удалённый репозиторий и работа с GitHub | ✅ Завершён |
| [Linux и Bash](notes/02-linux-terminal.md) | Навигация в терминале, права доступа, поиск, перенаправление вывода и shell-скрипты | ✅ Завершён |
| [Сети](notes/03-networking-basics.md) | DNS, TCP, HTTP/HTTPS, TLS, кэширование и диагностика сети | ✅ Завершён |
| [Автоматизация на Python](notes/04-python-automation.md) | Основы Python, функции, URL, JSON, проверка данных и коды завершения | 🟡 В процессе |

### 🧪 Практические упражнения

| Файл | Что демонстрирует |
| --- | --- |
| [`http-check.py`](http-check.py) | Проверку нескольких URL, обработку HTTP- и сетевых ошибок и коды завершения для shell/CI |
| [`service-info.py`](service-info.py) | Проверку записей о сервисах и подсчёт незашифрованных |
| [`grep-check.sh`](grep-check.sh) | Поиск шаблона в файле и различение совпадения, отсутствия совпадений и ошибки |
| [`permission-practice.sh`](permission-practice.sh) | Практику прав на выполнение файла |
| [`check-services.py`](check-services.py) | Перебор списка и применение условия |
| [`retry-check.py`](retry-check.py) | Условие `if/else` с лимитом попыток |
| [`branch-practice.md`](branch-practice.md) | Упражнение с Git-веткой и слиянием |

### 🚀 Примеры запуска

Проверить URL с помощью Python:

```bash
python3 http-check.py https://github.com https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/README.md
```

Найти Linux в README проекта:

```bash
./grep-check.sh Linux README.md
```

### 🗺️ План обучения

- [x] Основы Git и GitHub
- [x] Основы Linux и Bash
- [x] Основы сетей
- [ ] Автоматизация на Python
- [ ] Безопасность Docker
- [ ] SAST и SCA
- [ ] Безопасность CI/CD
- [ ] OWASP и безопасность веб-приложений

Скрипты в репозитории — небольшие учебные упражнения; лаборатория будет пополняться по мере изучения новых тем.
