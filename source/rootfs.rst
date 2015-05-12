Root FS
=======

The final root file system will be packaged as a *.tar.gz* file that, at the
end of the build process, *Bitbake* will let you find it under directory:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'rootfs_rst-host-51' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="rootfs_rst-host-51" class="language-markup">/path/to/yocto/build/tmp/deploy/images/microzed/</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

this means that within the SDK the actual path of the directory is:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'rootfs_rst-host-52' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="rootfs_rst-host-52" class="language-markup">/home/architech/architech_sdk/architech/microzed/yocto/build/tmp/deploy/images/microzed/</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

To deploy the root file system, you are going to need an SD card with two
partitions on it.

The first partition must be formatted as **FAT16**, its size must be sufficient
to contain all the following files (64MB are more than enough):

1. **UBOOT.BIN**, read directly by the processor at boot, containing the *first stage bootloader*, the  *bitstream* (optional), and *u-boot*

2. **uEnv.txt**, the bootscript with customizations

3. **uImage**, the Linux kernel 

4. **devicetree.dtb**, the device tree binary file

To have a better understanding of those components and how to boot the board please refer 
to :ref:`boot_label` Section.

The second partition, our root file system partition, can be formatted as **EXT2**.

We assume that the second partition of the SD card gets mounted (in your SDK virtual machine)
under:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'rootfs_rst-host-53' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="rootfs_rst-host-53" class="language-markup">/media/rootfs</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

.. warning::

 If that's not the case for your configuration, please find out what is the proper mounting point
 for such a partition on your system and replace it in the following instructions.

Untar the file corresponding to your root file system inside such a partition:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'rootfs_rst-host-54' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="rootfs_rst-host-54" class="language-markup">sudo rm -rf /media/rootfs/*
 sudo tar -xzf /home/architech/architech_sdk/architech/microzed/yocto/build/tmp/deploy/images/microzed/&lt;image&gt;-microzed.tar.gz -C /media/rootfs/</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

where *<image>* is the name of the recipe you used to build your root file system.
For example, if you built core-image-minimal-dev with :ref:`Bitbake <bitbake_label>`,
then the name of the tarball will be *core-image-minimal-dev-microzed.tar.gz*

.. important::

 sudo password is **architech**
