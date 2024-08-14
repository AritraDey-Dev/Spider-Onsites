# Packet Analyzing using Wireshark

## Problem Statement

Acme Corp's security team has reached out to you about a recent cybersecurity incident. They believe a malicious entity has managed to access a shared folder that stores confidential files. Threat intelligence has revealed an active dark web forum where disgruntled employees offer access to their employer's internal network for financial rewards. One of Acme Corp's employees has been identified as offering to provide access to a low-privileged domain-joined user for 10K in cryptocurrency.

Your task is to find details about that very user that the internal employee has created. To assist in your investigation, Acme Corp's security team has provided a zipped pcap file containing network traffic data. Analyze the traffic, find the out user and tell the password for it so that preventive measures can be taken.

## **Tasks**

- Download and extract the zipped pcap file.
- Analyze the network traffic to identify any suspicious activity related to user addition.
- Locate the protocol and specific packets where the attacker might have stored the password.
- Determine the user and stored password.
- Submit the password to successfully complete the challenge.

## Resources and clues:

- [Find hidden details](https://en.wikipedia.org/wiki/Steganography)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Wireshark Download](https://www.wireshark.org/download.html)
- [Documentation and user's guide](https://www.wireshark.org/docs/wsug_html_chunked/)