#!/usr/bin/env python

#####################################
# Author: Anoop Singh               #
# Email: anoop.singh@salesforce.com #
# Date: 03-28-2018                  #
#####################################

from __future__ import print_function


class Main(object):
    @classmethod
    def main(cls, args):
        try:
            gitRepoBranchNames = raw_input("Enter Git Repo(s) Name/Checkout Branch Name:: ")
            currentMinApiVersion = raw_input("Current Minimum API version:: ")
            newApiVersion = raw_input("What API version to update with:: ")            

            #  String enteredPassword = new String(console.readPassword("Please enter your ssh passphrase:: "));
            #  print("enteredPassword:" + enteredPassword);
            commands = []
            parts = gitRepoBranchNames.split(",")
            for gitRepoBranchName in parts:
                command = Command()
                commands.append(command)
                command.setCurrentApiVersion(currentMinApiVersion)
                command.setNewApiVersion(newApiVersion)
                repoBranchArray = gitRepoBranchName.split("/")
                command.setRepoName(repoBranchArray[0].strip())
                command.setBranchName(repoBranchArray[1].strip())
            for command in commands:
                cliGit = CLIGit(command)
                cliGit.execute()
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print("Usage: " + "Repo Name/Checkout Branch Name (e.g. Appstore_om/work-214, Appstore_Renewals/develop)" + "\nCurrent Minimum Api Version: (e.g. 39)" + "\nNew Api Version: (e.g. 41)")


if __name__ == '__main__':
    import sys, traceback
    from classes.Command import Command
    from classes.CLIGit import CLIGit
    Main.main(sys.argv)
