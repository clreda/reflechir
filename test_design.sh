#!/bin/bash

scp -r design-site/ $myOVH:~/reflechir-test/reflechir
ssh $myOVH './reflechir-test/start_server.sh'
exit
