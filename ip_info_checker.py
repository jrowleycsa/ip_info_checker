import requests
import json
import IP2Location
import os

# Setting API key (use absolute path)
apiFile = "/path/to/api.txt"

# Connecting to IP2Location DB
dbpath = "/path/to/IP2LOCATION-LITE-DB5.IPV6.BIN"  # Path to the database file (use absolute path)
dbconn = IP2Location.IP2Location(os.path.join("data", dbpath))

# Reading API key
with open(apiFile, "r") as apiF:
    api = apiF.read()

# Function to process IP
def process_ip(ip):
    # API url to check the IP
    url = 'https://api.abuseipdb.com/api/v2/check'

    # Query
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '365',
        'verbose': ''
    }

    headers = {
        'Accept': 'application/json',
        'Key': api
    }

    try:
        response = requests.request(method='GET', url=url, headers=headers, params=querystring, timeout=60)
        response.raise_for_status()

        # Check if 'response' is defined
        if response is not None:
            try:
                # Parse the JSON response
                results = json.loads(response.text)
                # Continue processing the results

                # Getting DB results for IP address
                ip2loc = dbconn.get_all(ip)

                # Results in json format
                results = json.loads(response.text)

                # Checking if key exists as countryName and City key is missing
                if "ipAddress" in results['data']:
                    ipaddr = str(results['data']['ipAddress'])
                else:
                    ipaddr = "NaN"

                if "isp" in results['data']:
                    isp = str(results['data']['isp'])
                else:
                    isp = "NaN"

                if ip2loc.city:
                    cityName = str(ip2loc.city)
                else:
                    cityName = "NaN"

                if ip2loc.region:
                    regionName = str(ip2loc.region)
                else:
                    regionName = "NaN"

                if "countryName" in results['data']:
                    countryName = str(results['data']['countryName'])
                else:
                    countryName = "NaN"

                if "totalReports" in results['data']:
                    totalRep = str(results['data']['totalReports'])
                else:
                    totalRep = "NaN"

                if "abuseConfidenceScore" in results['data']:
                    abuseConf = str(results['data']['abuseConfidenceScore'])
                else:
                    abuseConf = "NaN"

                # Print to terminal
                print(f"'{ipaddr}' is owned by '{isp}' and hosted in {cityName}, {regionName}, {countryName}, with {totalRep} reports of abuse, and a confidence of abuse of {abuseConf}%")

            except json.JSONDecodeError as json_error:
                # Handle JSON decoding errors
                print(f"JSON Decode Error: {json_error}")
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., timeouts, connection errors)
        print(f"Error: {e}")
        response = None  # Set response to None in case of an exception

        print(f"Error fetching data for IP: {ip}")

# Main function
def main():
    while True:
        ip = input("Enter IP address (or 'exit' to quit): ")
        if ip.lower() == 'exit':
            break
        process_ip(ip)

if __name__ == "__main__":
    main()
