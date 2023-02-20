# seidr-vowpalwabbit

<b>osi</b> - On host without pkg-config installed (e.g. Ubuntu 22.04 +build-essential), the OSI install cannot find the CoinUtils dependency and fails.

<b>clp</b> - On host without pkg-config installed (e.g. Ubuntu 22.04 +build-essential), the CLp install cannot find the CoinUtils dependency and fails.

<b>libnetworkit</b><p>
<ul>
  <li>prioqueue_hpp.patch - (@6.1:8.1) add #include <limits> to include/networkit/auxiliary/PrioQueue.hpp 
                           which resolves the below error when compiled with a recent g++:
 
  >> 92     /tmp/dkuehn/spack-stage/spack-stage-libnetworkit-7.0-o5rrxqdxfca2vahxywpyf4wrd7hemauu/spack-src/include/networkit/auxil
            iary/PrioQueue.hpp:31:32: error: 'numeric_limits' is not a member of 'std'
     93        31 |     const Key undefined = std::numeric_limits<Key>::max(); // TODO: make static
     94           |                                ^~~~~~~~~~~~~~

  <li>point_hpp.patch - (@6.1:6.1) add #include <stdexcept> to include/networkit/viz/Point.hpp which resolves the below error when compiled
                        with a recent g++:
                        
  >> 87     /tmp/dkuehn/spack-stage/spack-stage-libnetworkit-6.1-l6b5r6ztoqxtz3flxa4nbqgjkjhj2caj/spack-src/include/networkit/auxil
            iary/PrioQueue.hpp:31:32: error: 'numeric_limits' is not a member of 'std'
     88        31 |     const Key undefined = std::numeric_limits<Key>::max(); // TODO: make static
     89           |                                ^~~~~~~~~~~~~~
</ul>
</p>

<b>libsvm</b> - Add new versions, install source files to $PREFIX/src.
<p></p>
<b>liblinear</b> - New package
<p></p>
<b>seidr</b> - new package
<p></p>
<b>py-vowpalwabbit</b> - new package
<p></p>
<b>vowpal-wabbit</b> - new package
