# atcf-data-parser

A Python parser and command-line utility for the “a-deck” data posted online by the Automated Tropical Cyclone Forecasting System

Intended to read the cyclone forecasts posted as gzipped files to [ftp.nhc.noaa.gov/atcf/aid_public/](https://ftp.nhc.noaa.gov/atcf/aid_public/).

## Installation

Install the package from the Python Package Index (PyPI) with pipenv:

```bash
pipenv install atcf-data-parser
```

## Usage

You'll want to start with a URL to a gzipped a-deck file listed in the government FTP at [ftp.nhc.noaa.gov/atcf/aid_public/](https://ftp.nhc.noaa.gov/atcf/aid_public/). We will use 2023's Hurricane Otis, which had the id of ep182023, as our example.

From Python, you can download a pandas dataframe:

```python
import atcf_data_parser

url = "https://ftp.nhc.noaa.gov/atcf/aid_public/aep182023.dat.gz"
df = atcf_data_parser.get_dataframe(url)
```

Alternatively, from the command line you can output a CSV to stdout:

```bash
atcf-data-parser get-comma-delimited-data https://ftp.nhc.noaa.gov/atcf/aid_public/aep182023.dat.gz
```

## Reference

Here's more about how our utilities work.

### Python Functions

A collection of functions for downloading and parsing ATCF data posted to [its public FTP site](https://ftp.nhc.noaa.gov/atcf/aid_public/)

```{eval-rst}
.. autofunction:: atcf_data_parser.get_dataframe
.. autofunction:: atcf_data_parser.get_gzipped_url
```

### Command-line Interface

A command-line utility for downloading and parsing ATCF data posted to [its public FTP site](https://ftp.nhc.noaa.gov/atcf/aid_public/)


```bash
Usage: atcf-data-parser [OPTIONS] COMMAND [ARGS]...

  Parse “a-deck” data posted online by the Automated Tropical Cyclone
  Forecasting System.

Options:
  --help  Show this message and exit.

Commands:
  get-comma-delimited-data  Download a comma-delimited file from a URL...
  get-fixed-width-data      Download a fixed-width file from a URL and..
```

### get-comma-delimited-data

```bash
Usage: atcf-data-parser get-comma-delimited-data [OPTIONS] URL

  Download a comma-delimited file from a URL and print its contents.

Options:
  --help  Show this message and exit.
```

### get-fixed-width-data

```bash
Usage: atcf-data-parser get-fixed-width-data [OPTIONS] URL

  Download a fixed-width file from a URL and print its contents.

Options:
  --help  Show this message and exit.
```

## Links

- Source: [ftp.nhc.noaa.gov/atcf/aid_public/](https://ftp.nhc.noaa.gov/atcf/aid_public/)
- Data dictionary: [www.nrlmry.navy.mil/atcf_web/docs/database/new/abdeck.txt](https://www.nrlmry.navy.mil/atcf_web/docs/database/new/abdeck.txt)
- Model definitions: [ftp.nhc.noaa.gov/atcf/docs/nhc_techlist.dat](https://ftp.nhc.noaa.gov/atcf/docs/nhc_techlist.dat_
- Code: [github.com/palewire/atcf-data-parser](https://github.com/palewire/atcf-data-parser)
- Issues: [github.com/palewire/atcf-data-parser/issues](https://github.com/palewire/atcf-data-parser/issues)
- Packaging: [pypi.org/project/atcf-data-parser](https://pypi.org/project/atcf-data-parser)
