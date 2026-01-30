# 🧰 PyHund 8.0 Toolbox

>Welcome to the **PyHund 8.0 Toolbox** documentation. This suite provides specialized utilities designed to enhance the capabilities of the PyHund ecosystem, offering powerful fingerprinting and automation solutions for developers and security researchers.

The toolbox currently includes:
*   **PyHunter**: A website fingerprinting and analysis tool.
*   **AutoMan**: A generator for tailored Manifest files.


## 🕵️ PyHunter

>**PyHunter** is the reconnaissance engine of PyHund. It is designed to fingerprint websites and generate a JSON representation of their behavior, which is critical for configuring PyHund's main operations.

### Key Features

*   **Smart User-Agent Rotation**: Automatically detects blocked connections (403/429) and rotates through a curated list of modern User-Agents to bypass basic restrictions.
*   **Verification Analysis**: intelligently determines how a target website differentiates between valid and invalid user profiles. It checks:
    *   **Status Codes**: (e.g., 200 vs 404)
    *   **URL Redirections**: Detects if invalid users are redirected to a different page.
    *   **Content Length**: Compares response sizes to identify subtle differences.
    *   **Content Patterns**: Looks for specific error strings (like "404").
*   **Cookie & Header Mapping**: Automatically captures session cookies and headers required for valid requests.

### CLI Usage

You can run PyHunter directly from the command line to analyze a target.

```html
# Basic Usage
python3 tools/pyhunter.py <url> <valid_username>

# Verbose Mode (Recommended for debugging)
python3 tools/pyhunter.py <url> <valid_username> /v
```

> [!TIP]
> **URL Format**: Ensure your URL contains placeholders (e.g., `{}`) if the tool expects to inject the username, or follow standard PyHunter URL formatting conventions.

---

## 🤖 AutoMan

>**AutoMan** is the architect of the suite. It is built to streamline the creation of custom Manifest files, allowing for precise configuration of PyHund operations tailored to specific targets.

*   **Manifest Building**: Automates the construction of complex configuration files.
*   **Flexible Integration**: Designed to be integrated into larger workflows that require dynamic configuration generation.

> [!NOTE]
> AutoMan is currently in active development. The class structure is available for import, with method implementations arriving in upcoming updates.

---

## 👨‍💻 Developer's Guide

This toolbox is built with flexibility in mind. Both `PyHunter` and `AutoMan` are implemented as Python classes, making them easy to import and extend in your own projects.

### Importing the Tools

Assuming your project structure includes the `tools` directory:

```python
from tools.pyhunter import PyHunter
from tools.automan import AutoMan
```

### PyHunter API Reference

#### `class PyHunter(url: str)`

Initialize a new PyHunter instance.

*   **Parameters**:
    *   `url` (str): The target URL pattern.

#### `connect(url: str) -> Response`

Attempt to establish a connection to the given URL. Handles session management and User-Agent rotation automatically if blocks are detected.

*   **Returns**: `requests.Response` object or `None` if connection fails.

#### `analyse_verification_method(valid_user: str, invalid_user: str = "...") -> dict`

The core analysis method. Compares the server's response for a known valid user against a known invalid user to determine the best way to verify account existence.

*   **Parameters**:
    *   `valid_user` (str): A username known to exist on the target.
    *   `invalid_user` (str): A username known NOT to exist (defaults to a random string).
*   **Returns**: A dictionary containing the analysis results, including detected headers, cookies, and the identifying criteria (status code, length, etc.).

**Example**:

```python
from tools.pyhunter import PyHunter

# Initialize with a URL
hunter = PyHunter("https://example.com/user/{}")

# Run analysis
result = hunter.analyse_verification_method("admin")

if "Error" not in result:
    print(f"Detection Method: {result['check_type']}")
    print(f"Criteria: {result['criteria']}")
else:
    print("Analysis failed.")
```

### AutoMan API Reference

#### `class AutoMan()`

Initialize a new AutoMan instance.

*   **Usage**: Currently acts as a base structure for future manifest generation logic.

```python
from tools.automan import AutoMan

builder = AutoMan()
# Future methods will be called here to build manifests
```
