Linux Kernel
============

Like we saw for the :ref:`bootloader <bsp_bootloader_label>`, the first thing you need is: sources.
Get them from *Bitbake* build directory (if you built the kernel with it) or get them from the Internet.

*Bitbake* will place the sources under directory:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-101' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-101" class="language-markup">/path/to/build/tmp/work/microzed-poky-linux-gnueabi/linux-xlnx/3.8-xilinx+gitf4ff79d44a966ebea6229213816d17eb472b303e-r1/git</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>


If you are working with the virtual machine, you will find them under directory:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-102' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-102" class="language-markup">/home/architech/architech_sdk/architech/microzed/yocto/build/tmp/work/microzed-poky-linux-gnueabi/linux-xlnx/3.8-xilinx+gitf4ff79d44a966ebea6229213816d17eb472b303e-r1/git</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>


We suggest you to **don't work under Bitbake build directory**, you will pay a speed penalty and you could
have troubles syncronizing the all thing. Just copy them some place else and do what you have to do.

If you didn't build them already with *Bitbake* or you just want to do make every step by hand, you can
always get them from the Internet by cloning the proper repository and checking out the proper hash commit:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-103' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-103" class="language-markup">cd ~/Documents
 git clone -b xlnx_3.8 git://github.com/Xilinx/linux-xlnx
 cd linux-xlnx
 git checkout f4ff79d44a966ebea6229213816d17eb472b303e
 git checkout xlnx_3.8</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

and by properly patching the sources:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-104' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-104" class="language-markup">cd ..
 patch -p1 -d linux-xlnx/ &lt; ~/architech_sdk/architech/microzed/yocto/meta-xilinx/recipes-kernel/linux/linux-xlnx/libtraceevent-Remove-hard-coded-include-to-usr-local.patch</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>


If you don't use our SDK then use the following commands to patch the sources:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-105' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-105" class="language-markup">cd ~/Documents
 git clone git://git.yoctoproject.org/meta-xilinx.git
 cd meta-xilinx/
 git checkout cb7329a596a5ab2d1392c1962f9975eeef8e4576
 cd ..
 patch -p1 -d linux-xlnx/ &lt; meta-xilinx/recipes-kernel/linux/linux-xlnx/libtraceevent-Remove-hard-coded-include-to-usr-local.patch</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Download the config file and put it in the linux directory, renamed *.config*:

	`Download file config <_static/config>`_

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-106' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-106" class="language-markup">cp ~/Downloads/config ~/Documents/linux-xlnx/.config</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Source the script to load the proper evironment for the cross-toolchain (see :ref:`manual_compilation_label`
Section) and you are ready to customize the kernel:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-107' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-107" class="language-markup">source /home/architech/architech_sdk/architech/microzed/toolchain/environment-nofs
 cd ~/Documents/linux-xlnx
 make menuconfig</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

and to compile it:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-108' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-108" class="language-markup">make microzed_defconfig
 make -j &lt;2 * number of processor's cores&gt;</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

By the end of the build process you will get **zImage** under *arch/arm/boot*.

.. host::

 ~/Documents/linux-xlnx/arch/arm/boot/zImage
 
Now you need compile the devicetree file:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-109' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-109" class="language-markup">cp /home/architech/architech_sdk/architech/microzed/yocto/meta-microzed/recipes-kernel/linux/linux-xlnx-3.8/*.dts* arch/arm/boot/dts/
 make microzed-mmcblk0p2.dtb</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Enjoy!