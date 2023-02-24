# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VowpalWabbit(CMakePackage):
    """Vowpal Wabbit is a machine learning system which pushes the frontier of
    machine learning with techniques such as online, hashing, allreduce, reductions,
    learning2search, active, and interactive learning. """


    homepage = "https://vowpalwabbit.org/"
    url = "https://github.com/VowpalWabbit/vowpal_wabbit/archive/refs/tags/9.7.0.tar.gz"

    version("9.7.0", sha256="213a9386f35aa958475fa9fc54785353a8180623442eef2876867463efcfefe8")

    build_directory = "build"

    build_target = ["vw_cli_bin"]

    generator = "Ninja"
    depends_on("ninja", type="build")

    variant(
        'flatbuffers', default=False, description='Build with flatbuffers support'
    )

    depends_on("boost+program_options+math+python+test")
    depends_on("eigen")
    depends_on("flatbuffers", when="+flatbuffers")
    depends_on("fmt")
    depends_on("googletest")
    depends_on("help2man")
    depends_on("rapidjson")
    depends_on("spdlog")
    depends_on("zlib")

    def cmake_args(self):
        args = []
        if "+flatbuffers" in self.spec:
            args.append('-DBUILD_FLATBUFFERS="ON"')
        args.append('-DVW_INSTALL:BOOL="ON"')
        args.append('-DFMT_SYS_DEP:BOOL="ON"')
        args.append('-DRAPIDJSON_SYS_DEP:BOOL="ON"')
        args.append('-DSPDLOG_SYS_DEP:BOOL="ON"')
        args.append('-DVW_BOOST_MATH_SYS_DEP:BOOL="ON"')
        args.append('-DVW_EIGEN_SYS_DEP:BOOL="ON"')
        args.append('-DVW_GTEST_SYS_DEP:BOOL="ON"')
        args.append('-DVW_ZLIB_SYS_DEP:BOOL="ON"')
        args.append('-DBUILD_TESTING:BOOL="OFF"')

        return args

