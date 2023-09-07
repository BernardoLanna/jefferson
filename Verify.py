import psutil
import subprocess
import time

time_in_seconds = 5 # Se quiser testar diminua esse numero (sempre em segundos)

pid = 4566 #substitui pelo PID
file_path = "/home/jefferson/mplayer.sh"

def is_program_running(pid_name):
    for process in psutil.process_iter(['pid']):
        if process.info['pid'] == pid_name:
            return True
    return False



while True :
    time.sleep(time_in_seconds)
    if is_program_running(pid):
        print(f"mplayer is running.")

    else:
        print(f"mplayer is not running.")
        subprocess.Popen(['xdg-open', file_path])  #coloque aqui o local do arquivo que deseja ser executado
        print(f"mplayer was opened successfully")