from fastapi import FastAPI
import subprocess
app = FastAPI()
@app.get("/")
def home():
    return {"message": "System Monitor API"}
@app.get("/cpu")
def cpu_useage():
    result = subprocess.getoutput("top -bn1 | grep 'Cpu(s)'")
    return {"cpu": result}
@app.get("/memory")
def memory():
    result_m = subprocess.getoutput("free -h")
    return {"memory": result_m}
@app.get("/disk")
def disk():
    result_d = subprocess.getoutput("df -h")
    return {"disk": result_d}
@app.get("/proccess")
def proccess():
    result_p = subprocess.getoutput("ps aux --sort=-%cpu | head ")
    return {"proccess": result_p}