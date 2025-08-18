const { exec } = require('child_process');

const randomArgoPort = Math.floor(Math.random() * (65000 - 2000 + 1)) + 2000;
console.log(`Generated random port for ARGO_PORT: ${randomArgoPort}`);

const cfip = 'joeyblog.net';
console.log(`Using CFIP (优选域名): ${cfip}`);

const command = `CFIP=${cfip} ARGO_PORT=${randomArgoPort} bash <(curl -Ls https://main.ssss.nyc.mn/sb.sh)`;

console.log('Executing command...');
console.log('---');

const child = exec(command, { shell: '/bin/bash' });

child.stdout.on('data', (data) => {
  process.stdout.write(data);
});

child.stderr.on('data', (data) => {
  process.stderr.write(data);
});

child.on('close', (code) => {
  console.log('---');
  console.log(`Script finished with exit code ${code}`);
});

child.on('error', (err) => {
    console.error('Failed to start subprocess.', err);
});
