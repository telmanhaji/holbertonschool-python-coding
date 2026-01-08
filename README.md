This is a professional, well-structured `README.md` designed specifically for your GitHub repository. It highlights the technical constraints of the project while clearly explaining the cyber security concepts involved.

---

# Introduction to Cyber Security: Nmap Live Host Discovery

## 📌 Project Overview

This repository contains a series of scripts developed for the **Introduction to Cyber Security** curriculum. The primary focus is on **Nmap Live Host Discovery**, exploring how to identify active devices within a network using various scanning techniques.

The project transitions from basic network enumeration to advanced ICMP, TCP, and UDP discovery methods, all while adhering to strict scripting constraints.

## 🎯 Learning Objectives

By the end of this project, the following concepts are mastered:

* **Nmap Fundamentals:** Understanding what Nmap is and how its scanning engine operates.
* **Network Enumeration:** How to define targets and manage subnetworks.
* **Host Discovery Techniques:**
* **ARP Scanning:** Identifying local devices via Address Resolution Protocol.
* **ICMP Scans:** Utilizing Echo, Timestamp, and Address Mask requests.
* **TCP Pings:** Using SYN and ACK packets to bypass certain firewall configurations.
* **UDP Pings:** Discovering hosts by sending packets to specific ports.


* **Detection:** Identifying what Nmap can detect (OS, services, active hosts).

---

## 🛠️ Requirements & Constraints

To ensure code quality and consistency, all scripts follow these strict guidelines:

* **Environment:** Tested on **Kali Linux**.
* **Format:** All scripts are exactly **two lines** long.
* **Shebang:** The first line is always `#!/bin/bash`.
* **Scripting Style:** * No backticks (```), `&&`, `||`, or `;`.
* The IP range is passed as an argument (`$1`).
* `$1` is used **without quotes** as per project requirements.


* **Coding Standards:** Scripts are compliant with the **Betty style** (using `betty-style.pl` and `betty-doc.pl`).

---

## 🚀 Scan Techniques Covered

| Scan Type | Description | Nmap Flag |
| --- | --- | --- |
| **ARP Scan** | Finds hosts on a local ethernet network. | `-PR` |
| **ICMP Echo** | The classic "ping" to see if a host is up. | `-PE` |
| **ICMP Timestamp** | Uses ICMP type 13 to bypass basic filters. | `-PP` |
| **ICMP Mask** | Uses ICMP type 17 to request subnet masks. | `-PM` |
| **TCP SYN Ping** | Sends an empty SYN flag to elicit a response. | `-PS` |
| **TCP ACK Ping** | Sends an ACK packet to determine host state. | `-PA` |
| **UDP Ping** | Sends UDP packets to specific ports. | `-PU` |

---

## 📂 Repository Structure

| File | Task |
| --- | --- |
| `0-nmap_ping_scan.sh` | Basic Nmap discovery. |
| `1-nmap_arp_scan.sh` | Local network ARP discovery. |
| `2-nmap_icmp_echo.sh` | ICMP Echo based discovery. |
| ... | ... |

## 💻 Usage

To run any of the discovery scripts, ensure the file is executable and provide a target IP or range:

```bash
# Make the script executable
chmod +x <filename>.sh

# Run the script with a target range
./<filename>.sh 192.168.1.0/24

```

---

## 👨‍💻 Author

* **Project by:** Yosri Ghorbel
* **Level:** Amateur (Cyber Security Student)
* **Weight:** 2

---

*This project is part of a curriculum focused on ethical hacking and network security. Use these tools responsibly and only on networks you have permission to scan.*

Would you like me to help you write the specific 2-line Bash scripts for any of these Nmap scan types?
