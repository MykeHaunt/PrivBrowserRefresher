# PrivBrowserRefresher

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
