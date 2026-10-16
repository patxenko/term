import subprocess
import time

def vibrar(ms):
    subprocess.run(["termux-vibrate", "-d", str(ms)])

for _ in range(3):
    vibrar(150)
    time.sleep(0.3)