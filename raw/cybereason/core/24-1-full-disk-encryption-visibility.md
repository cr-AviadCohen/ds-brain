- Tutorial
Endpoint
Controls
Full Disk Encryption Visibility
With full disk encryption, all of the data on a disk drive is encoded
so that unauthorized parties cannot decipher the data. Full disk
encryption reduces the risk of data compromise in cases where a
computer is stolen or attackers otherwise gain physical access to
the computer.
BitLocker is a full disk encryption method that is included as a
feature in Microsoft versions (starting with Microsoft Vista) and that
uses AES encryption or XTS encryption with a 128-bit or 256-bit
key.
Cybereason Full disk encryption visibility enables you to view a list
of endpoints for which BitLocker is disabled. This allows you to
identify endpoints that are potentially vulnerable to data
compromise or related attacks, and to act accordingly.
In this topic:
Find endpoints that have BitLocker disabled
Related resources
Find endpoints that have BitLocker
disabled
To detect which endpoints in your system are not using BitLocker:
1. In the Investigation screen, under My saved queries, click
Hunting Query: Disk Encryption - Machines with BitLocker
disabled.
2. Click Get Results. The Investigation screen displays a list of
endpoints that have BitLocker disabled.
