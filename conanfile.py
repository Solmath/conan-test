from conan import ConanFile
import os
import shutil


class TestConan(ConanFile):
    def requirements(self):
        self.requires("spdlog/1.16.0")
        self.requires("zlib/1.3.1")
        self.requires("poco/[>=1.14.2]")
        # Pin transitive dependencies to match poco's existing binary
        self.requires("openssl/3.5.3", override=True)
        self.requires("sqlite3/3.50.4", override=True)
        self.requires("utf8proc/2.8.0", override=True)

    def generate(self):
        self.output.info("\033[1;32mGenerating build files...\033[0m")
        for require, dep in self.dependencies.items():
            self.output.info("\033[1;36m====================================\033[0m")
            self.output.info(f"\033[1;36mDependency: {dep.ref}\033[0m")
            self.output.info(f"  \033[1;32mPackage folder:\033[0m {dep.package_folder}")
            self.output.info(f"  \033[33mdirect:\033[0m {require.direct}")
            self.output.info(f"  \033[33mheaders:\033[0m {require.headers}")
            self.output.info(f"  \033[33mlibs:\033[0m {require.libs}")
            self.output.info(
                f"  \033[33mtransitive_headers:\033[0m {require.transitive_headers}"
            )
            self.output.info(
                f"  \033[33mtransitive_libs:\033[0m {require.transitive_libs}"
            )
            self.output.info(f"  \033[33mpackage_type:\033[0m {dep.package_type}")

    def deploy(self):
        self.output.info("\033[1;32mDeploying package...\033[0m")
        for dep in self.dependencies.values():
            deploy_dir = os.path.join(self.recipe_folder, "deploy")
            os.makedirs(deploy_dir, exist_ok=True)
            if dep.package_folder and os.path.isdir(dep.package_folder):
                package_name = str(dep.ref).replace("/", "_").replace("@", "_")
                dest = os.path.join(deploy_dir, package_name)
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(dep.package_folder, dest)
                self.output.info(f"Copied {dep.ref} to {dest}")
            else:
                self.output.warn(f"Package folder not found for {dep.ref}")
