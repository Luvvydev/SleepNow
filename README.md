# SleepNow One-Click, Uninterruptible macOS Sleep

---
## Motivation

macOS sleep is unreliable if you use a trackpad or a high-sensitivity mouse.

After clicking **Sleep**, tiny input drift often cancels the action. The system wakes itself immediately, forcing you to retry, stop moving your hands, or wait awkwardly. This is not user error. It is a known interaction between the window server and input devices.

This project exists to solve that exact problem, cleanly and permanently.
---

## What This Does

- Forces macOS to sleep immediately using the system power manager
- won't be canceled by accidental mouse or trackpad movement
- Requires no Terminal usage after setup

---

## AppleScript Source

on run  
  do shell script "/usr/bin/sudo /usr/bin/pmset sleepnow"  
end run

Save this in Script Editor as:
- File Format: Application
- Name: SleepNow

---

## Intended Audience

People who:
- Are tired of macOS canceling sleep
- Use sensitive mice or trackpads
- Want deterministic behavior
- Prefer simple, inspectable solutions
- Do not want background utilities or menu bar clutter

---

## License

Do whatever you want with this.

