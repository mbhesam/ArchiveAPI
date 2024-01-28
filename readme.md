<p align="center">
  <img src="https://github.com/mbhesam/archiveAPI/blob/main/cover.png" width="500" height="300" />
</p>
<p align="center">
    <h1 align="center">ARCHIVEAPI</h1>
</p>
<p align="center">
    <em><code>This API serves information about an archive of books</code></em>
</p>
<p align="center">
	<!-- Shields.io badges not used with skill icons. --><p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=md,py">
	</a></p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running archiveAPI](#-running-archiveAPI)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>This API serves information about an archive of books, allowing users to create, delete, update, and search for books across different collections. It provides extensive functionality for backend applications that require access to archive information.</code>

---

##  Features

<code>
    Create: Add new books to the archive.
    Delete: Remove specific books from the archive.
    Count: Retrieve the total number of books in the archive.
    Update: Modify existing book information.
    Download: Access specific books for download.
</code>

---

##  Repository Structure

```sh
└── archiveAPI/
    ├── api
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── services.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── archiveAPI
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── download
    │   ├── admin.py
    │   ├── apps.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    └── tasks
        ├── apps.py
        ├── celery.py
        ├── tasks.py
        └── tasks_utils.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                   | Summary                         |
| ---                                                                                    | ---                             |
| [.gitignore](https://github.com/mbhesam/archiveAPI/blob/master/.gitignore)             | <code>ignore files for git</code> |
| [requirements.txt](https://github.com/mbhesam/archiveAPI/blob/master/requirements.txt) | <code>requirements packages for running project</code> |
| [manage.py](https://github.com/mbhesam/archiveAPI/blob/master/manage.py)               | <code>core file for application</code> |

</details>

<details closed><summary>api</summary>

| File                                                                                   | Summary                         |
| ---                                                                                    | ---                             |
| [admin.py](https://github.com/mbhesam/archiveAPI/blob/master/api/admin.py)             | <code>administrator panel of api</code> |
| [views.py](https://github.com/mbhesam/archiveAPI/blob/master/api/views.py)             | <code>view functions</code> |
| [apps.py](https://github.com/mbhesam/archiveAPI/blob/master/api/apps.py)               | <code>app file</code> |
| [tests.py](https://github.com/mbhesam/archiveAPI/blob/master/api/tests.py)             | <code>code written for testing module</code> |
| [services.py](https://github.com/mbhesam/archiveAPI/blob/master/api/services.py)       | <code>file for running query to database</code> |
| [models.py](https://github.com/mbhesam/archiveAPI/blob/master/api/models.py)           | <code>database models</code> |
| [serializers.py](https://github.com/mbhesam/archiveAPI/blob/master/api/serializers.py) | <code>serializer classes</code> |
| [urls.py](https://github.com/mbhesam/archiveAPI/blob/master/api/urls.py)               | <code>url formats</code> |

</details>

<details closed><summary>tasks</summary>

| File                                                                                     | Summary                         |
| ---                                                                                      | ---                             |
| [tasks.py](https://github.com/mbhesam/archiveAPI/blob/master/tasks/tasks.py)             | <code>async and priodic tasks</code> |
| [apps.py](https://github.com/mbhesam/archiveAPI/blob/master/tasks/apps.py)               | <code>app file</code> |
| [tasks_utils.py](https://github.com/mbhesam/archiveAPI/blob/master/tasks/tasks_utils.py) | <code>required fucntion for runnig tasks</code> |
| [celery.py](https://github.com/mbhesam/archiveAPI/blob/master/tasks/celery.py)           | <code>celery configurations/code> |

</details>

<details closed><summary>archiveAPI</summary>

| File                                                                                    | Summary                         |
| ---                                                                                     | ---                             |
| [asgi.py](https://github.com/mbhesam/archiveAPI/blob/master/archiveAPI/asgi.py)         | <code></code> |
| [wsgi.py](https://github.com/mbhesam/archiveAPI/blob/master/archiveAPI/wsgi.py)         | <code></code> |
| [settings.py](https://github.com/mbhesam/archiveAPI/blob/master/archiveAPI/settings.py) | <code>basic settings and declerations</code> |
| [urls.py](https://github.com/mbhesam/archiveAPI/blob/master/archiveAPI/urls.py)         | <code>base urls format</code> |

</details>

<details closed><summary>download</summary>

| File                                                                            | Summary                         |
| ---                                                                             | ---                             |
| [admin.py](https://github.com/mbhesam/archiveAPI/blob/master/download/admin.py) | <code>administrator panel</code> |
| [views.py](https://github.com/mbhesam/archiveAPI/blob/master/download/views.py) | <code>view fucntions for download entities</code> |
| [utils.py](https://github.com/mbhesam/archiveAPI/blob/master/download/utils.py) | <code>required fucntion</code> |
| [apps.py](https://github.com/mbhesam/archiveAPI/blob/master/download/apps.py)   | <code>app file/code> |
| [urls.py](https://github.com/mbhesam/archiveAPI/blob/master/download/urls.py)   | <code>url formats</code> |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.10`

###  Installation

1. Clone the archiveAPI repository:

```sh
git clone https://github.com/mbhesam/archiveAPI
```

2. Change to the project directory:

```sh
cd archiveAPI
```

3. create virtual envirnoment and activate envirnoment:

```sh
python3.10 -m venv venv
source venv/bin/activate
```
4. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running archiveAPI

Use the following command to run archiveAPI:

```sh
python manage.py runserver
```

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/mbhesam/archiveAPI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/mbhesam/archiveAPI/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/mbhesam/archiveAPI/issues)**: Submit bugs found or log feature requests for Archiveapi.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/mbhesam/archiveAPI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/mbhesam/archiveAPI/blob/main/LICENSE) file.

---
