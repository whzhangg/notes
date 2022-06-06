# Manual for Connecting to Workstation Remotely
### Workstation Specification
Current Specification:
- OS: Ubuntu 18.04 LTS  
- CPU: Intel Xeon Silver 4214 2.20GHz (TB 3.20GHz) 12cores/24threads × 2 
- Memory: 192GB DDR4 2933 (16GB × 12)  
- Storage: 1TB SSD (SATA) + 2TB HDD (SATA)  
- GPU: NVIDIA RTX 3090 24GB

### Login
##### Requirement
You first need an account on the workstation. The IP address of the workstation is: `144.213.164.101`, this address can only be found inside NIMS network. (Port number is 22, if needed)

##### Using SSH
If ssh commend are available, it is recommended to use ssh to login remotely. Use the following commend to login:
```bash
> ssh your_username@144.213.164.101 -p 22
```

##### Using PuTTY
PuTTY provide a simple grahpic interface to establish remote connection, which can be downloaded from https://www.putty.org/. The window of PuTTY is like this
![[workstation_putty.png]]
We need to configure a new connection, following the steps:
1. Choose "Default Setting" first and start from there
2. Fill in Host Name IP address: `144.213.164.101`
3. In "Saved Session", provide a name for this configuration (any name is OK)
4. Click "Save"

To connect, simply double clicked the session name in "Saved Session". If any window appear, click "Yes". The window will appear to ask you for your account name and password. After entering the login information, a commend line interface will appear.

### File Transfer
##### Using WinSCP (Windows)
The graphical way to transfer file is to use "WinSCP", it can be downloaded from https://winscp.net/eng/download.php. 

After installing winSCP and open, it will promote you to enter Hostname and Username, then click "save" will save these information for future logins. 
![[workstation_winSCP.png]]
Click "Login" and click yes to any window appearing. After than, a window would appear which contain two panels, on the right are files in the remote machine and on the left are files in your local computer. You can drag files from one to another. 

##### Using CyberDuck
It seems cyberduck is a more modern alternative to WinSCP (https://cyberduck.io). 
> Cyberduck is a libre server and cloud storage browser for Mac and Windows with support for FTP, SFTP, WebDAV, Amazon S3, OpenStack Swift, Backblaze B2, Microsoft Azure & OneDrive, Google Drive and Dropbox.

The graphical interface is better than winSCP. The information you need for login is the same as for WinSCP

##### Using Commendline Utilities
You can use FTP (sftp commend) or scp commends to transfer files, but it is not recommended.