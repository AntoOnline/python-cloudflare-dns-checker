import configparser
import dns.resolver
import dns.rdatatype
import requests
import sys

# Load config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get Cloudflare API settings from config.ini
api_token = config['CLOUDFLARE']['api_token']

# Cloudflare API endpoint to retrieve all zones
api_endpoint = 'https://api.cloudflare.com/client/v4/zones'

# Set headers for Cloudflare API request
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

timeout = int(config['DNS']['timeout'])

# Get DNS resolver settings from config.ini
resolver = dns.resolver.Resolver()
resolver.timeout = timeout
resolver.nameservers = [config['DNS']['nameserver']]

# Make request to Cloudflare API
response = requests.get(api_endpoint, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Get list of zones from Cloudflare API response
    zones = response.json()['result']

    # Loop through zones and print details
    for zone in zones:
        domain = zone['name']
        zone_id = zone['id']

        print(f'\n--')
        print(f'Zone for {domain} (zone_id: {zone_id})')
        print(f'--')

        # Cloudflare API endpoint to retrieve DNS records for zone
        dns_api_endpoint = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A'

        # Make request to Cloudflare API to retrieve A records for zone
        dns_response = requests.get(dns_api_endpoint, headers=headers)

        # Check if request was successful
        if dns_response.status_code == 200:
            # Get list of A records from Cloudflare API response
            a_records = dns_response.json()['result']

            # Loop through A records and print details
            for a_record in a_records:
                name = a_record['name']
                value = a_record['content']
                ttl = a_record['ttl']

                # DNS lookup for A record
                try:
                    a_answer = resolver.resolve(
                        name, rdtype=dns.rdatatype.A)
                    ip = str(a_answer[0])
                    print(f'- IPv4 address for {name}: {ip}')
                except:
                    print('\033[91m- Error: DNS lookup failed\033[0m')

                # DNS lookup for AAAA record
                try:
                    aaaa_answer = resolver.resolve(
                        name, rdtype=dns.rdatatype.AAAA)
                    ip = str(aaaa_answer[0])
                    print(f'- IPv6 address for {name}: {ip}')
                except:
                    print('\033[91m- Error: DNS lookup failed\033[0m')



                # Test HTTP endpoint
                try:
                    http_response = requests.get(
                        f'http://{name}/', timeout=timeout)
                    http_status = http_response.status_code
                    print(f'- HTTP status code for {name}: {http_status}')
                except:
                    print(
                        '\033[91m- Error: HTTP endpoint not reachable\033[0m')
                    http_status = None

                # Test HTTPS endpoint
                try:
                    https_response = requests.get(
                        f'https://{name}/', timeout=timeout)
                    https_status = https_response.status_code
                    print(
                        f'- HTTPS status code for {name}: {https_status}')
                except:
                    print(
                        '\033[91m- Error: HTTPS endpoint not reachable\033[0m')
                    https_status = None

        else:
            print(
                f'Error: Cloudflare API returned status code {dns_response.status_code}')

