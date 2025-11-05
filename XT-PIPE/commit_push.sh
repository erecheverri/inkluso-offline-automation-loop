#!/bin/bash
set -e
cd ..
git add .
git commit -m "Inkluso Offline Build"
git push origin main
echo "Inkluso Offline Loop committed and pushed successfully."
