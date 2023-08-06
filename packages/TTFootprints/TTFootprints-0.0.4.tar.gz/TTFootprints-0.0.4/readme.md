# TTFootprints
TTFootprints is a library for working with ticket data exported from BMC Footprints.

## Installation

`python -m pip install ttfootprints`

OR

`git clone https://gitlab.uvm.edu/whunt1/libfp`

`cd libfp`

`python -m pip install .`

## Usage


### Read tickets from a csv
`from footprints import ticket`

tickets = `ticket.read_csv("/path/to/file")`

### Get ticket information

`first_ticket = tickets[0]`

`desc = first_ticket.data["Description"]`