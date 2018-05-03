# API Upgrade Automation

*API Upgrade Automation* is a script that will upgrade the Api versions in git repos for Salesforce Apex codebase.

1. You can upgrade the Api in multiple repos at the same time.
2. You specify the minimum Api version and the program will upgrade all versions between minimum and maximum desired to maximum Api version.e.g. If you enter Minimum Api version as 20 and maximum Api version as 42, the program will replace all versions between 20 and 41 to 42.


## Usage

*API Upgrade Automation* can be executed as mentioned below

```
$ git clone git@git.soma.salesforce.com:anoop-singh/apiupgrade.git

$ cd apiupgrade

$ ./Main.py

It will prompt for three inputs one after other:
  Enter Git Repo(s) Name/Checkout Branch Name:: 
            You need to specify the git 
            repo and the branch you want to checkout in this format
            [repo1 name/branch name]
            If you have more than one repo, you can have them comma separated as
            [repo1 name/branch name],[repo2 name/branch name]
  Current Minimum API version:: 
            You enter the minimum Api version. It can be 
            any api number (Ideally less than the the maximum version 
            that you are trying to upgrade to)
  What API version to update with:: 
            You enter the Api version that you want to upgrade to.
```

`API Upgrade Automation` sample usage:
* Enter Git Repo(s) Name/Checkout Branch Name:: `Appstore_Renewals/develop`
* Current Minimum API version:: `20`
* What API version to update with:: `41`

API Upgrade Automation sample usage with multiple repos at the same time:
* Enter Git Repo(s) Name/Checkout Branch Name:: `Appstore_Renewals/develop,Appstore_om/work-214,Appstore_Basebiz/work-214`
* Current Minimum API version:: `20`
* What API version to update with:: `41`

## Authors

Anoop Singh by [Anoop Singh](mailto:anoop.singh@salesforce.com).
