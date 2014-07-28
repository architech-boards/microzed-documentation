.. _qt_creator_label:

Qt Creator
==========

.. image:: _static/qt-0.png
	   :align: left

| **Qt** is a cross-platform application framework that is used to build applications. One of the best features of Qt is its capability of generating Graphical User Interfaces (GUIs).
| **Qt Creator** is a cross-platform C++ IDE which includes a visual debugger, an integrated GUI layout and form designer. It makes possible to compile and debug applications on both **x86** (host) and **ARM** (target) machines.
| This SDK relies on **version 4.8.5** of Qt and **version 2.8.1** of Qt Creator.

|
|
| Before getting our hands dirty, make sure all these steps have been followed:

1. Use :ref:`Hob <howToUseHOB>` or :ref:`Bitbake <bitbake_label>` to build an image which includes: *openssh*, support for C++, *tcf-agent* and *gdbserver*.

.. note::

 You could build *qt4e-demo-image* if you want to see the demo of Qt. Just remember to complete its file system with *tcf-agent*, *gdbserver* and *openssh*.

2. Deploy the :ref:`root file system <rootfs_label>` just generated on the final media used to boot the board

3. Replicate the same root file system into directory

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-host-151' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-host-151" class="language-markup">/home/architech/architech_sdk/architech/zedboard/sysroot</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

4. Copy the Qt Libraries to the board media used to boot

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-host-152' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-host-152" class="language-markup">sudo mkdir -p /path/to/board/sysroot/usr/local/Trolltech/
 sudo cp -r /usr/local/Trolltech/Zedboard/* /path/to/board/sysroot/usr/local/Trolltech/</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

5. Copy the Qt Libraries to your sdk sysroot directory

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-host-153' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-host-153" class="language-markup">sudo mkdir -p ~/architech_sdk/architech/zedboard/sysroot/usr/local/Trolltech/
 sudo cp -r /usr/local/Trolltech/Zedboard/* ~/architech_sdk/architech/zedboard/sysroot/usr/local/Trolltech</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

6. Unmount the media used to boot the board from your computer and insert it into the board

7. :ref:`Power-On <poweron_label>` the board

8. Open up the :ref:`serial console <serial_console_label>`.

If you based your root file system on *qt4e-demo-image*, be sure you execute this command

.. raw:: html

 <div>
 <div><b class="admonition-board">&nbsp;&nbsp;Board&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-board-241' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-board-241" class="language-markup">/etc/init.d/qtdemo stop</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

to stop the execution of the demo application.

9. Provide a working :ref:`network <network_label>` connection between your workstation and the board (connector *J11*), so, be sure that:

 1. your board has ip address 192.168.0.10 on interface eth0, and

 2. your PC has an ip address in the same family of addresses, e.g. 192.168.0.100. 

Hello World!
------------

The purpose of this example project is to generate a form with an "Hello World" label in it, at the beginning on the x86 virtual machine and than on ZedBoard board.

To create the project follow these steps:

1. Use the **Welcome Screen** to run Qt Creator by selecting *Architech→ZedBoard→Develop with Qt Creator*

.. image:: _static/qtCreatorStart.jpg
	   :align: center

2. Go to *File -> Open File or Project* to open **QtHelloWorld.pro** file located in */home/architech/architech_sdk/architech/zedboard/workspace/qt/QtHelloWorld/* directory.

3. Click on "QtHelloWorld" icon to open project menu.

.. image:: _static/qt-1.png
	   :align: center

4. Select the build configuration: **Desktop - Debug**.

.. image:: _static/qt-2.jpg
	   :align: center

5. To build the project, click on the bottom-left icon.

.. image:: _static/qt-3.png
	   :align: center

6. Once you built the project, click on the green triangle to run it.

.. image:: _static/qt-4.png
	   :align: center

7. Congratulations! You just built your first Qt application for x86.

.. image:: _static/qt-5.png
	   :align: center

In the next section we will debug our Hello World! application directly on ZedBoard.

Debug Hello World project
-------------------------

1. Select build configuration: **zedboard - Debug** and build the project.

.. image:: _static/qt-10.jpg
	   :align: center

2. Copy the generated executable to the target board (e.g /home/root/).

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-host-154' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-host-154" class="language-markup">scp /home/architech/architech_sdk/architech/zedboard/workspace/qt/build-QtHelloWorld-Hachiko-Debug/QtHelloWorld root@192.168.0.10:/home/root</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

3. Use minicom to launch gdbserver application on the target board:

.. raw:: html

 <div>
 <div><b class="admonition-board">&nbsp;&nbsp;Board&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-board-242' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-board-242" class="language-markup">gdbserver :10000 QtHelloWorld -qws</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

4. | In Qt Creator, open the source file main.cpp and set a breakpoint at line 6. 
    | To do this go with the mouse at line 6 and click with the right button to open the menu, select **Set brackpoint at line 6**

.. image:: _static/qt-6.png
	   :align: center

5. Go to *Debug→Start Debugging→Attach To Remote Debug Server*, a form named "Start Debugger" will appear, insert the following data:

.. image:: _static/qt-7.jpg
	   :align: center

- Kit: **zedboard**

- Local executable:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_creator_rst-host-155' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_creator_rst-host-155" class="language-markup">/home/architech/architech_sdk/architech/zedboard/workspace/qt/build-QtHelloWorld-zedboard-Debug/QtHelloWorld</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Press **OK** button to start the debug.

.. image:: _static/qt-8.png
	   :align: center

6. The hotkeys to debug the application are:

- **F10**: Step over

- **F11**: Step into

- **Shift + F11**: Step out

- **F5**: Continue, or press this icon:

.. image:: _static/qt-9.png
	   :align: center

7. To successfully exit from the debug it is better to close the graphical application from the target board with the mouse by clicking on the 'X' symbol. 