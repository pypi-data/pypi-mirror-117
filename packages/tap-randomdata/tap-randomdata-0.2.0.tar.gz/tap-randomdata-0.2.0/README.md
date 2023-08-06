# Singer Demo

## Intro

This Singer Tap implements a simple way to generate random data, using https://random-data-api.com/ as source.

## Available Streams

This Tap supports the Streams listed below:

- Company
- Restaurant
- Address
- Vehicle
- Food

Please, check https://random-data-api.com/documentation for more information.

## Config

To execute the Tap in Sync Mode you have to provide a config.json file.

There is only one required key: record_count. It must be a integer and represents the number of record to be generated.

Please check [sample_file](tap-randomdata/sample_config.json) for an example.