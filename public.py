from pyngrok import ngrok
import subprocess
import time

subprocess.Popen([
    "uvicorn",
    "app.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
])

time.sleep(3)

url = ngrok.connect(8000)

print("NovaChat Public URL:")
print(url)

while True:
    time.sleep(10)
