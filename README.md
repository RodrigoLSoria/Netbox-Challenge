# Netbox Technical Challenge

## Overview

The project includes:
- A **custom NetBox script** to filter sites by status (`active` or `planned`).
- A **standalone Python script** that queries the NetBox API.
- Automated **linting, testing, and documentation generation**.
- A **Docker-based setup** using the official NetBox image.

---

## Requirements

Ensure the following are installed on your host machine:

- Python 3.10+
- Docker and Docker Compose
- `pytest` and `requests` Python libraries

Install Python dependencies using:
```bash
pip install -r requirements.txt
```
## Setup
Clone this repository and install Docker.

Start NetBox and its dependencies with either:

		docker compose up -d

or use the Makefile shortcut:

		make up
		
Access NetBox UI at http://localhost:8000

Login with:
    Username: netbox
    Password: netbox

## Usage
### Task 1: Import Sites and Upload Custom Script

Import site data:
    Go to Organization → Sites → Import and select fixtures/sites.yaml.

Upload the custom site filter script:
    Navigate to Customization → Scripts or visit http://localhost:8000/extras/scripts/

then click Add and upload scripts/custom_site_filter.py.

To test the script:
    Run it via the UI by selecting either active or planned in the script data section. The output will display matching sites in YAML format.

### Task 2: Query Sites Using the API Script

Open your command line.

Navigate to the scripts folder.

Run the API query script with Python 3:

		python3 query_sites_api.py planned

Example output:

		Sites with status 'planned':
		# 1: Site 1 - {'value': 'planned', 'label': 'Planned'}
		# 2: Site 2 - {'value': 'planned', 'label': 'Planned'}

## Python Scripts Details
### Custom Script: Filter Sites by Status
Located at scripts/custom_site_filter.py.

Not mounted by Docker; upload manually via NetBox UI.

Requires a status filter (active or planned).

Outputs matching sites in YAML.
Logs each processed site in the UI log area as:
```bash
    # <site_id>: <site_name> - <site_status>
```

### API Query Script

Located at scripts/query_sites_api.py.

Queries the NetBox REST API using the API token.

Prints sites filtered by status in the format:
```bash
    	  # <site_id>: <site_name> - <site_status>
```
Run example:
```bash
		      python3 scripts/query_sites_api.py active
```

## Testing & Code Quality

The API script tests (Task 2) can be run locally since they only make HTTP requests to the NetBox API.

Run tests, linting, and generate documentation with:

		make lint
		make test
		make docs


## Makefile Shortcuts

| Command        | Description                     |
| -------------- | -------------------------------|
| `make up`      | Start NetBox containers         |
| `make down`    | Stop NetBox containers          |
| `make restart` | Restart NetBox containers       |
| `make logs`    | Show container logs (follow)   |
| `make ps`      | List running containers         |
| `make test`    | Run pytest tests                |
| `make lint`    | Run flake8 and pylint           |
| `make docs`    | Generate HTML documentation     |



## HTML DOCS

After running make docs, open docs/index.html to explore the auto-generated documentation.







