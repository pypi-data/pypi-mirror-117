#!/usr/bin/env python
########################################################################
# File :    dirac-wms-job-logging-info
# Author :  Stuart Paterson
########################################################################
"""
Retrieve history of transitions for a DIRAC job

Usage:
  dirac-wms-job-logging-info [options] ... JobID ...

Arguments:
  JobID:    DIRAC Job ID

Example:
  $ dirac-wms-job-logging-info 1
  Status                        MinorStatus                         ApplicationStatus             DateTime
  Received                      Job accepted                        Unknown                       2011-02-14 10:12:40
  Received                      False                               Unknown                       2011-02-14 11:03:12
  Checking                      JobSanity                           Unknown                       2011-02-14 11:03:12
  Checking                      JobScheduling                       Unknown                       2011-02-14 11:03:12
  Waiting                       Pilot Agent Submission              Unknown                       2011-02-14 11:03:12
  Matched                       Assigned                            Unknown                       2011-02-14 11:27:17
  Matched                       Job Received by Agent               Unknown                       2011-02-14 11:27:27
  Matched                       Submitted To CE                     Unknown                       2011-02-14 11:27:38
  Running                       Job Initialization                  Unknown                       2011-02-14 11:27:42
  Running                       Application                         Unknown                       2011-02-14 11:27:48
  Completed                     Application Finished Successfully   Unknown                       2011-02-14 11:28:01
  Completed                     Uploading Output Sandbox            Unknown                       2011-02-14 11:28:04
  Completed                     Output Sandbox Uploaded             Unknown                       2011-02-14 11:28:07
  Done                          Execution Complete                  Unknown                       2011-02-14 11:28:07
"""
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

__RCSID__ = "$Id$"

import DIRAC
from DIRAC.Core.Base import Script
from DIRAC.Core.Utilities.DIRACScript import DIRACScript


@DIRACScript()
def main():
  Script.parseCommandLine(ignoreErrors=True)
  args = Script.getPositionalArgs()

  if len(args) < 1:
    Script.showHelp(exitCode=1)

  from DIRAC.Interfaces.API.Dirac import Dirac, parseArguments
  dirac = Dirac()
  exitCode = 0
  errorList = []

  for job in parseArguments(args):

    result = dirac.getJobLoggingInfo(job, printOutput=True)
    if not result['OK']:
      errorList.append((job, result['Message']))
      exitCode = 2

  for error in errorList:
    print("ERROR %s: %s" % error)

  DIRAC.exit(exitCode)


if __name__ == "__main__":
  main()
