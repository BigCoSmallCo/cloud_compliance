# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2018-12-21
### Changed
- Instances with no labels now being handles properly (bugfix)
- Deploy script installing dependencies

## [1.1.0] - 2018-12-18
### Added
- Systemctl service and scripts.
- subdirectory for scripts

### Changed
- Init.d setup changed to systemctl
- cloud-label.sh changed to instance-start.sh

## [1.0.3] - 2018-12-18
### Change
- Typographical bugfix

## [1.0.2] - 2018-12-17
### Added
- Documentation updates.

### Changed
- Argument name for compr (bugfix).
- changed get_labels to set_labels(bugfix).

## [1.0.1] - 2018-12-17
### Added
- Deploy script for unix based systems.

### Changed
- Project rename.
- Filenames changed.

## [1.0.0] - 2018-12-17
### Added
- Added arguments & argparse

### Removed
- Looping.
- Port checking.
- Regex.
- Daemonization.
- system detection.

## [0.2.0] - 2018-12-14
### Added
- Operation checking for api calls.
- regex for grabbing port numbers.
- Variable label setting.
- Shell script for running as Daemon.
- Logging

### Changed
- API calls changed to googleapiclient
- Metadata calls changed functionally.

## [0.1.0] - 2018-12-7
### Added
- Functions for grabbing instance metadata and access tokens.
- Global variables for meta info.

### Removed
- Temporary URL's for Metadata calls.

## [0.0.1] - 2018-12-6
### Added
- Local monitoring for port 22 on a 1 second loop.
- Temporary URL's for GCP Metadata calls.
