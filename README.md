# DevSecOps Lab

A hands-on learning portfolio for DevSecOps and security engineering. This repository brings together structured study notes, command-line practice, and small automation scripts.

## Study Notes

The notes document the commands used, observed output, explanations, and lessons learned. They are currently written in Russian.

| Module | Topics | Status |
| --- | --- | --- |
| [Git and GitHub](notes/01-git-basics.md) | Repositories, commits, branches, remotes, and GitHub workflow | Completed |
| [Linux and Bash](notes/02-linux-terminal.md) | Terminal navigation, permissions, search, redirection, and shell scripting | Completed |
| [Networking](notes/03-networking-basics.md) | DNS, TCP, HTTP/HTTPS, TLS, caching, and network diagnostics | Completed |
| [Python automation](notes/04-python-automation.md) | Variables, conditions, loops, URL checks, exceptions, and exit codes | In progress |

## Hands-on Exercises

| File | What it demonstrates |
| --- | --- |
| [`http-check.py`](http-check.py) | Checks multiple URLs, handles HTTP and connection errors, and returns meaningful exit codes for shell or CI use |
| [`grep-check.sh`](grep-check.sh) | Searches a file for a pattern and distinguishes matches, no matches, and errors |
| [`permission-practice.sh`](permission-practice.sh) | Practices executable file permissions |
| [`check-services.py`](check-services.py) | Practices iterating over a list and applying a condition |
| [`retry-check.py`](retry-check.py) | Practices `if/else` decisions using an attempt limit |
| [`branch-practice.md`](branch-practice.md) | Records a Git branch and merge exercise |

## Run an Example

Check a URL from Python:

```bash
python3 http-check.py https://github.com https://raw.githubusercontent.com/abdlvmx/devsecops-lab/main/README.md
```

Search the project README:

```bash
./grep-check.sh Linux README.md
```

## Learning Roadmap

- [x] Git and GitHub fundamentals
- [x] Linux and Bash fundamentals
- [x] Networking fundamentals
- [ ] Python automation
- [ ] Docker security
- [ ] SAST and SCA
- [ ] CI/CD security
- [ ] OWASP and web application security

The scripts are small learning exercises; the repository will grow as new topics are studied and practiced.
