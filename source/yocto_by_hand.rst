Yocto
=====

If you have launched machine_installer or run_install.sh script, yocto is already installed. 
The following steps are useful for understood how the sdk works "under the hood".

Installation with repo
----------------------

The easiest way to setup and keep all the necessary meta-layers in sync with upstream repositories
is achieved by means of Google's **repo** tool.
The following steps are necessary for a clean installation:

1) Install repo tool, if you already have it go to step 4

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-31' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-31" class="language-markup">mkdir -p ~/bin
 sudo apt-get install curl
 curl http://commondatastorage.googleapis.com/git-repo-downloads/repo &gt; ~/bin/repo
 chmod a+x ~/bin/repo</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

2) Make sure directory *~/bin* is included in your *PATH* variable by printing its content

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-32' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-32" class="language-markup">echo $PATH</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

3) If *~/bin* directory is not included, add this line to your *~/.bashrc*

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-33' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-33" class="language-markup">export PATH="$PATH:${HOME}/bin"</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

4) Open a new terminal

5) Change the current directory to the directory where you want all the meta-layers to be downloaded into

6) Download the manifest

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-34' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-34" class="language-markup">repo init -u https://github.com/architech-boards/microzed-manifest.git -b dizzy -m manifest.xml</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

7) Download the repositories

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-35' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-35" class="language-markup">repo sync</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

By the end of the last step, all the necessary meta-layers should be in place, anyway, you still need to 
edit your **local.conf** and **bblayers.conf** to compile for microzed machine and using all the downloaded
meta-layers.

Updating with repo
------------------

When you want your local repositories to be updated, just:

1) Open a terminal

2) Change the current directory to the directory where you ran repo init

3) Sync your repositories with upstream

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-36' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-36" class="language-markup">repo sync</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

Install Yocto by yourself
-------------------------

If you really want to download everything by hand, just clone branch *dizzy* of *meta-xilinx*:

.. raw:: html

 <div>
 <div><b class="admonition-host">&nbsp;&nbsp;Host&nbsp;&nbsp;</b>&nbsp;&nbsp;<a style="float: right;" href="javascript:select_text( 'yocto_by_hand_rst-host-37' );">select</a></div>
 <pre class="line-numbers pre-replacer" data-start="1"><code id="yocto_by_hand_rst-host-37" class="language-markup">git clone -b dizzy git://git.yoctoproject.org/meta-xilinx.git</code></pre>
 <script src="_static/prism.js"></script>
 <script src="_static/select_text.js"></script>
 </div>

and have a look at the README file.

To install *Eclipse*, *Qt Creator*, *cross-toolchain*, *NFS*, *TFTP*, etc., read **Yocto**/**OpenEmbedded** documentation, along
with the other tools one.