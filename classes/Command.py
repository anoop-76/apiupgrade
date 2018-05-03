#!/usr/bin/env python

#####################################
# Author: Anoop Singh               #
# Email: anoop.singh@salesforce.com #
# Date: 03-28-2018                  #
#####################################

from __future__ import print_function
class Command(object):
    repoName = None
    branchName = None
    currentApiVersion = None
    newApiVersion = None

    def __init__(self):
        """  __init__ """

    def getRepoName(self):
        return self.repoName

    def setRepoName(self, repoName):
        self.repoName = repoName

    def getRepoRemoteURL(self):
        return "git@git.soma.salesforce.com:IT/" + self.repoName + ".git"

    def getBranchName(self):
        return self.branchName

    def setBranchName(self, branchName):
        self.branchName = branchName

    def getCurrentApiVersion(self):
        return self.currentApiVersion

    def setCurrentApiVersion(self, currentApiVersion):
        self.currentApiVersion = currentApiVersion

    def getNewApiVersion(self):
        return self.newApiVersion

    def setNewApiVersion(self, newApiVersion):
        self.newApiVersion = newApiVersion

    def __str__(self):
        return "[Command]: repoName=" + self.repoName + " ,branchName=" + self.branchName + " ,currentApiVersion=" + self.currentApiVersion + " ,newApiVersion=" + self.newApiVersion
