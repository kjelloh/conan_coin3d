from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
# from conan.tools.scm import Git
import subprocess


class coin3dRecipe(ConanFile):
    name = "coin3d"
    version = "4.0.3"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of coin3d package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def source(self):
        # git = Git(self)
        # git.run("clone https://github.com/coin3d/coin.git")
        # git.run("checkout 8f19fe933040bbbe74dee474ad2231291b9b306e")
        subprocess.run(["git", "clone", "--recurse-submodules", "https://github.com/coin3d/coin.git"], check=True)
        subprocess.run(["git", "-C", "coin", "checkout", "8f19fe933040bbbe74dee474ad2231291b9b306e"], check=True)

    def requirements(self):
        self.requires("boost/1.87.0")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")
        if self.options.get_safe("boost"):
            self.options["boost"].header_only = True            

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["coin3d"]

