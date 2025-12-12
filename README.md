# Conan Playground

```bash
conan install . -pr="./myprofile"
```

Will produce the following output:

```bash
conanfile.py: Generating build files...
conanfile.py: Dependency: spdlog/1.16.0, Package folder: %CONANCACHE%\p\spdlo5509f6e05a652\p
conanfile.py: Dependency: fmt/12.0.0, Package folder: %CONANCACHE%\p\fmtd0db6d3e7b488\p
conanfile.py: Dependency: cmake/4.2.0, Package folder: %CONANCACHE%\p\cmake20ac4e0137fee\p
```

This shows that package folders of transitive dependencies will be available after the install command.
