# Simple Network Latency Tester

## Task
Create a tool that measures the latency between the client and a specified server.

## Objective
The objective of this project is to understand network latency and packet transmission by measuring the round-trip time of packets sent to a target server.

## Implementation Steps
1. **Use ICMP (Ping) Requests:**
   - Implement functionality to send ICMP (ping) requests to measure the round-trip time to a target server.

2. **Display Results:**
   - Display the results of the latency tests, including:
     - Average latency
     - Packet loss percentage

3. **User Input for Server Selection:**
   - Allow users to specify different servers for testing by inputting the server's IP address or hostname.

## Tools
- **Programming Languages:**
  - Python with the [ping3](https://pypi.org/project/ping3/) library.
  - Node.js with the [ping](https://www.npmjs.com/package/ping) library.

