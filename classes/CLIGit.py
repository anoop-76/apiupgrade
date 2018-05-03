#!/usr/bin/env python

#####################################
# Author: Anoop Singh               #
# Email: anoop.singh@salesforce.com #
# Date: 03-28-2018                  #
#####################################

from __future__ import print_function
from CLIGitProcess import CLIGitProcess
from ApiUpgrade import ApiUpgrade
import os
import shutil
class CLIGit(object):
    command = None
    workingDir = None
    cloneDir = None

    def __init__(self, command):
        self.command = command
        self.workingDir = os.environ["HOME"]
        print(self.workingDir)

        self.cloneDir = self.workingDir + "/apiupgrade/" 
        self.workingDir = self.cloneDir + self.command.getRepoName()

    def execute(self):
        print("\n\n************************************************")
        print(self.command.getRepoName() + ": START Upgrading Api")
        print("************************************************")
        print("\n\tWorkingDir=" + self.workingDir)
        self.cloneRepo()
        self.createBranch()
        self.upgrade()
        self.commit()
        self.push()
        print("\n\n************************************************")
        print(self.command.getRepoName() + ": END Upgrading Api")
        print("************************************************\n")

    def cloneRepo(self):
        self.cleanRepo()

        commandArgs = " git clone " + self.command.getRepoRemoteURL()
        #  ssh-agent -s
        #  ssh-add ~/.ssh/id_rsa
        CLIGitProcess(self.command).execute(commandArgs, self.cloneDir, "clone")

    def createBranch(self):
        branchName = "work-apiupgrade"
        commandArgs = " git checkout " + self.command.getBranchName()
        CLIGitProcess(self.command).execute(commandArgs, self.workingDir, "createBranch")
        commandArgs2 = " git checkout -b " + branchName
        CLIGitProcess(self.command).execute(commandArgs2, self.workingDir, "createBranch")

    def commit(self):
        commandArgs = " git commit -m 'api-upgrade-changes' "
        CLIGitProcess(self.command).execute(commandArgs, self.workingDir, "commit")

    def push(self):
        commandArgs = " git push -u origin work-apiupgrade "
        CLIGitProcess(self.command).execute(commandArgs, self.workingDir, "push")

    def upgrade(self):
        upgrade = ApiUpgrade(self.workingDir, self.command)
        upgrade.upgrade()

    def cleanRepo(self):
        try:
            shutil.rmtree(self.workingDir)
        except OSError, e:
            print ("Error: %s - %s." % (e.filename,e.strerror))        
        if not os.path.exists(self.workingDir):
            os.makedirs(self.workingDir)

    
