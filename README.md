# tap-salesloft

`tap-salesloft` is a Singer tap for Salesloft.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
pipx install git+https://github.com/MarkEstey/firehose-tap-salesloft.git
```

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Settings

| Setting                 | Required | Default                   | Description |
|:------------------------|:--------:|:-------------------------:|:------------|
| api_base_url            | False    | https://api.salesloft.com | The base url for the Salesloft API service |
| api_key                 | True     | None                      | The token to authenticate against the API service |
| page_size               | False    | 100                       | The number of results to request per page. Must be in the range 1-100. |
| rate_target_pct         | False    | 80                        | The percentage of the rate limit to consume. Must be in the range 1-100. |
| start_date              | False    | 2011-09-01T00:00:00+00:00 | The earliest record date to sync |
| stream_type_conformance | False    | root_only                 | The level of type conformance to apply to streams (see: https://sdk.meltano.com/en/latest/classes/singer_sdk.Stream.html#singer_sdk.Stream.TYPE_CONFORMANCE_LEVEL). Defaults to 'root_only'. Must be one of: 'none', 'root_only', 'recursive' |
| stream_maps             | False    | None                      | Inline stream maps (see: https://sdk.meltano.com/en/latest/stream_maps.html) |
| stream_maps_config      | False    | None                      | Inline stream maps config (see: https://sdk.meltano.com/en/latest/stream_maps.html) |
| user_agent              | False    | tap-salesloft             | The user-agent string provided on outgoing requests |
| stream_map_config       | False    | None                      | User-defined config values to be used within map expressions. |
| flattening_enabled      | False    | None                      | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth    | False    | None                      | The max depth to flatten schemas. |
| batch_config            | False    | None                      |             |

A full list of supported settings and capabilities for this tap is available by running:

```bash
tap-salesloft --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

Follow the steps in [API Key Authentication](https://developers.salesloft.com/docs/platform/api-basics/api-key-authentication) to obtain
an API key and provide it to the tap via the `api_key` setting. Note that the permissions of the account used to obtain the API key will
affect the tap.

## Usage

You can easily run `tap-salesloft` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-salesloft --version
tap-salesloft --help
tap-salesloft --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-salesloft
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-salesloft --version
# OR run a test `elt` pipeline:
meltano elt tap-salesloft target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
