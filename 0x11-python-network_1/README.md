# 0x11-python-network_1

#### Repository Description
This repository holds a collection of Python scripts demonstrating HTTP requests, response handling, and working with web APIs. These scripts perform various network-related tasks using Python libraries like `urllib` and `requests`, showcasing URL fetching, response header access, POST request handling, and HTTP error management.

#### Requirements and Guidelines
- **Environment:** Scripts are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- **File Structure:** All scripts end with a new line and start with `#!/usr/bin/python3`.
- **README:** A mandatory `README.md` file at the repository root contains a description.
- **Coding Style:** Adherence to `pycodestyle (version 2.8.*)` coding standards.
- **File Execution:** All scripts are executable.
- **Documentation:** Each module contains accessible documentation using `python3 -c 'print(__import__("my_module").__doc__)'`.
- **Dictionary Access:** Utilization of `get` to access dictionary values by key.
- **Module Execution:** Code doesn't execute when imported (`if __name__ == "__main__":`).
- **File Length:** File length evaluated using `wc`.

#### Tasks Overview
- **Tasks 0-3:** Using `urllib` to perform URL fetching, access response headers, and handle HTTP errors.
- **Tasks 4-7:** Similar tasks as before but using the `requests` package instead of `urllib`.
- **Task 8:** Sending POST requests and handling responses for search queries using the JSON API.
- **Task 9:** Accessing GitHub user information via Basic Authentication and personal access tokens through the GitHub API.
- **Task 10 (Advanced):** Using the GitHub API to list recent commits in a repository based on specified guidelines.

#### File Details
Each Python script corresponds to a specific task outlined in the requirements and guidelines. Scripts are organized based on task numbers.

Referencing the task numbers and associated filenames will help understand each script's functionality and execution. Adhering to the specified guidelines and requirements for each task while working with these scripts is essential.

Note: For scripts involving APIs or multiple requests, consider rate limits for unauthenticated requests (60 requests per hour per IP).
