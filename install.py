import os

os.system("wsl --install")
os.system("python -m venv venv")
os.system("source venv/bin/activate")
os.system("python.exe -m pip install --upgrade pip")
os.system("pip install -r requirements.txt")