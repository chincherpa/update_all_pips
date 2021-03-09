
if 1:
  import os
  import subprocess

  pip_export_file = "pip_freeze.txt"

  here = os.path.dirname(os.path.realpath(__file__))
  os.chdir(here)
  subprocess.call("pip freeze > " + pip_export_file, shell=True)

  with open(pip_export_file, "r") as f:
    pcks = f.read().splitlines()

  new_content = []
  for pck in pcks:
    package_name = pck.partition("==")[0]
    print(package_name)

  # geht nicht, hängt
    # subprocess.call(f"pip install {package_name} --upgrade", shell=True)
    new_content.append(f"pip install {package_name} --upgrade")

  # write batch file
  with open("update_all_pips.bat", "w+") as f:
    for line in new_content:
      f.write(line + "\n")

  subprocess.call("update_all_pips.bat", shell=True)

#--------------------------------------------
if 0:
  import subprocess

  proc = subprocess.Popen("pip freeze",stdout=subprocess.PIPE)
  for line in iter(proc.stdout.readline,''):
    if len(line) > 0:
      subprocess.call(b'pip install %s --upgrade'.format(line.partition("==")[0]), shell=True)
    else:
      break