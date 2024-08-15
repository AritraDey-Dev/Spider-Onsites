import ping3
import sys
from statistics import mean

def ping_server(host, count=4):
    latencies = []
    lost_packets = 0

    print(f"Pinging {host} with {count} packets...")

    for i in range(count):
        latency = ping3.ping(host)
        if latency is None:
            print(f"Packet {i+1} lost.")
            lost_packets += 1
        else:
            print(f"Packet {i+1}: {latency*1000:.2f} ms")
            latencies.append(latency)

    if latencies:
        avg_latency = mean(latencies) * 1000
        print(f"\nAverage Latency: {avg_latency:.2f} ms")
    else:
        avg_latency = None
        print("\nNo packets were successfully received.")

    packet_loss = (lost_packets / count) * 100
    print(f"Packet Loss: {packet_loss:.2f}%")

    return avg_latency, packet_loss

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 latency_tester.py <server>")
        sys.exit(1)

    host = sys.argv[1]
    ping_server(host)
