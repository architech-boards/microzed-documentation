**********************************
Architech's ZedBoard documentation
**********************************

.. image:: _static/board.png
    :align: center

.. only:: html

.. include:: index_custom.rst

If you are a new user of the **Yocto based SDK** we suggest you to read the :ref:`quick` chapter,
otherwise, if you want to have a better understanding of specific topics, just jump directly to
the chapter that interests you the most.

Furthermore, we encourage you to read the `official Yocto Project documentation <https://www.yoctoproject.org/documentation>`_.

Notations
=========

Throughout this guide, there are commands, file system paths, etc., that can either refer to the
machine (real or virtual) you use to run the SDK or to the board.

.. host::

 This box will be used to refer to the machine running the SDK

.. board::

 This box will be used to refer to ZedBoard board

However, the previous notations can make you struggle with long lines. In such a case, the following
notation is used.
 
.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'index_rst-host-171' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="index_rst-host-171" class="language-markup">This Box will be used where long lines need to be displayed, as well as with system paths, commands, configuration files, etc.
 All related to the host.
 It will be used to display code example as well.</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

.. raw:: html

 <div>
 <div><b class="admonition-board">&nbsp;&nbsp;Board&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'index_rst-board-251' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="index_rst-board-251" class="language-markup">The same facility will be used, when needed, for the board.</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

If you click on *select* on the top right corner of these two last boxes, you will get the text inside the box selected.
We have to warn you that your browser might select the line numbers as well, so, the first time you use such a feature,
you are invited to check it.

Sometimes, when referring to file system paths, the path starts with **/path/to**. In such a case, the documentation is **NOT**
referring to a physical file system path, it just means you need to read the path, understand what it means, and understand
what is the proper path on your system. For example, when referring to the device file associated to your USB flash memory you
could read something like this in the documentation:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'index_rst-host-172' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="index_rst-host-172" class="language-markup">/path/to/your/USB/device</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Since things are different from one machine to another, you need to understand its meaning and corresponding value for your
machine, like for example:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'index_rst-host-173' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="index_rst-host-173" class="language-markup">/dev/sdb</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Chapters
========

.. toctree::
  :maxdepth: 2
  :numbered:

  unboxing
  quick
  sdk-architecture
  create-sdk
  bsp
  tools
  board
  faq