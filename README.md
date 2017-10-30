Requirements
------------
* Git
* Docker

Tested on
---------
* Host machine OS: Ubuntu 16.04
* Docker version 17.05.0-ce

Set up
------
```
git clone git@github.com:michick/test-docker.git
cd test-docker
./start.sh
```

Done
----
Connect to localhost:22 by SFTP. Upload files to upload directory.
User and password impraise:impraise.

Notes
-----
Of course directory /tmp/tmptest will not be suitable for production. Instead directory with proper permissions should be used.
