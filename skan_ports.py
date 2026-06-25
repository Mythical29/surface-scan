import socket
import sys

def banner_grab(target_host):
    target_ports = [21, 22, 80, 443, 8080]
    print(f"[*] Mapping network ports and checking flags on: {target_host}")
    
    for port in target_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        try:
            print(f"[*] Scanning port {port}...")
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"  [+] Port {port} is OPEN.")
                # Send basic payload to trigger banner response if web/ftp/ssh
                s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = s.recv(1024)
                if banner:
                    clean_banner = banner.decode('utf-8', errors='ignore').split('\n')[0].strip()
                    print(f"    -> Banner Grabbed: {clean_banner}")
            s.close()
        except Exception as e:
            print(f"  [-] Connection dropped on port {port}: {e}")
            s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 recon_ports.py <domain_or_ip>")
        sys.exit(1)
    banner_grab(sys.argv[1])
