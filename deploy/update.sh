#!/bin/sh
# Pull the latest main branch of the atlas so the project page stays current.
# Install once:  git clone https://github.com/savorcode/bci-paradigm-atlas.git /var/www/bci-paradigm-atlas
# Schedule:      crontab -e  ->  */10 * * * * /var/www/bci-paradigm-atlas/deploy/update.sh >> /var/log/atlas-update.log 2>&1
set -eu
cd /var/www/bci-paradigm-atlas
git fetch --quiet origin main
if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
    git reset --quiet --hard origin/main
    echo "$(date '+%F %T') updated to $(git rev-parse --short HEAD)"
fi
