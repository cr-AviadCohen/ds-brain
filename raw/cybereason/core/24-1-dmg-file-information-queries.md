Afterwards, select a file from the results list to display the element


details screen and view details on the associated mount point.


**Option 2 (valid only if processes were run from the DMG):** **File**

Element THEN


**Mount point** Element -> filter for Media type is _Disk image file_


If processes were run from the DMG, Cybereason will display a


**Files** section in the mount point details screen that lists files

mounted from that DMG mount point.

## Find mount points that mount DMG files


**Goal:** Find different mount points for DMG files in your Mac

machines.


**Explanatory statement:** I want to find different mount points of
DMG files.


Construct this query:


**Mount point** Element -> Media type is _Disk image file_


## Find DMG files that were mounted

**Goal:** Find a list of all DMG files actually mounted on the Mac


machine.


**Explanatory statement:** I want to find a list of all DMG files that


actually have been mounted on a machine.


Construct this query:


**Mount point** Element -> Media type is _Disk image file_


Then, select a mount point from the results list to display details for


the mount point. The file that mounted this mount point is listed as
**Mounted from image file** in the **Properties** section.


Click the file link for more information on the file.



