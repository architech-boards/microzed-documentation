.. _appendix_label:

Appendix
========

In this page you can find some useful info about how Linux works. If you are coming from Microsoft world, the next paragraphs can help you to have a more soft approach to Linux world.

.. _sudo_info_label:

**sudo** command
----------------

**sudo** is a program for Unix-like computer operating systems that allows users to run programs/commands
with the security privileges of another user, normally the superuser or root. Not all the users can call
sudo, only the **sudoers**, **architech** (the default user of the virtual machine) user is a sudoer.
When you run a command preceeded by sudo Linux will ask you the user password, for **architech** user the
password is **architech**.

.. _device_files_label:

Device files
------------

Under Linux, (almost) all hardware devices are treated as files. A device file is a special file which allows users to access an hardware device by means of the standard file operations (open, read, write, close, etc), hiding hardware details. All device files are in */dev* directory.
In order to access a filesystem in Linux you first need to mount it. Mounting a filesystem simply means making the particular filesystem accessible at a certain point in the Linux directories tree.
In Linux, memory cards are generally named starting with *mmcblk*. For example if you insert 2 memory cards in 2 different slots of the same computer, Linux will create 2 device files:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-171' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-171" class="language-markup">/dev/mmcblk0
 /dev/mmcblk1</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

The number identifies a specific memory card.
A memory card itself can have one or more partitions. Even in this case, Linux will create a device file for every partition present in the sd card.
So, for example if the "mmcblk0" countains 3 partitions, the operating system will add these files under */dev* directory:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-172' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-172" class="language-markup">/dev/mmcblk0    /* device */
 /dev/mmcblk0p0  /* first partition */
 /dev/mmcblk0p1  /* second partition */
 /dev/mmcblk0p2  /* third partition */</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Not all devices are named according to the aforementioned naming scheme. For example, usb pens and hard disks are named with *sd* followed by a letter which is incremented every time a new device gets connected (starting with *a*), as opposed to the naming scheme adopted by SD cards where a number (starting with *0*) was incremented.
A machine with an hard disk and two pen drives would tipically have the following devices:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-173' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-173" class="language-markup">/dev/sda
 /dev/sdb
 /dev/sbc</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Usually */dev/sda* file is the primary hard disk (this might depend on your hardware). 

As memory cards, the pen can have one or more partitions, so if for example we have a pen drive which has been recognized as *sdc*, and the pen drive has 2 partitions on it, we will have the following device files:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-174' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-174" class="language-markup">/dev/sdc   /* device */
 /dev/sdc1  /* first partition */
 /dev/sdc2  /* second partition */</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Commands like mount, umount, dd, etc., use partition device files.
FIXME mkfs

.. warning::

 | Be very careful when addressing device files, addressing the wrong one may cost you the loss of important data

Disks discovery
---------------

When dealing with plug and play devices, it is quite comfortable to take advantage of **dmesg** command. The kernel messages (printk) are arranged into a ring buffer, which the user can be easly access by means of **dmesg** command. Every time the kernel recognizes new hardware, it prints information about the new device within the ring buffer, along with the device filename.
To better filter out the information regarding the plug and play device we are interested in, it is better if we first clean up the ring buffer:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-175' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-175" class="language-markup">$ sudo dmesg -c</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

now that the ring buffer has been emptied, we can plug the device and, after that, display the latest messages from the kernel:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-176' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-176" class="language-markup">$ dmesg</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

On the Ubuntu machine (with kernel version *3.2.0-65-generic*) this documentation has been written with, we observed the following messages after inserting a pen drive:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-177' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-177" class="language-markup">[10553.164670] usb 2-1.2: new high-speed USB device number 7 using ehci_hcd
 [10553.261991] scsi7 : usb-storage 2-1.2:1.0
 [10554.262123] scsi 7:0:0:0: Direct-Access     USB      DISK 2.0         1219 PQ: 0 ANSI: 0 CCS
 [10554.264376] sd 7:0:0:0: Attached scsi generic sg2 type 0
 [10554.268203] sd 7:0:0:0: [sdb] 1957888 512-byte logical blocks: (1.00 GB/956 MiB)
 [10554.269344] sd 7:0:0:0: [sdb] Write Protect is off
 [10554.269358] sd 7:0:0:0: [sdb] Mode Sense: 43 00 00 00
 [10554.270177] sd 7:0:0:0: [sdb] No Caching mode page found
 [10554.270187] sd 7:0:0:0: [sdb] Assuming drive cache: write through
 [10554.274644] sd 7:0:0:0: [sdb] No Caching mode page found
 [10554.274655] sd 7:0:0:0: [sdb] Assuming drive cache: write through
 [10554.275287]  sdb: sdb1
 [10554.278257] sd 7:0:0:0: [sdb] No Caching mode page found
 [10554.278268] sd 7:0:0:0: [sdb] Assuming drive cache: write through
 [10554.278277] sd 7:0:0:0: [sdb] Attached SCSI removable disk</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

As you can see, the operating system have recognized the usb device as *sdb* (this translates to */dev/sdb*) and its only partition as *sdb1* (this translates to */dev/sdb1*)

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-178' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-178" class="language-markup">[10554.275287]  sdb: sdb1</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

The most useful command to gather information about mass storage devices and related partitions is **fdisk**.
On the very same machine of the previous example, the execution of this command:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-179' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-179" class="language-markup">$ sudo fdisk -l</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

produces the following output:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1710' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1710" class="language-markup">Disk /dev/sda: 500.1 GB, 500107862016 bytes
 255 heads, 63 sectors/track, 60801 cylinders, total 976773168 sectors
 Units = sectors of 1 * 512 = 512 bytes
 Sector size (logical/physical): 512 bytes / 512 bytes
 I/O size (minimum/optimal): 512 bytes / 512 bytes
 Disk identifier: 0x410fac6e
 
 Device Boot         Start         End      Blocks   Id  System
 /dev/sda1   *        2048      616447      307200    7  HPFS/NTFS/exFAT
 /dev/sda2          616448   933025791   466204672    7  HPFS/NTFS/exFAT
 /dev/sda3       933025792   966281215    16627712   83  Linux
 /dev/sda4       966281216   976756735     5237760   82  Linux swap / Solaris
 
 Disk /dev/sdb: 1002 MB, 1002438656 bytes
 223 heads, 37 sectors/track, 237 cylinders, total 1957888 sectors
 Units = sectors of 1 * 512 = 512 bytes
 Sector size (logical/physical): 512 bytes / 512 bytes
 I/O size (minimum/optimal): 512 bytes / 512 bytes
 Disk identifier: 0x00029795
 
 Device Boot         Start         End      Blocks   Id  System
 /dev/sdb1            2048     1957887      977920    b  W95 FAT32</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

The machine has two mass storage devices, a 500GB hard disk and a 1GB USB pen disk. As you can see from the output, *sudo fdisk -l* command lists information regarding the disks seen by the kernel along with the partitions found on them, disk after disk.
The first disk (sda) presented by *fdisk* is the primary hard disk (where Linux is running), it has 4 partitions, two of which (sda1 and sda2) are used by a Microsoft operating system while the other two (sda3 and sda4) are used by a Linux operating system.
The second disk (sdb) depicted by *fdisk* is an USB disk with a single FAT32 partition (sdb1)

As already stated, in order to access a filesystem in Linux you first need to mount it.
Mounting a partition means binding a directory to it, so that files and directories contained inside the partition will be available in Linux filesystem starting from the directory used as mount point. 

**mount** command
-----------------

Suppose you want to read a file named *readme.txt* which is contained inside the USB disk of the previous example, in the main directory of the disk.
Before accessing the device you must understand if it is already mounted. **mount** is the command that lets you control the mounting of filesystems in Linux. It is a complex command that permits to mount different devices and different filesystems. In this brief guide we are using it only for a very common use case.
Launching **mount** without any parameter lists all mounted devices with their respective mounting points. 
Every line of the list, describes the name of the mounted device, where it has been mounted (path of the directory in the Linux filesystem, that is the mount point), the type of filesystem (ext3, ext4, etc.), and the options used to mount it (read and write permissions,etc.).
Launching the command on the same machine of the previous section example, we don't find the device */dev/sdb1*.

 | $ mount
 | /dev/sda2 on /media/windows7 type fuseblk (rw,noexec,nosuid,nodev,allow_other,blksize=4096)
 | /dev/sda3 on / type ext4 (rw,errors=remount-ro)
 | proc on /proc type proc (rw,noexec,nosuid,nodev)
 | sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
 | none on /sys/fs/fuse/connections type fusectl (rw)
 | none on /sys/kernel/debug type debugfs (rw)
 | none on /sys/kernel/security type securityfs (rw)
 | udev on /dev type devtmpfs (rw,mode=0755)
 | devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
 | tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
 | none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
 | none on /run/shm type tmpfs (rw,nosuid,nodev)
 | binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,noexec,nosuid,nodev)
 | rpc_pipefs on /run/rpc_pipefs type rpc_pipefs (rw)
 | vmware-vmblock on /run/vmblock-fuse type fuse.vmware-vmblock (rw,nosuid,nodev,default_permissions,allow_other)
 | gvfs-fuse-daemon on /home/roberto/.gvfs type fuse.gvfs-fuse-daemon (rw,nosuid,nodev,user=roberto)

This tells us that the USB disk has not been mounted yet.

The mount operation requires three essential parameters:
- the device to mount
- the directory to associate
- the type of filesystem used by the device

Thanks to the previously introduced **fdisk** command, we know the partition to mount (*/dev/sdb1*) and the type of filesystem used (FAT32). The directory to bind can be anything you like, by convention the user should mount his own devices under */media* or */mnt*. We haven't created it yet, so:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1711' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1711" class="language-markup">$ mkdir -p /media/usbdisk</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

At this point, we have the information we need to execute the mounting. To semplify our life, we leave the duty of understanding what filesystem is effectively used by the device to the **mount** command by using option *-t auto* (if we would have wanted to tell mount exactly which filesystem to use we would have written *-t vfat*), like

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1712' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1712" class="language-markup">$ mount -t auto /dev/sdb1 /media/usbdisk</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

The partition is now binded to */media/usbdisk* directory and its data are accessible from this directory.

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1713' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1713" class="language-markup">$ cd /media/usbdisk
 $ ls
 readme.txt</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

now we can open the file, read it and, possibly, modify it.

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1714' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1714" class="language-markup">$ gedit readme.txt</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

When you want to disconnect the device, you need the inverse operation of **mount** which is **umount**. This command saves all data still contained in RAM (and waiting to be written on the device) and unbind the directory from the device file.

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1715' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1715" class="language-markup">$ umount /media/usbdisk</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Once the directory */media/usbdisk* is unmounted it's empty, feel free to delete it if doesn't interest you anymore.
It is now possible to remove the device from the machine.

What if you wanted to know the amount of free disk space available on a mounted device?

**df** command shows the disk space usage of all currently mounted partitions. For every partition, **df** prints its device file, size, free and used space, and the partition mount point.
On our example machine we have:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'appendix_rst-host-1716' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="appendix_rst-host-1716" class="language-markup">$ df -h
 Filesystem      Size  Used Avail Use% Mounted on
 /dev/sda3        16G   11G  4.0G  74% /
 /dev/sda2       445G  408G   37G  92% /media/windows7</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

**-h** option tells **df** to print sizes in human readable format.