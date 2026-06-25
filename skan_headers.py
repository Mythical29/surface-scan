import requests
import socket
import sys

def audit_host(domain):
    print(f"[*] Resolving infrastructure mapping for: {domain}")
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[+] Target IP resolved: {ip_address}")
    except socket.gaierror:
        print("[-] Critical: DNS resolution failed.")
        return

    url = f"https://{domain}"
    security_headers = {
        'Strict-Transport-Security': 'Mitigates MITM/Session Hijacking',
        'X-Frame-Options': 'Prevents Clickjacking attacks',
        'X-Content-Type-Options': 'Prevents MIME-sniffing exploits',
        'Content-Security-Policy': 'Mitigates XSS and data injection'
    }

    print(f"[*] Inspecting HTTP security boundaries at {url}...")
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        for header, description in security_headers.items():
            if header in response.headers:
                print(f"  [SECURE] {header} is configured properly.")
            else:
                print(f"  [MISCONFIGURED] Missing {header} ({description})")
    except requests.exceptions.RequestException as e:
        print(f"[-] Network connection error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 recon_headers.py <subdomain.domain.com>")
        sys.exit(1)
    audit_host(sys.argv[1])
