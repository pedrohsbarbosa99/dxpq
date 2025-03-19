<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="https://iili.io/3xVmRY7.png" width="40%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# Simple Python Wrapper for postgres connection.

<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/pedrohsbarbosa99/dxpq?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/pedrohsbarbosa99/dxpq?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/pedrohsbarbosa99/dxpq?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/pedrohsbarbosa99/dxpq?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview


**dxpq** is a simple and intuitive Python library designed to facilitate connection and interaction with PostgreSQL databases. It was created with the goal of providing an efficient way to perform common PostgreSQL operations, such as executing SQL queries, inserting and updating data, and managing transactions.

This library is lightweight and easy to use, allowing developers to quickly connect to the database without the complexity of setting up additional packages. With support for basic SQL commands and transactions, **dxpq** offers a clear and straightforward interface for working with PostgreSQL.

Ideal for those seeking a minimalist solution focused only on essential database operations, **dxpq** is perfect for projects that don't require large frameworks or heavy libraries but still need robust communication with PostgreSQL.


---

## Features

- **Database Connection**: Easily establish a connection to a PostgreSQL database using a connection string.

- **Cursor Management**: Create and manage cursors for executing SQL queries. Fetch all results or a single row, with support for different result formats (e.g., dictionary-style results).

- **SQL Execution**: Execute SQL queries and commands with parameters for secure and dynamic query building.

- **Context Manager Support**: The library supports context manager functionality, allowing the use of connections and cursors in `with` blocks for automatic resource management.

- **Cursor Types**: Supports different cursor types, such as dictionary-style results, for easier access to columns by name.

- **Clean Resource Management**: Automatically close database connections and cursors when done, either through context management or explicit cleanup with `close()` and `__del__` methods.



---

## Project Structure

```sh
└── dxpq/
    ├── README.md
    ├── dxpq
    │   ├── __init__.py
    │   ├── connection.py
    │   └── cursor.py
    ├── pyproject.toml
    ├── requirements-dev.txt
    └── requirements.txt
```

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build dxpq from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/pedrohsbarbosa99/dxpq
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd dxpq
    ```

3. **Install the dependencies:**
	**Using https://pypi.org/project/pip:**

	```sh
	❯ pip install -r requirements.txt, requirements-dev.txt
	```

### Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pip install dxpq
```

```python
import dxpq

connection = dxpq.Connection("postgresql://postgres:postgres@localhost:5432/postgres")
with connection.cursor() as cursor:
    cursor.execute("select 1")
    cursor.fetchall()
```

### Testing

Under development

---

## Roadmap

- [ ] **`Transaction support`**: Implement support to SQL commands
<!-- - [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three. -->

---

## Contributing

- **💬 [Join the Discussions](https://github.com/pedrohsbarbosa99/dxpq/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/pedrohsbarbosa99/dxpq/issues)**: Submit bugs found or log feature requests for the `dxpq` project.
- **💡 [Submit Pull Requests](https://github.com/pedrohsbarbosa99/dxpq/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/pedrohsbarbosa99/dxpq
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
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/pedrohsbarbosa99/dxpq/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=pedrohsbarbosa99/dxpq">
   </a>
</p>
</details>

---

## License

Dxpq is protected under the [MIT](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

---

<!-- ## Acknowledgments -->

<!-- - Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top) -->

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
