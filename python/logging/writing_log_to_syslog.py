#!/usr/bin/python3

import syslog
syslog.syslog('processing started')
if error:
	syslog.syslog(syslog.LOG_ERR,'Processing started')
