import re

ip_regex = r"^((\d{1,3}\.){3}(?!0)\d{1,3}(\/\d{1,2})?|(\d{1,3}\.){3}0(\/\d{1,2}))$"

def validate_ip(ip_address):
    return bool(re.match(ip_regex, ip_address))

# Test IP addresses from file
def test_ips(file_path):
    with open(file_path, 'r') as f:
        for ip in f.readlines():
            ip = ip.strip()
            result = validate_ip(ip)
            print(f"{ip}: {result}")

# Run tests
test_ips('valid_ips.txt')
test_ips('invalid_ips.txt')