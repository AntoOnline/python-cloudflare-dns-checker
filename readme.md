# Cloudflare DNS Checker

This script retrieves all A records for all domains in a Cloudflare account, and performs DNS and nasic HTTP/HTTPS checks to verify that the records are set up correctly. It does not check SSL Certificate validity.

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

## Configuration

The script is configured using the `config.ini` file. The file contains the following settings:

- `api_token`: Your Cloudflare API token. You can generate a new token in the Cloudflare dashboard.
- `nameserver`: The DNS resolver to use for lookups.
- `timeout`: The timeout for DNS and HTTP requests, in seconds.

You can modify these settings to match your Cloudflare account and DNS configuration.
