import subprocess
import random
import sys

random_argo_port = random.randint(2000, 65000)
print(f"Generated random port for ARGO_PORT: {random_argo_port}")

cfip = 'joeyblog.net'
print(f"Using CFIP (优选域名): {cfip}")

command = f"CFIP={cfip} ARGO_PORT={random_argo_port} bash <(curl -Ls https://main.ssss.nyc.mn/sb.sh)"

print('Executing command...')
print('---')

try:
    process = subprocess.Popen(
        command,
        shell=True,
        executable='/bin/bash',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()

    for line in process.stderr:
        sys.stderr.write(line)
        sys.stderr.flush()

    process.wait()
    
    print('---')
    print(f"Script finished with exit code {process.returncode}")

except FileNotFoundError:
    print("Error: '/bin/bash' not found. This script requires a bash shell to run.")
except Exception as e:
    print(f"An error occurred: {e}")
