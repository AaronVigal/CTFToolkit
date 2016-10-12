# CTFToolkit (Computer Science Club Toolkit)
A Kali-Linux Toolkit made by Aaron Vigal for the Millard West Computer Science Club that includes the following projects:

1. [CSCipher](#cscipher)
2. [Flag Crawler](#flag-crawler)
3. [Steggo Sniffer](#steggo-sniffer)
3. [Brute Force Web](#brute-force-web)

This framework should run under most versions of Linux but is optimized for working on Kali.
The setup is very straight-forward just copy and paste the following code into a terminal:
```{r, engine='bash', count_lines}
wget https://raw.githubusercontent.com/AaronVigal/CTFToolkit/master/setup
chmod +x setup
./setup 
```
The setup file checks/installs the following dependencies:

1. Java
2. aircrack-ng
3. Python 3.5
4. Python 2.7
5. pip3
6. ruby
7. perl
8. at
9. libnotify-bin
10. tput
11. selenium 
12. bs4

For a detailed description on how each module works check the sections below.

## General Layout:
Each individual menu contains multiple sub menus or options for customizable on each individual module. The structure of this toolkit looks like this:
```
CTFToolkit
│   README.MD
│   LICENSE  
│
└───CSCipher
│   │   Load from file
│   │   Load from web page
|   |   Enter in text
│   └───
│   
└───Flag Crawler
│   │   Wget Entire Site
│   │   Robots.txt
|   |   User Agent Spoofer
|   |   All
│   └───
|
└───Steggo Sniffer
│   │   Simple Steggo
│   │   Least Sig Bit
|   |   All
│   └───
│   
└───Brute Force Web
│   │   Custom Post Requests
│   │   Use Rockyou.txt
|   |   Use Custom Wordlist
│   └───
│   
└───

```

##Metasploit
This module uses the Metasploit framework built into Kali-Linux to create and Android APK that will allow a back door into the users phone. The script creates the malicious APK file and embeds it into a normal, unsuspicious APK that when opened, will automatically trigger a Perl script to create a persistent backdoor into the users phone. This can be done in two ways, over your local area network (LAN), or you can open a port for the data to be sent to and listen on the local binding for the data coming in. These options can be specified during the process of the script creating the APK. Here's a list of sample command you could use once you connect to the victims phone:
1. blah
2. blah
3. blah
4. blah
5. blah

##DNS Spoofing
This was intended with the idea in mind to make it as simple as possible to spoof a url quickly and easily. Give it a domain to change to your local IP Address and it will edit the needed files in your system and fire up a cloned version of the page on your network that connects back to you. It's as easy as that!

##Slowloris
This toolkit integrates the Slowloris program created by [Robert Hansen](ha.ckers.org/slowloris/) and is a low bandwidth DoS attack that eats networks for breakfast. You simply specify to go through HTTPS or HTTPS, feed the module an IP and a number of threads and it will get to work.

##Cracking WiFi
A tool created by [Aaron Vigal](https://www.github.com/AaronVigal) to brute force the password for any WiFi Network. This tool works by finding the MAC Address of the networks router and sending it deauthentication packets, and sniffing the network for the devices to reconnect. Once the program has intercepted the hand shake then it will start hashing passwords from a chosen wordlist and comparing it to the handshakes hash. This uses a combination of tools from the [aircrack-ng](https://www.aircrack-ng.org/) suite and would not be possible without it.

## Zengineering Toolkit
This module was created by [Thomas Gerot](https://www.github.com/tjgerot) with the intention to scrape common social media outlets and gather information about a given user. The toolkit relies heavily on webpage scraping for social media accounts and selenium driver implementation to handle the dynamic web application used in the Douglas County Assessor. As the toolkit discovers usernames and domains, it will repeat the process for each one.

##CSCipher
This tool was designed to help crack encrypted CTF passwords to obtain a flag. You give the module an encrypted string of text via a .txt file or straight through the interface and it will run a variety of analysis's and test to determine what kind of cipher it was encrypted with, and return the decoded message.


##*Warning!!!*
Millard West, its Affiliates and all of this projects Contributers in no way promote or encourage un-lawful hacking and this toolkit should be rightfully used for it's purpose for penetration testing on your own network or any network that you have explicit consent from the Administrator. Millard West, its Affiliates and any Contributers cannot and will not be held liable for any damage or unlawful action that may occur while using this toolkit. 

Happy Hacking!
