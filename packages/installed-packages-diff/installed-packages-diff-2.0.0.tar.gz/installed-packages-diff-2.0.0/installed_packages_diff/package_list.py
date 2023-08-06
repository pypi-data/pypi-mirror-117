class PackageList(object):
  def __init__(self, packages=None):
    self.packages = {}
    if packages:
      for package in packages:
        self.add_package(package)

  def add_package(self, package):
    versions = self.packages.get(package.name, [])
    versions.append(package.version)
    self.packages[package.name] = versions
