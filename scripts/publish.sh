#!/usr/bin/bash

set -x

# Build page with Hugo
cd page
hugo build
cd -

# Copy files to the server
source ".env"
rsync -azrvh --progress -e "ssh -p $PORT" $SOURCE $HOST:$DEST

# Reload nginx
ssh $HOST -p $PORT -t nginx -s reload
