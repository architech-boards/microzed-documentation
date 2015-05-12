Linux Kernel
============

Like we saw for the :ref:`bootloader <bsp_bootloader_label>`, the first thing you need is: sources.
Get them from *Bitbake* build directory (if you built the kernel with it) or get them from the Internet.

*Bitbake* will place the sources under directory:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-111' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-111" class="language-markup">/path/to/build/tmp/work/microzed-poky-linux-gnueabi/linux-xlnx/3.17-xilinx+gitAUTOINC+7b042ef9ea-r0</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>


If you are working with the virtual machine, you will find them under directory:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-112' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-112" class="language-markup">/home/architech/architech_sdk/architech/microzed/yocto/build/tmp/work/microzed-poky-linux-gnueabi/linux-xlnx/3.17-xilinx+gitAUTOINC+7b042ef9ea-r0</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>


We suggest you to **don't work under Bitbake build directory**, you will pay a speed penalty and you could
have troubles syncronizing the all thing. Just copy them some place else and do what you have to do.

If you didn't build them already with *Bitbake* or you just want to do make every step by hand, you can
always get them from the Internet by cloning the proper repository and checking out the proper hash commit:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-113' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-113" class="language-markup">cd ~/Documents
 git clone -b xlnx_3.17 git://github.com/Xilinx/linux-xlnx.git
 cd linux-xlnx
 git checkout 7b042ef9ea5cc359a22110c75342f8e28c9cdff1</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

and by properly patching the sources:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-114' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-114" class="language-markup">patch -p1 &lt; ~/architech_sdk/architech/microzed/yocto/meta-microzed/recipes-kernel/linux/linux-xlnx/3.17/0001-Updated-the-TI-Wilink8-driver-to-R8.5.patch
 patch -p1 &lt; ~/architech_sdk/architech/microzed/yocto/meta-microzed/recipes-kernel/linux/linux-xlnx/3.17/0002-Patching-kernel-to-adapt-TI-Wilink8-driver.patch
 patch -p1 &lt; ~/architech_sdk/architech/microzed/yocto/meta-microzed/recipes-kernel/linux/linux-xlnx/3.17/0003-Fixed-TI-Wilink8-driver-with-kernel-structure.patch
 patch -p1 &lt; ~/architech_sdk/architech/microzed/yocto/meta-xilinx/recipes-kernel/linux/linux-xlnx/3.17/tty-xuartps-Fix-RX-hang-and-TX-corruption-in-set_termios.patch
 cp ~/architech_sdk/architech/microzed/yocto/meta-microzed/recipes-kernel/linux/linux-xlnx/3.17/defconfig .config</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>


If you don't use our SDK then use the following commands to patch the sources:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-115' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-115" class="language-markup">cd ~/Documents
 git clone git://git.yoctoproject.org/meta-xilinx.git
 cd meta-xilinx
 git checkout 7f759048bb0aeef3c0b3938be81d2bcade7acb7e</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Download the config file and put it in the linux directory, renamed *.config*:

	`Download file config <_static/config>`_

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-116' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-116" class="language-markup">cp ~/Downloads/config ~/Documents/linux-xlnx/.config</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Source the script to load the proper evironment for the cross-toolchain (see :ref:`manual_compilation_label`
Section) and you are ready to customize and compile the kernel:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-117' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-117" class="language-markup">source ~/architech_sdk/architech/microzed/toolchain/environment-nofs
 LOADADDR=0x0008000 make uImage -j &lt;2 * number of processor's cores&gt;</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Now you need compile the devicetree file:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'kernel_rst-host-118' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="kernel_rst-host-118" class="language-markup">cp ~/architech_sdk/architech/microzed/yocto/meta-microzed/conf/machine/boards/microzed/microzed* arch/arm/boot/dts/
 make microzed-mmcblk0p2.dtb</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

By the end of the build process you will get **uImage** and **devicetree** under *arch/arm/boot*.

.. host::

 ~/Documents/linux-xlnx/arch/arm/boot/uImage
 ~/Documents/linux-xlnx/arch/arm/boot/dts/microzed-mmcblk0p2.dtb
 

Enjoy!