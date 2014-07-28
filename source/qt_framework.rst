.. _qt_framework_label:

Qt Framework
============

The Qt Framework used by this SDK is composed of libraries for your host machine and your target.
To compile the libraries for *x86* you only need your distribution toolchain, while to compile the
libraries for ZedBoard board you need the proper cross-toolchain (see Chapter :ref:`manual_compilation_label`
for further information on how to get it).

This section just wants to show you how the framework has been generated.

Before to begin, keep in mind you might need to install the following package to compile yourself
the libraries under Ubuntu

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_framework_rst-host-91' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_framework_rst-host-91" class="language-markup">sudo apt-get install libxrender-dev</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

So, to install *qt-everywhere* for *x86* from sources, the usual drill of download, uncompress, *configure*,
*make* and *make install* is required:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_framework_rst-host-92' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_framework_rst-host-92" class="language-markup">wget http://download.qt-project.org/official_releases/qt/4.8/4.8.5/qt-everywhere-opensource-src-4.8.5.zip
 unzip qt-everywhere-opensource-src-4.8.5.zip
 cd qt-everywhere-opensource-src-4.8.5
 ./configure /*Choose Open source Edition when asked, and accept the license*/
 make
 make install</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

The installation of the libraries for ZedBoard from sources is sligthly more complicated. Once you downloaded
and uncompressed the sources

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_framework_rst-host-93' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_framework_rst-host-93" class="language-markup">wget http://download.qt-project.org/official_releases/qt/4.8/4.8.5/qt-everywhere-opensource-src-4.8.5.zip
 unzip qt-everywhere-opensource-src-4.8.5.zip
 cd qt-everywhere-opensource-src-4.8.5
 cp -r mkspecs/qws/linux-arm-g++/ mkspecs/qws/linux-zedboard-g++
 cd mkspecs/qws/linux-zedboard-g++/
 gedit qmake.conf</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

you need to customize *qmake* configuration

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_framework_rst-host-94' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_framework_rst-host-94" class="language-markup">#
 # qmake configuration for building with arm-linux-g++
 #
 
 include(../../common/linux.conf)
 include(../../common/gcc-base-unix.conf)
 include(../../common/g++-unix.conf)
 include(../../common/qws.conf)
 
 # modifications to g++.conf
 QMAKE_CC                = arm-poky-linux-gnueabi-gcc --sysroot=/home/architech/architech_sdk/architech/zedboard/toolchain/sysroots/armv7a-vfp-neon-poky-linux-gnueabi
 QMAKE_CXX               = arm-poky-linux-gnueabi-g++ --sysroot=/home/architech/architech_sdk/architech/zedboard/toolchain/sysroots/armv7a-vfp-neon-poky-linux-gnueabi
 QMAKE_LINK              = arm-poky-linux-gnueabi-g++ --sysroot=/home/architech/architech_sdk/architech/zedboard/toolchain/sysroots/armv7a-vfp-neon-poky-linux-gnueabi
 QMAKE_LINK_SHLIB        = arm-poky-linux-gnueabi-g++ --sysroot=/home/architech/architech_sdk/architech/zedboard/toolchain/sysroots/armv7a-vfp-neon-poky-linux-gnueabi
 
 # modifications to linux.conf
 QMAKE_AR                = arm-poky-linux-gnueabi-ar cqs
 QMAKE_OBJCOPY           = arm-poky-linux-gnueabi-objcopy
 QMAKE_STRIP             = arm-poky-linux-gnueabi-strip
 
 load(qt_config)</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

save the file and exit from gedit, then *configure*, *make* and *make install*

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'qt_framework_rst-host-95' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="qt_framework_rst-host-95" class="language-markup">cd ../../../
 ./configure -no-pch -opensource -confirm-license -prefix /usr/local/Trolltech/Zedboard -no-qt3support -embedded arm -nomake examples -nomake demo -little-endian -xplatform qws/linux-zedboard-g++ -qtlibinfix E
 make
 make install</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

A comfortable tool to get your job done with Qt is *Qt Creator*, which its use will be introduced
in Section :ref:`qt_creator_label`. You can download it from here:

.. tip::

 http://sourceforge.net/projects/qtcreator.mirror/files/Qt%20Creator%202.8.1/qt-creator-linux-x86-opensource-2.8.1.run/download