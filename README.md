# PrivBrowserRefresher

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![License](https://img.shields.io/github/license/MykeHaunt/PrivBrowserRefresher)
![Status](https://img.shields.io/badge/status-Beta-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/MykeHaunt/PrivBrowserRefresher)
![Contributors](https://img.shields.io/github/contributors/MykeHaunt/PrivBrowserRefresher)
![Issues](https://img.shields.io/github/issues/MykeHaunt/PrivBrowserRefresher)
![Stars](https://img.shields.io/github/stars/MykeHaunt/PrivBrowserRefresher?style=social)
![Forks](https://img.shields.io/github/forks/MykeHaunt/PrivBrowserRefresher?style=social)

> **WORK IN PROGRESS BY: H. Pandit**

**PrivBrowserRefresher** is a cross-platform, Python-based tool to:
- Open a specified URL in multiple **private/incognito** windows or tabs  
- Support Safari (macOS), Chrome, Firefox and Edge  
- Auto-refresh each window/tab at **2 Hz** (Safari via AppleScript; see limitations below)

---

## Features

- **Cross-platform**: Windows, macOS, Linux  
- **Multi-browser**:  
  - **Safari** (private windows & 2 Hz refresh via AppleScript; macOS only)  
  - **Chrome**, **Firefox**, **Edge** (private mode launch via CLI flags)  
- **Flexible UI**: Prompt for URL, count, windows vs. tabs, and browser choice  
- **Auto-refresh**: 2 Hz reloads for Safari; instructions for other browsers  

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/PrivBrowserRefresher.git
   cd PrivBrowserRefresher
