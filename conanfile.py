from conans import ConanFile, CMake, tools


class ParallelSTLConan(ConanFile):
    name = "ParallelSTL"
    version = "20181004"
    license = "Apache License 2.0"
    url = "https://github.com/elshize/conan-ParallelSTL"
    code_url = "https://github.com/intel/parallelstl/"
    generators = "cmake_paths"

    def source(self):
        self.run("git clone https://github.com/justusc/FindTBB.git")
        self.run("git clone %s" % self.code_url)
        #self.run("cp FindTBB/FindTBB.cmake parallelstl")
        self.run("cd parallelstl && git checkout %s" % self.version)

    def package(self):
        tools.replace_in_file("parallelstl/CMakeLists.txt",
                "project(ParallelSTL VERSION ${VERSION_MAJOR}.${VERSION_MINOR} LANGUAGES CXX)",
                '''project(ParallelSTL VERSION ${VERSION_MAJOR}.${VERSION_MINOR} LANGUAGES CXX)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../FindTBB")''')
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = 'conan_paths.cmake'
        cmake.configure(source_dir='parallelstl')
        self.copy("*", dst="include", src="parallelstl/include")
        self.copy("*.cmake")

    def requirements(self):
        self.requires("TBB/2018_U5@conan/stable")
