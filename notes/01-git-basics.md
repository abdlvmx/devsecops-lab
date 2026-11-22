# Заметки под мой личный курс DevSecOps

## Тема 1. Git: создание репозитория и первый коммит

**Статус:** основная часть выполнена; упражнение с изменением README ещё не завершено.

### Цели занятия

- Создать папку учебного проекта и Git-репозиторий.
- Разобраться в выводе `git status`.
- Создать README и проследить путь файла от неотслеживаемого до коммита.
- Понять назначение Staging Area и посмотреть историю коммитов.

## 1. Создание проекта и репозитория

В терминале была создана папка проекта, выполнен переход в неё и инициализирован Git:

```bash
mkdir -p ~/devsecops-lab
cd ~/devsecops-lab
git init
```

- `mkdir -p` создаёт папку; ключ `-p` не выдаёт ошибку, если папка уже существует.
- `cd` переходит в папку.
- `git init` создаёт в текущей папке новый локальный Git-репозиторий.

Проверка текущего расположения и состояния:

```bash
pwd
git status
```

`pwd` показал `/Users/abdlvmx/devsecops-lab`. Git сообщил, что выбрана ветка `main`, коммитов пока нет и сохранять пока нечего.

## 2. Создание README и состояние Untracked

Файл README был создан такой командой:

```bash
cat > README.md <<'EOF'
# DevSecOps Lab

My practical DevSecOps and Security Engineering learning lab.

## Topics

- Git and GitHub
- Linux and Bash
- Python automation
- Docker security
- SAST and SCA
- CI/CD security
- Network security
- OWASP
EOF
```

`cat > README.md` записывает введённый текст в файл. Строка `EOF` завершает ввод. В README указаны темы учебной лаборатории.

После `ls -la` файл `README.md` был виден в папке. `git status` показал его в секции `Untracked files`: файл существует, но Git ещё не включил его в отслеживание.

**Важно:** создание файла само по себе не добавляет его в историю Git.

## 3. Staging Area: подготовка изменений

Файл был добавлен в область подготовки:

```bash
git add README.md
git status
```

Git показал `new file: README.md` в разделе `Changes to be committed`. Это означает, что содержимое подготовлено к следующему коммиту.

### Зачем отдельно нужны `git add` и `git commit`

Staging Area позволяет выбрать, какие именно изменения войдут в следующий коммит. Например, можно подготовить README и тесты, оставив изменения Dockerfile для отдельного коммита.

- `git add` помещает выбранные изменения в Staging Area.
- `git commit` сохраняет подготовленный снимок в истории проекта.

Так проще делать отдельные понятные коммиты для документации, исправлений безопасности и конфигурации CI/CD.

## 4. Первый коммит и история

Первый коммит был создан командой:

```bash
git commit -m "Initial commit: and project README"
```

Фактический вывод:

```text
[main (root-commit) 923c00c] Initial commit: and project README
 1 file changed, 14 insertions(+)
 create mode 100644 README.md
```

Сообщение коммита содержит небольшую языковую неточность: `and project README`. На работу это не влияет; более естественный вариант — `Initial commit: add project README`. Уже созданный коммит менять не требуется.

Затем были выполнены:

```bash
git log --oneline
git status
```

Полученный результат:

```text
923c00c (HEAD -> main) Initial commit: and project README

On branch main
nothing to commit, working tree clean
```

- `root-commit` — первый коммит в истории репозитория.
- `923c00c` — короткая часть уникального идентификатора коммита (commit hash).
- `1 file changed` и `14 insertions(+)` — в коммит вошёл один файл с 14 добавленными строками.
- `HEAD` указывает на текущую позицию в истории; сейчас она совпадает с вершиной ветки `main`.
- `working tree clean` означает, что в рабочей папке нет незакоммиченных изменений.
- `git log --oneline` показывает историю коммитов в кратком виде.

## 5. Изменение README и просмотр `git diff`

В конец README был добавлен раздел прогресса:

```bash
cat >> README.md <<'EOF'

## Learning Progress

- Git basics: completed
EOF
```

После этого выполнены:

```bash
git status
git diff
```

`git status` показал `README.md` как `modified` в разделе `Changes not staged for commit`. Команды `git add` и `git commit` ещё не были выполнены, поэтому изменение пока находилось только в рабочей папке.

`git diff` показал добавленные строки:

```diff
## Learning Progress

- Git basics: completed
```

Это обычный `git diff`: он показывает изменения между рабочей папкой и индексом (Staging Area).

В том же `git status` появились `.DS_Store` и `notes/` в разделе `Untracked files`. Это новые файлы/папка, которые Git пока не отслеживает.

## 6. Подготовка и сохранение изменения README

Команда `git add README.md` подготовила именно README, не добавляя `.DS_Store` и `notes/`.

`git status` после этого показал:

```text
Changes to be committed:
  modified: README.md

Untracked files:
  .DS_Store
  notes/
```

`git diff --cached` вывел тот же добавленный раздел `Learning Progress`. Суффикс `--cached` показывает изменения, уже подготовленные к коммиту.

Затем изменение было сохранено:

```bash
git commit -m "Add learning progress to README"
```

Результат:

```text
[main 3e07ab2] Add learning progress to README
 1 file changed, 4 insertions(+)
```

После коммита `git status` продолжил показывать `.DS_Store` и `notes/` как неотслеживаемые — они в коммит не попали. `git log --oneline` показал два коммита:

```text
3e07ab2 (HEAD -> main) Add learning progress to README
923c00c Initial commit: and project README
```

Таким образом, второй коммит сохранил только четыре строки README, а папка с этим конспектом остаётся отдельным неотслеживаемым содержимым.

## 7. `.gitignore` и добавление конспекта

Чтобы Git не предлагал системный файл macOS `.DS_Store`, создай файл `.gitignore`:

```bash
cat > .gitignore <<'EOF'
.DS_Store
EOF
```

Затем подготовь `.gitignore` и папку конспектов:

```bash
git add .gitignore notes/
git status
git diff --cached --stat
```

Создан `.gitignore` с шаблоном `.DS_Store`, затем выполнены:

```bash
git add .gitignore notes/
git status
git diff --cached --stat
```

`git status` показал к коммиту два новых файла:

```text
new file: .gitignore
new file: notes/01-git-basics.md
```

`.DS_Store` пропал из обычного статуса, потому что теперь подходит под правило в `.gitignore`.

На этом этапе первоначальная проверка `git diff --cached --stat` показала:

```text
.gitignore             |   1 +
notes/01-git-basics.md | 239 ++++++++++++++++++++++++++++++++++++++++++++++
2 files changed, 240 insertions(+)
```

После повторного `git add notes/01-git-basics.md` команда `git status` показала только два подготовленных новых файла: `.gitignore` и `notes/01-git-basics.md`. Финальный `git diff --cached --stat` показал 272 строки конспекта и 273 добавленные строки суммарно.

Затем изменения были сохранены:

```bash
git commit -m "Add Git study notes and ignore macOS files"
git status
git log --oneline
```

Результат коммита:

```text
[main 1096bd7] Add Git study notes and ignore macOS files
 2 files changed, 273 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 notes/01-git-basics.md
```

После коммита `git status` показал `nothing to commit, working tree clean`. В `git log --oneline` теперь три коммита:

```text
1096bd7 (HEAD -> main) Add Git study notes and ignore macOS files
3e07ab2 Add learning progress to README
923c00c Initial commit: and project README
```

`.gitignore` и конспект сохранены в истории. `.DS_Store` не попал в коммит, потому что соответствует правилу `.DS_Store` в `.gitignore`.

## 8. Подключение GitHub и первая отправка

Проверка `git remote -v` ничего не вывела: у локального репозитория ещё не было настроенного удалённого адреса.

Для GitHub был создан адрес `https://github.com/abdlvmx/devsecops-lab.git`. Он добавлен под стандартным коротким именем `origin`:

```bash
git remote add origin https://github.com/abdlvmx/devsecops-lab.git
git remote -v
```

Проверка показала `origin` для получения (`fetch`) и отправки (`push`). Затем первая отправка была выполнена:

```bash
git push -u origin main
```

Git сообщил:

```text
* [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

Ветка `main` опубликована на GitHub. Ключ `-u` настроил отслеживание удалённой ветки `origin/main`; в дальнейшем для этой ветки обычно достаточно `git push` и `git pull`.

## Что важно запомнить

1. `git init` начинает историю репозитория в текущей папке.
2. `git status` помогает понять, что Git видит и на каком этапе находятся изменения.
3. Новый файл сначала имеет состояние Untracked.
4. `git add` подготавливает выбранные изменения; `git commit` сохраняет их в истории.
5. `git log --oneline` показывает коммиты, а `working tree clean` означает отсутствие незакоммиченных изменений.
6. `git diff` показывает незастейдженные изменения; `git diff --cached` — подготовленные.
7. Коммит сохраняет только подготовленные изменения. Файлы в `Untracked files` в него не входят.
8. `.gitignore` задаёт файлы, которые Git должен игнорировать.
9. `git remote -v` показывает адреса удалённых репозиториев.
10. `git push -u origin main` отправляет ветку на сервер и настраивает upstream-связь.

## Контрольные вопросы

1. Что означает состояние Untracked?
2. Зачем нужна Staging Area?
3. Чем отличаются `git add` и `git commit`?
4. Что означает `working tree clean`?
5. Что показывает `git diff` до `git add`?

**Освоение темы:** создание репозитория, README, работа с индексом и diff, `.gitignore`, конспект, коммиты и первая отправка ветки `main` на GitHub выполнены. Ветка отслеживает `origin/main`.
