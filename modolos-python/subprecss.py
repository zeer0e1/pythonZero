import subprocess

import sys


print(sys.platform)

cmd = ['ping', '127.0.0.1']

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding='cp850'
)
print()
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)
