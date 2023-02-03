# Execute Uploaded File - A Vulnerable Web Application
This repository contains a web application that prompts a user to upload a file, simulating a phishing attack scenario. The uploaded file is then executed automatically, allowing the attacker to run a command of their choice on the victim's machine.

The application makes use of the watchdir.py script within the documents directory, which monitors a specified directory for new files and can execute them accordingly. This makes it a valuable tool for demonstrating the dangers of malicious file uploads, and can be used in a penetration testing course to educate students on the techniques used by attackers.

As an example, students can upload a LibreOffice document with macro capabilities, showing the potential for an attacker to execute arbitrary code on a target's machine.

This application is for educational purposes only and should not be used for malicious purposes.


To install, place extracted folder into any web server. 

Dependencies required
  - Python3 with Watchdog Package 
  - PHP (Some changes to the php.ini, such as max packet and file upload sizes may be needed to be changed)
  
