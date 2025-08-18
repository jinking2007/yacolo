import subprocess
import random
import sys
import uuid
import socket

def find_free_port(start_port=2000, end_port=65000):
    """
    Finds an available TCP port in a given range.
    """
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                # If bind is successful, the port is free
                return port
            except OSError:
                # Port is already in use
                continue
    # If no free port is found in the range
    return None

# 1. 查找一个空闲端口
argo_port = find_free_port()
if argo_port is None:
    print("Error: Could not find any free port between 2000 and 65000.")
    sys.exit(1)
print(f"Found a free port for ARGO_PORT: {argo_port}")

# 2. 设置优选域名
cfip = 'joeyblog.net'
print(f"Using CFIP (优选域名): {cfip}")

# 3. 生成随机UUID
random_uuid = str(uuid.uuid4())
print(f"Generated random UUID: {random_uuid}")

# 4. 构造完整的 shell 命令
command = f"UUID={random_uuid} CFIP={cfip} ARGO_PORT={argo_port} bash <(curl -Ls https://main.ssss.nyc.mn/sb.sh)"

print('Executing command...')
print('---')

try:
    # 5. 执行命令
    process = subprocess.Popen(
        command,
        shell=True,
        executable='/bin/bash',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    # 实时打印标准输出
    for line in process.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()

    # 实时打印标准错误
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
