# my-skan-tools

Just a collection of python scripts I put together to speed up my asset mapping and info-gathering steps. They handle subdomain dumping, quick header checks, and basic port verification straight from the terminal so I don't have to keep doing them manually.

## What's in here:

### 1. Subdomain Scraper (`skan_subdomains.py`)
Gathers subdomains for a target by pulling json data directly from crt.sh certificate logs. It filters out duplicate names and wildcards, then spits out a clean list of unique hosts. Completely passive, doesn't touch the target network at all.
* **Run it:** `python3 skan_subdomains.py target.com`

### 2. Header Audit (`skan_headers.py`)
Grabs the IP address for whatever host you give it, connects over HTTPS, and checks if the server is missing standard security controls like HSTS, CSP, or X-Frame-Options. Useful for spotting quick misconfigurations or clickjacking paths.
* **Run it:** `python3 skan_headers.py dev.target.com`

### 3. Port Checker (`skan_ports.py`)
A straightforward raw socket script that tests if standard ports (21, 22, 80, 443, 8080) are open. If a port answers, it sends a quick request string to see if the service leaks a version banner.
* **Run it:** `python3 skan_ports.py 192.168.1.1` or `python3 skan_ports.py target.com`
