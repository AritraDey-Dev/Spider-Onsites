# Intrusion Detection System

## Problem Statement 
In today's interconnected digital landscape, where organizations rely heavily on networked systems and data, the security of these networks is paramount. Intrusion Detection Systems (IDS) play a crucial role in safeguarding these networks by actively monitoring and analyzing network traffic for malicious activities and security breaches. So this task requires you to design and implement an Intrusion Detection System (IDS) using Snort to monitor network traffic, detect potential intrusions, and generate alerts.


## **Tasks**:

### Setup Snort IDS
 * Install Snort on a Linux-based system(e.g. Ubuntu)
 * Configure Snort to monitor network interface and detect various types of network traffic.

### Rule Creation
 * Write Snort Rules to detect common network activities:
    i. HTTP requests
    ii. FTP/SSH login attempts
    iii. ICMP request (ping sweeps)
    iv. Download attempts of files with specific extensions (e.g. '.exe')

### Network Setup
 * Install Apache HTTP server on snort machine.
 * Host the web server on the machine with a file named "example.txt".

### Testing
 * A series of tests will be performed to validate the efficitveness of IDS:
    i. Accessing web pages.
    ii. Attempt to download files.
    iii. Accessing FTP/SSH services and login attempts.
    iv. ICMP ping sweeps.
    v. Port Scanning.
    vi. DOS attacks (syn or ping flood).


## Resources
* Snort download: [Snort Documnetation](https://www.snort.org/)
* Snort and Snort Rules: [snort use cases](https://www.crowdstrike.com/cybersecurity-101/threat-intelligence/snort-rules/)
* Snorpy - a simple Snort rule creator: [Snorpy for web](http://www.cyb3rs3c.net/)
* Snort Rules Creation: [Custom Rules creation](https://youtu.be/pjoZfOLMDgU?si=Vem3tgBjHHloKOid)
* Configure Apache: [Apache Documentation](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview)

