from conans import ConanFile, CMake, tools


class ParallelSTLConan(ConanFile):
    name = "ParallelSTL"
    version = "20181004"
    license = "Apache License 2.0"
    url = "https://github.com/elshize/conan-ParallelSTL"
    code_url = "https://github.com/intel/parallelstl/"
    description = "JSON for Modern C++"

    def source(self):
        self.run("git clone %s" % self.code_url)
        self.run("cd parallelstl && git checkout %s" % self.version)

    def package(self):
        self.copy("*", dst="include", src="parallelstl/include")

    def requirements(self):
        self.requires("TBB/2018_U5@conan/stable")
