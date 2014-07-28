Yocto
=====

The easiest way to setup and keep all the necessary meta-layers in sync with upstream repositories
is achieved by means of Google's **repo** tool.
The following steps are necessary for a clean installation:

1) Install repo tool, if you already have it go to step 4

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-71' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-71" class="language-markup">mkdir -p ~/bin
 sudo apt-get install curl
 curl http://commondatastorage.googleapis.com/git-repo-downloads/repo &gt; ~/bin/repo
 chmod a+x ~/bin/repo</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

2) Make sure directory *~/bin* is included in your *PATH* variable by printing its content

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-72' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-72" class="language-markup">echo $PATH</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

3) If *~/bin* directory is not included, add this line to your *~/.bashrc*

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-73' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-73" class="language-markup">export PATH="$PATH:${HOME}/bin"</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

4) Open a new terminal

5) Change the current directory to the directory where you want all the meta-layers to be downloaded into

6) Download the manifest

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-74' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-74" class="language-markup">repo init -u https://github.com/architech-boards/zedboard-manifest.git -b dora -m manifest.xml</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

7) Download the repositories

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-75' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-75" class="language-markup">repo sync</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

By the end of the last step, all the necessary meta-layers should be in place, anyway, you still need to 
edit your **local.conf** and **bblayers.conf** to compile for zedboard-zynq7 machine and using all the downloaded
meta-layers.

When you want your local repositories to be updated, just:

1) Open a terminal

2) Change the current directory to the directory where you ran repo init

3) Sync your repositories with upstream

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-76' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-76" class="language-markup">repo sync</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

If you really want to download everything by hand, just clone branch *dora* of *meta-xilinx*:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-77' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-77" class="language-markup">git clone -b dora git://git.yoctoproject.org/meta-xilinx.git</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

and have a look at the README file.

To install *Eclipse*, *Qt Creator*, *cross-toolchain*, *NFS*, *TFTP*, etc., read **Yocto**/**OpenEmbedded** documentation, along
with the other tools one.