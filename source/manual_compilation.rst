Cross compiler
==============

Yocto/OpenEmbedded can be driven to generate the cross-toolchain for your platform.
There are two common ways to get that:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'manual_compilation_rst-host-91' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="manual_compilation_rst-host-91" class="language-markup">bitbake meta-toolchain</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

or

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'manual_compilation_rst-host-92' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="manual_compilation_rst-host-92" class="language-markup">bitbake &lt;image recipe name&gt; -c populate_sdk</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

The first method provides you the toolchain, you need to provide the file system to compile against,
the second method provides both the toolchain and the file system along with -dev and -dbg packages
installed.

Both ways you get an installation script.

The virtual machine has a cross-toolchain installed for each board, each generated with *meta-toolchain*.
To use it just do:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'manual_compilation_rst-host-93' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="manual_compilation_rst-host-93" class="language-markup">source /home/architech/architech_sdk/architech/microzed/toolchain/environment</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

to compile Linux user-space stuff. If you want to compile kernel or bootloader then do:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'manual_compilation_rst-host-94' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="manual_compilation_rst-host-94" class="language-markup">source /home/architech/architech_sdk/architech/microzed/toolchain/environment-nofs</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

and you are ready to go.