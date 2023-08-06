# target-localjson

## Intro

This Singer Target implements a simple way persist data as local json files.

## Install

pip install target-localjson

## Config

To execute the Tap in Sync Mode you have to provide a config.json file.

There is only one required key: dest_dir. It must be a string and represents the destination directory where json files will be persisted. 

For each stream received, the Target creates a subdirectory and puts the json files there.

**Requires write permission on dest_dir.**

## Run Target

e.g.

    tap-<your-choice> -c tap_sample_config.json | target-localjson -c sample_config.json