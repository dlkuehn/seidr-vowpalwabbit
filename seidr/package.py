# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Seidr(CMakePackage):
    """Seidr is a toolkit to create crowd networks. We provide fast implementations 
    of several highly regarded algorithms as well as utility programs to create 
    and explore crowd networks."""

    homepage = "https://seidr.readthedocs.io/en/latest/"

    url = "https://github.com/bschiffthaler/seidr/releases/download/0.14.2/seidr-0.14.2.tar.gz"

    version("0.14.2", sha256="771442aa7fd8e7ed97d3db465496a6004e163f9c111cd91c19fe86f4961f216f")

    variant("tbb", default=False, description="Enable TBB support")
    variant("mpi", default=False, description="Enable MPI support")

    depends_on("pkg-config", type="build")
    depends_on("armadillo")
    depends_on("blas")
    depends_on("zlib")
    depends_on("clp")
    depends_on("boost+system+serialization+filesystem+program_options")
    depends_on("libnetworkit@7.1:7.1 +static")
    depends_on("libsvm@323:323")
    depends_on("liblinear@230:230")
    depends_on("libtlx")

    depends_on("intel-tbb@2020.3:2020.3", when="+tbb")
    depends_on("mpi", when="+mpi")

    build_directory = 'build'

    patch("deps-cmakelists.patch")
    patch("cmakelists.patch")
    patch("find-clp-cmake.patch")

    def setup_build_environment(self, env):
        if "+tbb" in self.spec:
            env.set("TBB_ROOT", self.spec["tbb"].prefix)
        env.set("CLP_ROOT", self.spec["clp"].prefix)
        env.set("COIN_UTILS_ROOT", self.spec["coinutils"].prefix)
        env.set("LIBLINEAR_ROOT", self.spec["liblinear"].prefix)
        env.set("LIBNETWORKIT_ROOT", self.spec["libnetworkit"].prefix)
        env.set("LIBSVM_ROOT", self.spec["libsvm"].prefix)
        env.set("TLX_ROOT", self.spec["libtlx"].prefix)

    def cmake_args(self):
        args = []
        if "+mpi" in self.spec:
            args.append("-DSEIDR_WITH_MPI=ON")
        else:
            args.append("-DSEIDR_WITHOUT_MPI=ON")
        args.append(self.define_from_variant("SEIDR_PSTL", "tbb"))
        args.append('-DNARROMI_USE_CLP:BOOL=ON')
        return args
