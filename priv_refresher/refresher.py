#!/usr/bin/env python3

import subprocess, time, shutil, sys, platform

def prompt():
    url = input("Enter the full URL (e.g., https://example.com): ").strip()
    try:
        count = int(input("How many private windows/tabs to open? "))
    except ValueError:
        print("Invalid number.")
        sys.exit(1)
    mode = input("Open in (W)indows or (T)abs? [W/T]: ").strip().lower()
    browser = input("Browser (safari / chrome / firefox / edge): ").strip().lower()
    return url, count, mode, browser

def open_safari_private(url, count):
    for i in range(count):
        script = f'''
        tell application "Safari"
            activate
            tell application "System Events"
                keystroke "n" using {{shift down, command down}}
            end tell
            delay 1
            set URL of front document to "{url}"
        end tell'''
        subprocess.run(["osascript", "-e", script])
        time.sleep(1)

def refresh_safari_2hz():
    script = '''
    repeat
        tell application "Safari"
            repeat with w in windows
                repeat with t in tabs of w
                    tell t to do JavaScript "location.reload();"
                end repeat
            end repeat
        end tell
        delay 0.5
    end repeat'''
    subprocess.Popen(["osascript", "-e", script])

def get_cmd(browser, url, mode):
    if browser=="chrome":
        exe = shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chrome.exe")
        return [exe, "--incognito", url] if exe else None
    if browser=="firefox":
        exe = shutil.which("firefox") or shutil.which("firefox.exe")
        if not exe: return None
        return [exe, "--private-window", url] if mode=="w" else [exe, "--new-tab", url, "--private-window"]
    if browser=="edge":
        exe = shutil.which("msedge") or shutil.which("msedge.exe")
        return [exe, "--inprivate", url] if exe else None
    return None

def main():
    url, count, mode, browser = prompt()
    os_name = platform.system()
    if browser=="safari":
        if os_name!="Darwin":
            print("Safari support requires macOS."); sys.exit(1)
        open_safari_private(url, count)
        print("Starting 2 Hz auto-refresh on Safari…")
        refresh_safari_2hz()
    else:
        for i in range(count):
            cmd = get_cmd(browser, url, mode)
            if not cmd:
                print(f"Cannot find {browser} executable."); break
            subprocess.Popen(cmd)
            time.sleep(1)
        print("For auto-refresh on Chrome/Firefox/Edge, please install a browser extension or use DevTools protocols.")

if __name__ == "__main__":
    main()