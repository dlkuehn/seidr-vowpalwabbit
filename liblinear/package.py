# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Liblinear(MakefilePackage):
    """LIBLINEAR is a simple package for solving large-scale regularized linear
    classification, regression and outlier detection."""

    homepage = "https://www.csie.ntu.edu.tw/~cjlin/liblinear/"

    url = "https://github.com/cjlin1/liblinear/archive/refs/tags/v246.tar.gz"
    list_url = "https://github.com/cjlin1/liblinear/archive/refs/tags/"
    list_depth = 1

    version("246", sha256="88bef33258c0b686a57a8f373ff3eb1912666aadd5a26cfb2101604ef2c64140")
    version("245", sha256="ce29f42c2c0d10e4627ac50a953fe3c130d2802868e6a2dc9a396356b96e8abc")
    version("244", sha256="6e2526245ba4d01bd2660f35f59293fe04e32d5b16fd0372e40d0609df63b373")
    version("243", sha256="925fc8afe26302d18a2b0812fb311093ee15ad11d3d74a0eb43b4a159ff23e36")
    version("242", sha256="7c83100b8b49502f4bde62d46e83cc27f4d7439d96d7c008d542751630d63919")
    version("241", sha256="d86936a8347c9a851bf4240da7136ab20767cb9e31e292bf3e81b61b9143ded3")
    version("240", sha256="629423728a32a434e7fc3ae4a36f7c5488d414ad509f8611516b17d050275d22")
    version("230", sha256="9b57710078206d4dbbe75e9015d4cf7fabe4464013fe0e89b8a2fe40038f8f51")

    depends_on("blas~shared")


    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        libblas = self.spec["blas"].prefix
        makefile.filter("LIBS = blas/blas.a", "LIBS = -lopenblas", string=True)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        mkdirp(prefix.src)
        install("train", prefix.bin)
        install("predict", prefix.bin)
        install("linear.h", prefix.include)
        install("linear.cpp", prefix.src)
        install("linear.o", prefix.lib)
        if self.version == Version("230"):
            install("tron.h", prefix.include)
            install("tron.cpp", prefix.src)
            install("tron.o", prefix.lib)
