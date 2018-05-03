#!/usr/bin/env python

#####################################
# Author: Anoop Singh               #
# Email: anoop.singh@salesforce.com #
# Date: 03-28-2018                  #
#####################################

from __future__ import print_function
from CLIGitProcess import CLIGitProcess
import os, sys, traceback
class ApiUpgrade(object):
    workingDir = None
    command = None

    def __init__(self, workingDir, command):
        """ generated source for method __init__ """
        self.workingDir = workingDir
        self.command = command

    def upgrade(self):
        self.walk(self.workingDir)
        self.addFile()

    def walk(self, path):
        try:
            for root, directories, files in os.walk(path):
                if 'de' in directories:
                    directories.remove('de')

                for filename in files:
                    # Join the two strings in order to form the full filepath.
                    filepath = os.path.join(root, filename)
                    if filepath.endswith("-meta.xml") or filepath.endswith("package.xml"):

                        try:
                            # Read in the file
                            with open(filepath, 'r') as file :
                                filedata = file.read()
                                file.close()

                            index = int(self.command.getCurrentApiVersion())
                            while index < int(self.command.getNewApiVersion()):
                                # Replace the target string
                                filedata = filedata.replace("<apiVersion>" + str(index) + ".0</apiVersion>", "<apiVersion>" + self.command.getNewApiVersion() + ".0</apiVersion>")
                                filedata = filedata.replace("<version>" + str(index) + ".0</version>", "<version>" + self.command.getNewApiVersion() + ".0</version>")
                                index += 1
                            
                            # Write the file out again
                            with open(filepath, 'w') as file:
                                file.write(filedata)
                                file.close()
                                
                        except IOError as e:
                            traceback.print_exc(file=sys.stdout)

        except Exception as e:
            traceback.print_exc(file=sys.stdout)

    def addFile(self):
        commandArgs = "git add . "
        CLIGitProcess(self.command).execute(commandArgs, self.workingDir, "add")
