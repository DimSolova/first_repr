import subprocess

git_path = 'C:\\Program Files\\Git\\cmd\\git.exe'  # Путь к git.exe
directory_path = r'C:\Users\admin\PycharmProjects\First_reposit'

command = f'"{git_path}" status'
process = subprocess.Popen(command, cwd=directory_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()

if process.returncode == 0:
    print(output.decode())
else:
    print(f'Ошибка: {error.decode()}')