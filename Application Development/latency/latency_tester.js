const ping = require('ping');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function pingServer(host, count = 4) {
    let latencies = [];
    let lostPackets = 0;

    console.log(`Pinging ${host} with ${count} packets...`);

    const promises = Array.from({ length: count }, (_, i) => {
        return ping.promise.probe(host)
            .then(res => {
                if (res.alive) {
                    console.log(`Packet ${i + 1}: ${res.time} ms`);
                    latencies.push(parseFloat(res.time));
                } else {
                    console.log(`Packet ${i + 1} lost.`);
                    lostPackets++;
                }
            });
    });

    Promise.all(promises).then(() => {
        if (latencies.length > 0) {
            const avgLatency = latencies.reduce((a, b) => a + b, 0) / latencies.length;
            console.log(`\nAverage Latency: ${avgLatency.toFixed(2)} ms`);
        } else {
            console.log("\nNo packets were successfully received.");
        }

        const packetLoss = (lostPackets / count) * 100;
        console.log(`Packet Loss: ${packetLoss.toFixed(2)}%`);

        rl.close();
    });
}

rl.question("Enter server IP or hostname: ", (host) => {
    pingServer(host);
});
