import requests

def check_subdomain(subdomain, domain):
    try:
        # HTTP isteği yaparak subdomain'i kontrol et
        response = requests.get(f"http://{subdomain}.{domain}")
        if response.status_code == 404:
            print(f"[+] Subdomain bulundu: {subdomain}.{domain}")
    except requests.exceptions.RequestException:
        # Hata durumunda subdomain takeover kontrolü yap
        try:
            cname = socket.gethostbyname(f"{subdomain}.{domain}")
            if cname.endswith("amazonaws.com"):
                print(f"[+] Subdomain takeover yapılabilecek: {subdomain}.{domain}")
        except socket.gaierror:
            pass

def find_subdomains(domain):
    subdomains = ["www"]

    while subdomains:
        subdomain = subdomains.pop(0)
        check_subdomain(subdomain, domain)

        # Alt subdomainleri kontrol etmek için ekleyin
        new_subdomains = [f"{subdomain}.{sub}" for sub in subdomains_list]
        subdomains.extend(new_subdomains)

# Ana kod
domain = "example.com"  # Buraya araştırılacak domaini girin
subdomains_list = ["mail", "admin", "test"]  # İstediğiniz alt subdomainleri listeye ekleyin
find_subdomains(domain)
