# Netdiscover<h1 align="center" id="title">NetDiscover</h1>

<p align="center"><img src="https://static.thenounproject.com/png/1620258-200.png" alt="project-image"></p>

<p id="description">The network discovery tool is a Python script developed using the Scapy library which enables the user to explore and identify devices on a local network. It utilizes various network protocols and techniques to gather information about active hosts. Upon execution the tool starts by scanning the local network using an IP range specified by the user. It generates IP packets for each address within the given range and sends them out waiting for responses. This approach allows the tool to identify active hosts on the network. Once a response is received the tool extracts relevant information from the packet such as the source IP address MAC address and Device vendors. By analyzing this data it determines the type of device (e.g. router computer printer) and its operating system if possible. This information can help users understand the network topology and identify potential vulnerabilities.</p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Download tool</p>

```
git clone https://github.com/iraklichubinidze/Netdiscover.git
```

<p>2. Install requirements</p>

```
pip install -r requirements.txt
```

<p>3. Run Program</p>

```
python3 netdiscover.py
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Scapy
