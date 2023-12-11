# Simple Port Scan Program

## Overview

This is a simple Python script for port scanning. The program uses sockets to check the status of ports within a specified range on a target IP address.

## Features

- Scan a range of ports on a target IP address.
- Identify open and closed ports.
- Lightweight and easy to use.

## Usage


1. **Run the Script:**

    ```bash
    python SimplePortScanner.py
    ```

2. **Input Information:**

    - Enter the target IP address when prompted.
    - Input the start and end of the port range.

3. **Review Results:**

    The script will display the status of each port in the specified range.

## Example

```bash
Give me your target IP for scan: 192.168.1.1
Start of range: 1
End of range: 100

Port 22 is OPEN
Port 80 is OPEN
Port 443 is closed
... (other ports)
