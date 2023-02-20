# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libsvm(MakefilePackage):
    """Libsvm is a simple, easy-to-use, and efficient software for SVM
    classification and regression."""

    homepage = "https://www.csie.ntu.edu.tw/~cjlin/libsvm/"

    url = "https://github.com/cjlin1/libsvm/archive/refs/tags/v330.tar.gz"
    list_url = "https://github.com/cjlin1/libsvm/archive/refs/tags/"
    list_depth = 1

    version("330", sha256="e4fe41308c87cc210aec73e4f5f0fb4da14234d90e7a131763fbad3788ca2d80")
    version("325", sha256="1f587ec0df6fd422dfe50f942f8836ac179b0723b768fe9d2fabdfd1601a0963")
    version("324", sha256="3ba1ac74ee08c4dd57d3a9e4a861ffb57dab88c6a33fd53eac472fc84fbb2a8f")
    version("323", sha256="7a466f90f327a98f8ed1cb217570547bcb00077933d1619f3cb9e73518f38196")
    version("322", sha256="a3469436f795bb3f8b1e65ea761e14e5599ec7ee941c001d771c07b7da318ac6")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.lib)
        mkdirp(prefix.include)
        mkdir(prefix.src)
        install("svm-predict", prefix.bin)
        install("svm-scale", prefix.bin)
        install("svm-train", prefix.bin)
        install("svm.cpp", prefix.src)
        install("svm.h", prefix.include)
        install("svm.o", prefix.lib)
