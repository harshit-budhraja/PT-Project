# Programming Tools Project

In this project, we'll be making a realtime system monitoring tool, which can spy on a system anonymously and send us the system's data and actions over the internet. This project will be primarily implemented in **C/C++** and **Python3**. We'll use tools like **make**  and **PyBuilder** for build automation.

## Brief Overview of the structure

The tool will consist of two major components - 
* A **server API**, which will grab the actions and data from all the multiple PC's which we are monitoring and display the data appropriately.
* A **trojan horse** which will be injected into the victim's PC for monitoring purposes.

The linux server will host scripts in PHP. The backend model will deploy a MYSQL database which will hold the logs from the victim PC's. The trojan horse will run several python and C scripts on the victim's machine and transfer the sensitive data to our servers.

For demonstration purposes, we'll be using a sub-domain on Harshit's [Private Server](https://arachnis.org), the end-point to which is [https://apps.arachnis.org/pt-project/](https://apps.arachnis.org/pt-project/). However, for testing, we will be simulating this in XAMPP's local server, which has the same configuration as any other linux server.
