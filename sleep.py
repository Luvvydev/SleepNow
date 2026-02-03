import time
import subprocess

DELAY_SECONDS = 3  # set to 2 if you want
time.sleep(DELAY_SECONDS)

subprocess.run(["/usr/bin/pmset", "sleepnow"], check=True)

