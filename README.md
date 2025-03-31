
## 💡 How It Works
Directory Listing Check:
Sends an HTTP GET request to check if the response contains "Index of /"—an indicator that directory listing is enabled.

## SQL Injection Test:
Appends a SQL payload (e.g., ' OR '1'='1) to the target URL and scans for error messages that might indicate a vulnerability. If a potential issue is detected, the tool provides recommendations such as using parameterized queries or prepared statements.

## XSS Vulnerability Test:
Injects a script payload (e.g., <script>alert('xss')</script>) to see if it is reflected unescaped in the response, which would suggest an XSS vulnerability.

## Port Scanning:
Uses socket connections to check common ports (e.g., FTP, SSH, SMTP, HTTP, HTTPS) and lists any that are open, giving you insight into potentially exposed services.

## Remediation Recommendations:
For each detected vulnerability, the tool prints out best practices and actionable steps to mitigate the risk.

## 🤝 Contributing
We welcome contributions to make this project even better! To contribute:
``
Fork the repository.
Create your feature branch.
Commit your changes.
Push to the branch.
Open a Pull Request.
``


Vulnerability-Scanner/
├── main.py                  
├── directory_listing.py     
├── sql_injection.py        
├── xss_scanner.py           
├── port_scanner.py         
├── remediation.py           
├── utils.py                 
├── requirements.txt         
├── README.md                                
└── sample_targets.txt      


📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Built with passion for cybersecurity and a desire to educate.
Special thanks to all contributors who helped shape this tool.
Made with ❤️ by poweristsutsun
