import requests
import sys


NETBOX_URL = "http://localhost:8000"
API_TOKEN = "1234567890abcdef1234567890abcdef12345678" 


def get_sites_by_status(status):
    """
    Query Netbox API for sites with a specific status.

    Args:
        status (str): Site status to filter ('planned' or 'active').

    Returns:
        list: List of site dictionaries.
    """
    if not status:
        raise ValueError("You must specify a status ('active' or 'planned')")
    
    url = f"{NETBOX_URL}/api/dcim/sites/"
    headers = {"Authorization": f"Token {API_TOKEN}"}
    params = {"status": status}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"[ERROR] invalid response: {e}")
        sys.exit(1)
           
def main():
    if len(sys.argv) != 2:
        print("Usage: python query_sites_api.py <status>")
        sys.exit(1)

    status = sys.argv[1]
    try:
        sites = get_sites_by_status(status)
    except ValueError as ve:
        print(f"[ERROR] {ve}")
        sys.exit(1)

    if not sites:
        print(f"No sites found with status '{status}'")
        return

    print(f"Sites with status '{status}':")
    for site in sites:
        print(f"# {site['id']}: {site['name']} - {site['status']}")


if __name__ == "__main__":
    main()
