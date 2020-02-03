#!/usr/bin/env bash

set -ex

echo "$(git rev-parse HEAD)"
date

dockerfile="./Dockerfile"

if [[ ! -z "$1" ]]; then
    dockerfile="$1"
fi

docker build -t "pecan-prover:latest" - < "$dockerfile"

