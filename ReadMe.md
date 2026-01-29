# PyHund
![Version](https://img.shields.io/badge/version-R8.0-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-WIP-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-InDev-orange?style=for-the-badge)

> **The extensible, lightweight, and modern user-instance hunter**

## 🚀 Overview
**PyHund** is a next-generation OSINT tool designed for ease of use, scalability and results that matter. It searches for user-instances across a vast network of websites and delivers simple, easy to use reports right to your doorstep ( *or screen most likely* ).

In this new version, **PyHund** has been built to be modular, extensible and data-forward. With refined collection and analytics systems, as well as a robust plugin arcitecture, you can drop in new modules to make your application work for you!

### ✨ Key Features
- **✨ Need for Speed**: Requests and parsing methodology has been optimized and is now multi-threaded
- **🧩 Plugin Logic**: Plugins allow for endless support and modification of program logic
- **🛠️ Zero Config**: Works out of the box
- **🛡️ Bot Evasion**: Makes use of smart headers, rotation and adaptive connections to evade bot detection
- **🔧 Developer Tools**: Includes tools such as `PyHunter` and `AutoMan` for those wanting a more tailored experiance

## 📦 Installation

Get up and running in seconds.

```bash
# Clone the repository
git clone https://github.com/your-repo/PyHund.git
cd PyHund

# Install dependencies
pip3 install -r requirements.txt

# Run the installer
chmod +x installer.sh
sudo ./installer.sh
```

## 🎮 Quick Start

Huting user-instances is as simple as:

```html
pyhund <username>
```

**Example**
```bash
pyhund JohnDoe
```

### Multiple Targets

```bash
pyhund JohnDoe "Mark Markson" JaneDoe
```

## ⚙️ Advanced Usage

Customize your hunt with powerful arguments.

| Argument | Description |
| :--- | :--- |
| `/verbose`, `/v` | Enable verbose output for program execution |
| `/outfile:<path>`, `/o:<path>` | Sets expected output file in the form of `name.ext`. *PyHund* will then use the `ext` provided ( *json / yaml / txt*( **Default** ) */ html / pdf* ) to inform the output format you want |
| `/threads:<count>`, `/t:<count>` | Set maximum number of threads to be issued during program execution |

**Example**
```bash
pyhund @usernames.txt /v /t:20 /o:scan.html
```
> **Note**: when `@<filepath>` provided, program will read both command line usernames as well as all usernames provided in passed in file.

## 🛠️ Developer Tools: PyHunter
Included by deafult is **PyHunter**, a powerful utility for developers to reverse-engineer site verification methods for user-instance authentication.

### Usage
```html
python3 pyhunder.py <url> <valid_username> [/v]
```

**Features:**
- **Auto-Discovery**: detemines if a site checks users by Status Code, Content Length, or URL.
- **Smart Rotation**: Automatically rotates User-Agents if blocked.
- **Response Mapping**: Generates a JSON config ready to paste into your plugin.
- **Cookie Check**: Automatically tests if cookies are required or can be ignored.

## 🛠️ Developer Tools: AutoMan
Included by default is **AutoMan**, a quality of life tool for those that want to build their own site manifests to be used by **PyHund**.

### Usage
```html
python3 automan.py <mode> @<sitelist_path> 
```
