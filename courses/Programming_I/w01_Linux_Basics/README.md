## Linux & Termius

* Termius is the tool we use to connect to the Linux server.

* Four elements for creating a new host in Termius: IP address, Port, Username, Password
  
* Termius offers SFTP for file management (upload/download)

<br>

### 1. Overview of Termius
Termius is a cross-platform SSH client widely used for securely connecting to and managing remote Linux servers.
It supports multiple connection protocols and provides a user-friendly interface for daily server operation, file transfer, and system maintenance.

### 2. Four Essential Elements for Creating a New Host in Termius
To establish a connection to a Linux server in Termius, users must configure a new host profile with four mandatory parameters:

#### 2.1 IP Address
- The **IP address** is the unique network identifier of the target Linux server.
- It can be a public IP or a private internal IP address.
- This address allows Termius to locate the server on the network.

#### 2.2 Port
- The **port** specifies the communication endpoint for the SSH service.
- The default SSH port is **22**.
- In secure environments, administrators may change the SSH port to a custom value to reduce unauthorized access risks.

#### 2.3 Username
- The **username** is a valid system account on the Linux server.
- Common examples include `root`, `ubuntu`, `centos`, or custom user accounts.
- Permissions for server operations depend on the privileges assigned to this user.

#### 2.4 Password
- The **password** is the authentication credential associated with the username.
- It verifies the identity of the user attempting to log in.
- For enhanced security, public-key authentication can also be used as an alternative to password authentication.

### 3. SFTP Functionality in Termius
In addition to SSH terminal access, Termius integrates **SFTP (SSH File Transfer Protocol)** for secure file management between the local machine and the remote Linux server.

#### 3.1 Core Functions
- **File Upload**: Transfer files and directories from the local system to the remote server.
- **File Download**: Retrieve files and directories from the remote server to the local system.
- **File Management**: Support real-time file browsing, editing, renaming, moving, and deletion through a graphical interface.

#### 3.2 Security Advantage
All SFTP operations in Termius are encrypted via the SSH protocol, ensuring data confidentiality and integrity during transmission.

### 4. Summary
- Termius is a reliable tool for connecting to and administering Linux servers via SSH.
- Creating a usable host configuration requires four key components: **IP address, port, username, and password**.
- The built-in SFTP module enables secure and convenient file transfer and management between local and remote environments.

<br>





