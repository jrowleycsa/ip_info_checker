# IP Info Checker

The IP Info Checker is a Python script that provides detailed information about an IP address. It utilizes the AbuseIPDB API to fetch abuse reports and the IP2Location database for geolocation information.

## Prerequisites
- Python 3.x installed
- requests (pip install requests)
- IP2Location (pip install IP2Location)

## Setup

1. Clone the repository: `git clone https://github.com/jrowleycsa/ip-info-checker.git`
2. Obtain an API key from [abuseIPDB](https://www.abuseipdb.com)
3. Download the IP2Location database file (IP2LOCATION-LITE-DB5.IPV6.BIN) from [IP2Location Lite](https://lite.ip2location.com/ip2location-lite)
4. Add your AbuseIPDB API key to a file named api.txt and add its path within the script (/path/to/api.txt).

![image](https://github.com/jrowleycsa/ip_info_checker/assets/152403367/c6a0108d-ba38-4353-839a-47aaf05dee65)

5. Ensure you have the IP2Location database file (IP2LOCATION-LITE-DB5.IPV6.BIN) and add its path within the script (/path/to/IP2LOCATION-LITE-DB5.IPV6.BIN).
   
![image](https://github.com/jrowleycsa/ip_info_checker/assets/152403367/a9391c94-cc17-4d24-910c-e11a38f75156)


### Python venv

A Python virtual environment is an isolated workspace for Python projects, ensuring dependencies are managed per project

1. create an environment `python3 -m venv my_project`
2. Start the environment `source my_project/bin/activate`
3. install dependencies `pip install requests IP2Location`

## Usage

1. Run the script: `python3 ip_info_checker.py`
2. Enter the IP address you want to check when prompted. Type exit to quit the script.
3. The script will fetch abuse reports and geolocation information for the entered IP address and display it in the terminal.
   


# Output
![image](https://github.com/jrowleycsa/abuseipdbInt/assets/152403367/ac9148db-aafe-4898-b3d9-677ba0b62764)

The script displays the following information for the provided IP address:

- IP Address
- ISP (Internet Service Provider)
- City Name
- Region
- Country Name
- Total Reports of Abuse
- Abuse Confidence Score

## Troubleshooting

### ValueError: Invalid header value
In this instance, there is likely a newline character within the api.txt file, to fix run `truncate -s -1 api.txt`

