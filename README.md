# FTP Anonymous Login Checker

## Description

This Python script checks for anonymous FTP login on a list of IP addresses. For each IP, it attempts to connect to the FTP server, logs in as 'anonymous', and then checks for read and write access. The script outputs the results for each IP, indicating whether anonymous login is allowed, and whether read/write access is available. It also handles common FTP errors, such as connection timeouts and refused connections.

## Features

* Checks for anonymous FTP login on a list of IP addresses.
* Detects read access by attempting to list files.
* Detects write access by attempting to create a directory.
* Handles common FTP errors (e.g., connection timeout, connection refused).
* Provides verbose output for each IP address.
* Returns a list of results, including IP address, login status, access permissions, and any errors.

## Requirements

* Python 3.x
* ftplib (standard Python library)
* socket (standard Python library)

## Usage

1.  Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  Create a file named `ip_list.txt` in the same directory as the script.  Add the list of IP addresses you want to check to this file, one IP address per line.  Alternatively, you can modify the `ip_addresses` list directly in the script.
3.  Run the script:
    ```bash
    python ftp_checker.py
    ```
4.  The script will output the results to the console, showing the status of anonymous login and read/write access for each IP address.

##  `ip_list.txt` Example

```text

192.168.1.100
192.168.1.101
192.168.1.102
Output Example+-----------------------------------------------------------------------------+
|                               FTP Check Results                               |
+-----------------------------------------------------------------------------+
| IP Address: 127.0.0.1                                           |
| Anonymous Login: True                                           |
| Read Access: True                                                |
| Write Access: False                                               |
+-----------------------------------------------------------------------------+
| IP Address: 192.0.2.0                                           |
| Anonymous Login: False                                          |
| Read Access: False                                               |
| Write Access: False                                               |
| Error: Connection refused                                           |
+-----------------------------------------------------------------------------+

LicenseMIT LicenseCopyright (c) 2024 [Your Name]Permission is hereby granted, free of charge, to any person obtaining a copyof this software and associated documentation files (the "Software"), to dealin the Software without restriction, including without limitation the rightsto use, copy, modify, merge, publish, distribute, sublicense, and/or sellcopies of the Software, and to permit persons to whom the Software isfurnished to do so, subject to the following conditions:The above copyright notice and this permission notice shall be included in allcopies or substantial portions of the Software.THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS ORIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHERLIABILITY, WHETHER IN AN ACTION OF CONTRACT
