#!/usr/bin/env python

#####################################
# Author: Anoop Singh               #
# Email: anoop.singh@salesforce.com #
# Date: 03-28-2018                  #
#####################################

from __future__ import print_function
from subprocess import call
import subprocess
import os
import sys, traceback
class CLIGitProcess(object):
    command = None

    def __init__(self, comamnd):
        self.command = comamnd

    # 
    #    * Executes git commands (with arguments) specified on the command line.
    #    
    def execute(self, commandArgs, currentWorkingDir, gitCommand):
        PIPE = subprocess.PIPE
        homeDirectory = os.environ["HOME"]
        print("\tHomeDirectory=" + homeDirectory)
        try:
            # String destinationDir = homeDirectory + "/apiupgrade/" + command.getRepoName();
            s = None
            try:
                print(commandArgs)
                popen = subprocess.Popen(commandArgs, cwd=currentWorkingDir, stdout=subprocess.PIPE, shell=True)
                for line in popen.stdout:
                    print(line)

                #process = subprocess.Popen(['git', 'pull', branch], stdout=PIPE, stderr=PIPE)
                #process = subprocess.Popen(commandArgs, shell=True, stdout=PIPE, stderr=PIPE)
                #stdoutput, stderroutput = process.communicate()

                #if 'fatal' in stderroutput:
                #    # Handle error case
                #    print("Error!")
                #    print(stderroutput)
                #else:
                #    # Success!
                #    print("Success!")
                #    print(stdoutput)

                #  using the Runtime exec method:
                #p = Runtime.getRuntime().exec_(commandArgs, None, File(currentWorkingDir))
                #stdInput = BufferedReader(InputStreamReader(p.getInputStream()))
                #stdError = BufferedReader(InputStreamReader(p.getErrorStream()))

                #  OutputStream out = p.getOutputStream();
                #  out.write("sales".getBytes());
                #  out.flush();
                #  read the output from the command


                #print("\t" + gitCommand + " : Here is the standard output of the command:\n")
                #while (s = stdInput.readLine()) != None:
                #    print("\t" + s)
                #  read any errors from the attempted command
                #print("\t" + gitCommand + " : Here is the standard error of the command (if any):\n")
                #while (s = stdError.readLine()) != None:
                #    print("\t" + s)
            except IOError as e:
                print("\tException:")
                traceback.print_exc(file=sys.stdout)
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
