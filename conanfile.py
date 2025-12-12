from conan import ConanFile

class TestConan(ConanFile):
    
    def requirements(self):
        self.requires("spdlog/1.16.0")
    
    def generate(self):
        self.output.info("Generating build files...")
        for dep in self.dependencies.values():
            self.output.info(f"Dependency: {dep.ref}, Package folder: {dep.package_folder}")
