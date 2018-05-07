# Source: http://stackoverflow.com/a/5839291
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
    print ("Upgrading.......")
