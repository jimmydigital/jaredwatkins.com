---
date: 2013-05-07
title: "Fixing MySQL SSL Replication Errors"
categories:
  - Personal
  - Computing and Tech
tags:
  - mysql
  - ssl
  - replication
---
I spent 2 nights trying to get mysql replication over ssl to work.. and kept hitting this generic
error message: connection error 2026. After much searching and trying different things I finally
found the solution that worked for me.  If you are hitting this error here's a short list of
things to check.<!--more-->

Searching around I found a few key things to look for when you see this error. First.. make sure your certificate
CNs are unique. Some people mistakenly used the same strings when generating server and client
certificates. When generating your CSR and going through all the cert detail questions your CN
would normally be the fully qualified domain name of the host you are generating the cert for.

    openssl x509 -in <cert file> -noout -noout -subject

Then I would check that you can connect manually from your replication slave to the master.

    mysql -h <master server> --ssl -u <replication user on master>

After you connect make sure your sesson is using ssl by issuing the command "\s". It should
list something like this:
    SSL:                    Cipher in use is DHE-RSA-AES256-SHA

In my case the manual connection was working fine.. but not the replication.

The problem I had was actually with paths used in the 'CHANGE MASTER TO' line on the slave.
When setting values for MASTER_SSL_CA, MASTER_SSL_CERT, and MASTER_SSL_KEY you should specificy
the complete path to the files.  The docs suggest otherwise.. in combination with MASTER_SSL_CAPATH.
I found that particular setting wasn't used the way I expected.. so I left it out and went with
full path names.

Hope that's helpful for someone else!

