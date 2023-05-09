# Cloudflare DNS Checker

This script retrieves all A and AAAA records for all domains in a Cloudflare account, and performs DNS and basic HTTP/HTTPS status code checks to verify that the records are set up correctly. It does not check SSL Certificate validity.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Rename the `config.ini.example` file to `config.ini`.
4. Fill in your Cloudflare API token and DNS resolver settings in the `config.ini` file.

## Usage

To run the script, simply run the `cloudflare_dns_checker.py` file:

```
python cloudflare_dns_checker.py
```

The script will retrieve all A records for all domains in your Cloudflare account and perform the following checks for each record:

- DNS lookup for both IPv4 and IPv6 addresses.
- HTTP request to the specified domain over both HTTP and HTTPS protocols.

If any errors occur during these checks, they will be printed to the console.

## Example output

```
--
Zone for anto.online (zone_id: fsa5e492cabc)
--
- IPv4 address for anto.online: 1722.67.1631.80
- IPv6 address for anto.online: 26206:4700:30330::ac43:a150
- HTTP status code for anto.online: 200
- HTTPS status code for anto.online: 200
- IPv4 address for demo.anto.online: 1104.21.9.197
- IPv6 address for demo.anto.online: 2606:47030:3030::ac43:a150
- HTTP status code for demo.anto.online: 200
- HTTPS status code for demo.anto.online: 200

--
Zone for example.com (zone_id: fsa5e492cabc)
--
- IPv4 address for example.com: 1014.211.7134.212
- IPv6 address for example.com: 26106:4100:3037::6815:4ad4
- HTTP status code for example.com: 200
- HTTPS status code for example.com: 200
- IPv4 address for www.example.com: 1172.617.2106.120
- IPv6 address for www.example.com: 26106:4100:30337::6815:4ad4
- HTTP status code for www.example.com: 200
- HTTPS status code for www.example.com: 200
```

## Configuration

The script is configured using the `config.ini` file. The file contains the following settings:

- `api_token`: Your Cloudflare API token. You can generate a new token in the Cloudflare dashboard.
- `nameserver`: The DNS resolver to use for lookups.
- `timeout`: The timeout for DNS and HTTP requests, in seconds.

You can modify these settings to match your Cloudflare account and DNS configuration.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Want to connect?

Feel free to contact me on [Twitter](https://twitter.com/OnlineAnto), [DEV Community](https://dev.to/antoonline/) or [LinkedIn](https://www.linkedin.com/in/anto-online) if you have any questions or suggestions.

Or just visit my [website](https://anto.online) to see what I do.
