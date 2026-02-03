This repo documents a macOS one click sleep shortcut.

Command used:
sudo /usr/bin/pmset sleepnow

Optional: wrap in Script Editor and save as Application.

SleepNow.applescript: 
`on run
  do shell script "/usr/bin/sudo /usr/bin/pmset sleepnow"
end run`
