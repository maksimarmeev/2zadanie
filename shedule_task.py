import subprocess
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(base_dir, 'import_requests.py')
python_exe = sys.executable
task_name = "Collectdatalibrary"
cmd = [
    "schtasks",
    "/create",
    "/tn", task_name,
    "/tr", f'"{python_exe}" "{script_path}"',
    "/sc", "daily",
    "/st", "07:00",
    "/f" 
]

try:
    subprocess.run(cmd, check=True)
    print("Process added to Sheduler")
except subprocess.CalledProcessError as e:
    print(f'Error {e} during adding')
