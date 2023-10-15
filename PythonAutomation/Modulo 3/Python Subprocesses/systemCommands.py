import subprocess
subprocess.run(["date"])#Obtenemos la fecha y hora del sistema
subprocess.run(["sleep", "2"])#Con sleep el proceso tarda el tiempo indicado en volver a estar operativo
result = subprocess.run(["ls" ,"this_file_does_not_exist"])
