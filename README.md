**IP Validator**

A Python script to validate IPv4 addresses using regular expressions.

**Features**

- Validates IPv4 addresses with optional subnet masks
- Allows network IPs (e.g., 10.10.10.0) only with subnet masks
- Allows non-network IPs (e.g., 10.10.10.1) with or without subnet masks

**Usage**

1. Clone the repository: `git clone https://github.com/VivekRavichandran07/Ipv4-Regex.git
2. Run the script: python ipvalidator.py
3. Test IP addresses using valid_ips.txt and invalid_ips.txt files

**Requirements**

- Python 3.x

**Regex Pattern**

^((\d{1,3}\.){3}(?!0)\d{1,3}(\/\d{1,2})?|(\d{1,3}\.){3}0(\/\d{1,2}))$

**Files**

- ipvalidator.py: Python script
- valid_ips.txt: Test file with valid IP addresses
- invalid_ips.txt: Test file with invalid IP addresses

**Contributing**

Pull requests and issues welcome!
