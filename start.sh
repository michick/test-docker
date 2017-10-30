#!/usr/bin/env bash

set -e
# create dir for shared volume if doesn't exist
if [ ! -d "/tmp/tmptest" ]; then
  mkdir /tmp/tmptest
fi

# run containers
docker run --rm --name test-remove-it -p 22:22 -v /tmp/tmptest:/home/impraise/upload -d atmoz/sftp impraise:impraise:::upload \
&& docker build -t test-watcher . \
&& docker run --rm -v /tmp/tmptest:/var/impraise test-watcher

# cleanup before exiting
function cleanup {
  docker stop test-remove-it
  rm -rf /tmp/tmptest
}

trap cleanup EXIT

