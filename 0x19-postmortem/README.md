# Wordpress website running on a LAMP stack outage incident report
## Issue Summary
From 6:00 AM to 8:06 AM WAT, request to ALX Wordpress website running on LAMP stack
resulted in 500 error response messages. At its peak, 100% of traffic to this website
is affected. Users could not benefit from the services provided on this website.
The root cause of this outage is the typo in the Wordpress configuration file where
PHP file is to be included but with a wrong extension.

## Timeline (all times West African Time)
- 6:00 AM: The sandbox hosting the website was released. The issue was detected by
		   an engineer he was trying to access the website.
- 7:00 AM: The current running process was investigated together with the open port,
		   it was assumed that the error occurred when the server is trying to get some resources.
- 7:05 AM: The error log of MySQL running on the server was investigated, as well as
		   the PHP and Apache log files, which were all misleading investigations.
- 7:10 AM: [strace](https://strace.io/) debugging tool was used to track the system calls used in running the
		   Apache2 process to detect any failed call with the aid of [tmux](https://hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/).
- 7:45 AM: It was analysed that a file with wrong extension was included in one of the Wordpress
		   configuration files where the extension was 'phpp' instead of 'php'.
		   This led to tracing the file and line where this error occurred in the server codebase.
- 8:05 AM: The configuration file was located and the affected line was corrected with a Puppet code.
- 8:06 AM: 100% of traffic back online

## Root cause
At 6:00 AM WAT, the sandbox was released for debugging by the technical team of ALX.
When a request is made to the server, 500 error response message was received. The issue
affected 100% of the traffic coming to the server.

At 7:00 AM the debugging process started by investigating the running processes.
All the stack composition log files were investigated before [strace](https://strace.io/)
was finally used to check the system calls used in the current running Apache process.
All files are read correctly until a line 137 was reached in the file
`/var/wwww/html/wp-settings.php` where the expected file extension to be used
was included wrongly.

## Resolution and recovery
At 7:10 AM WAT, [tmux](https://hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) was used to
run [strace](https://strace.io/) on a window and `curl` on another one. The system
calls were traced till a negative output value was encountered. This gave an hint
on what went wrong.

The identified file name was searched in the Wordpress codebase recursively with `grep`
command together with option `n` to get the number where the typo occurred.
The error was then fixed using Puppet `exec` resource type and the website
was resolved and 100% accessible at 8:06 AM.

## Corrective and preventative measures
This situation can be improved by practicing Continuous Integration (CI), the use
of monitoring tools and placing engineers on-call. The following actions can also
be taken.
- Automation of file configuration process.
- Implementation of vigorous testing before deployment to production environment.
- Creation of redundancy in the server to avoid total outage.
