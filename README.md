# seidr-vowpalwabbit

<b>osi</b> - On host without pkg-config installed (e.g. Ubuntu 22.04 +build-essential), the OSI install cannot find the CoinUtils dependency and fails.

<b>clp</b> - On host without pkg-config installed (e.g. Ubuntu 22.04 +build-essential), the CLp install cannot find the CoinUtils dependency and fails.

<b>libnetworkit</b><p>
<ul>
  <li>prioqueue_hpp.patch - (@6.1:8.1) add <code>#include &lt;limits&gt;</code> to include/networkit/auxiliary/PrioQueue.hpp 
                           which resolves the below error when compiled with a recent g++:
  <blockquote><pre><code>
  >> 92     include/networkit/auxiliary/PrioQueue.hpp:31:32: error: 'numeric_limits' is not a member of 'std'
     93        31 |     const Key undefined = std::numeric_limits&lt;Key&gt;::max(); // TODO: make static
     94           |                                ^~~~~~~~~~~~~~
  </code></pre></blockquote>
  </li>
  <li>point_hpp.patch - (@6.1:6.1) add <code>#include &lt;stdexcept&gt;</code> to include/networkit/viz/Point.hpp which resolves the below error when compiled
                        with a recent g++:
  <blockquote><pre><code>                      
   >> 712    include/networkit/viz/Point.hpp:327:24:error: 'out_of_range' is not a member of 'std'
     713      327 |             throw std::out_of_range{""};
     714          |                        ^~~~~~~~~~~~
    </code></pre></blockquote>
    </li>
</ul>
</p>

<b>libsvm</b> - Add new versions, install source files to $PREFIX/src, add alternate package file.
<p></p>
<b>liblinear</b> - New package, add alternate package file.
<p></p>
<b>seidr</b> - new package
<p></p>
<b>py-vowpalwabbit</b> - new package
<p></p>
<b>vowpal-wabbit</b> - new package
