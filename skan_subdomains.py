import requests
import sys
import json

def fetch_subdomains(domain):
    print(f"[*] Querying Certificate Transparency logs for: {domain}")
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("[-] Error: Unable to reach crt.sh API.")
            return
        
        data = response.json()
        subdomains = set()
        
        for entry in data:
            name = entry['name_value']
            # Clean up wildcards and split multi-domain certificates
            for sub in name.split('\n'):
                if not sub.startswith('*') and domain in sub:
                    subdomains.add(sub.strip())
                    
        print(f"[+] Found {len(subdomains)} unique subdomains:")
        for sub in sorted(subdomains):
            print(f"  - {sub}")
            
    except Exception as e:
        print(f"[!] Target API error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 recon_subdomains.py <domain.com>")
        sys.exit(1)
    fetch_subdomains(sys.argv[1])
