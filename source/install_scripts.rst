Installation
============

Architech's Yocto based SDK is built on top of **Ubuntu 12.04 32bit**, hence all the scripts
provided are proven to work on such a system.


If you wish to use another distribution/version you might need to change some script
option and/or modify the scripts yourself, remember that you won't get any support in
doing so.

Install a clone of the virtual machine inside your native machine
-----------------------------------------------------------------

To install the same tools you get inside the virtual machine on your native machine
you need to download and run a system wide installation script:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'install_scripts_rst-host-101' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="install_scripts_rst-host-101" class="language-markup">git clone -b dizzy https://github.com/architech-boards/machine_installer.git
 cd machine_installer
 ./machine_install -g -p</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

where *-g* option asks the script to install and configure a few graphic customization,
while *-p* option asks the script to install the required packages on the machine.
If you want to install the toolchain on a machine not equal to Ubuntu 12.04 32bit then
you may want to read the script, install the required packages by hand, and run it without
options. You might need to recompile the Qt application used to render the splashscreen.

At the end of the installation process, you will get the same tools installed within 
the virtual machine, that is, all the tools necessary to work with Architech's boards.

Install just one board
----------------------

If you don't want to install the tools for all the boards, you can install just the subset
of tools related to Microzed:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'install_scripts_rst-host-102' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="install_scripts_rst-host-102" class="language-markup">git clone -b dizzy https://github.com/architech-boards/microzed-splashscreen.git
 cd microzed-splashscreen
 ./run_install</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

This script needs the same tools/packages required by *machine_install*