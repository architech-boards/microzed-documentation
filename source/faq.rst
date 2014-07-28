***
FAQ
***

Virtual Machine
===============

What is the password for the default user of the virtual machine?
-----------------------------------------------------------------

The password for the default user, that is **architech**, is:

.. host::

 architech

What is **sudo**?
-----------------

**sudo** is a program for Unix-like computer operating systems that allows users to run programs/commands
with the security privileges of another user, normally the superuser or root. Not all the users can call
sudo, only the **sudoers**, **architech** (the default user of the virtual machine) user is a sudoer.
When you run a command preceeded by sudo Linux will ask you the user password, for **architech** user the
password is **architech**.

What is the password for user root?
-----------------------------------

By default, Ubuntu 12.04 32bit comes with no password defined for **roor** user, to set it run the following
command:

.. host::

 sudo passwd root

Linux will ask you (twice, the second time is just for confirmation) to write the password for user root.

ZedBoard
========