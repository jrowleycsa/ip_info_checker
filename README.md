IP Info Checker

The IP Info Checker is a Python script that provides detailed information about an IP address. It utilizes the AbuseIPDB API to fetch abuse reports and the IP2Location database for geolocation information.
Prerequisites

Before running the script, ensure you have the following:

    Python 3.x installed
    requests library (pip install requests)
    IP2Location library (pip install IP2Location)

Setup

    Clone the repository:

    bash

    git clone https://github.com/your_username/ip-info-checker.git

    Add your AbuseIPDB API key to the api.txt file located in the ipdb directory.

    Ensure you have the IP2Location database file (IP2LOCATION-LITE-DB5.IPV6.BIN) in the specified path (/home/j/Desktop/ipdb/).

Usage

    Run the script:

    bash

    python ip_info_checker.py

    Enter the IP address you want to check when prompted. Type exit to quit the script.

    The script will fetch abuse reports and geolocation information for the entered IP address and display it in the terminal.

Output

The script displays the following information for the provided IP address:

    IP Address
    ISP (Internet Service Provider)
    City Name
    Region
    Country Name
    Total Reports of Abuse
    Abuse Confidence Score

Note

    If you want to check multiple IP addresses stored in a CSV file, you can specify the file path as a command-line argument.
