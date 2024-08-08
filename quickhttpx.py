import argparse
import httpx
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

# Global counters and storage for 200 OK URLs
status_counts = {
    "200 OK": 0,
    "300 Redirect": 0,
    "400 Error": 0,
    "Other": 0
}
ok_urls = []

def fetch_url(client, url):
    try:
        response = client.get(url)
        content_length = len(response.content)
        if response.status_code == 200:
            status_counts["200 OK"] += 1
            ok_urls.append((url, content_length))
            return f"{Fore.GREEN}200 OK: {Fore.WHITE}{url} - Size: {content_length} bytes"
        elif 300 <= response.status_code < 400:
            status_counts["300 Redirect"] += 1
            return f"{Fore.YELLOW}Status {response.status_code}: {Fore.WHITE}{url} - Size: {content_length} bytes"
        elif 400 <= response.status_code < 500:
            status_counts["400 Error"] += 1
            return f"{Fore.RED}Status {response.status_code}: {Fore.WHITE}{url} - Size: {content_length} bytes"
        else:
            status_counts["Other"] += 1
            return f"{Fore.RED}Status {response.status_code}: {Fore.WHITE}{url} - Size: {content_length} bytes"
    except httpx.RequestError as e:
        status_counts["Other"] += 1
        return f"{Fore.RED}Request error for {url}: {e}"

def format_domain(domain):
    if not domain.startswith(('http://', 'https://')):
        return f"https://{domain}"
    return domain

def check_directories(domain, directory_file, max_threads):
    # Format the domain to ensure it starts with https:// or http://
    domain = format_domain(domain)
    
    # Strip any trailing slashes from the domain
    domain = domain.rstrip('/')

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Checking directories for domain:{Fore.YELLOW} {domain}")
    print(f"{Fore.CYAN}{Style.BRIGHT}Using file:{Fore.YELLOW} {directory_file}")
    print(f"{Fore.CYAN}{Style.BRIGHT}Number of threads:{Fore.YELLOW} {max_threads}\n")

    # Check if the file exists
    if not os.path.isfile(directory_file):
        print(f"{Fore.RED}Error: The file '{directory_file}' was not found.")
        return

    # Read directories from the file
    try:
        with open(directory_file, 'r') as file:
            directories = file.readlines()
    except Exception as e:
        print(f"{Fore.RED}Error reading the file '{directory_file}': {e}")
        return

    # Remove any whitespace characters like `\n` at the end of each line and strip leading/trailing slashes
    directories = [dir.strip().lstrip('/') for dir in directories if dir.strip()]
    
    total_directories = len(directories)
    if total_directories == 0:
        print(f"{Fore.RED}No directories found in the file.")
        return
    
    print(f"{Fore.GREEN}{Style.BRIGHT}Testing {total_directories} directories.\n")

    # Create a client
    client = httpx.Client()

    # Process directories with threading
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(fetch_url, client, f"{domain}/{directory}"): directory for directory in directories}
        
        current_threads = 0
        table_data = []

        for future in as_completed(futures):
            current_threads += 1
            url_result = future.result()
            table_data.append([current_threads, futures[future], url_result])
            print(url_result)

    # Close the client
    client.close()
    print(f"\n{Fore.CYAN}Finished checking directories.")

    # Display final summary
    summary_table = [
        ["200 OK", status_counts["200 OK"]],
        ["300 Redirect", status_counts["300 Redirect"]],
        ["400 Error", status_counts["400 Error"]],
        ["Other", status_counts["Other"]]
    ]
    print(tabulate(summary_table, headers=[f"{Fore.GREEN}Status", f"{Fore.GREEN}Count"], tablefmt="grid"))

    # Display 200 OK URLs with content size
    if ok_urls:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}200 OK URLs with Content Size:")
        ok_table = [[url, size] for url, size in ok_urls]
        print(tabulate(ok_table, headers=[f"{Fore.GREEN}URL", f"{Fore.GREEN}Size (bytes)"], tablefmt="grid"))

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Check directories for given domain(s).')
    parser.add_argument('-d', '--domain', help='The domain to check (e.g., http://example.com)')
    parser.add_argument('-D', '--domains-list', help='Path to a file containing a list of domains')
    parser.add_argument('-l', '--list', required=True, help='Path to the file containing the list of directories')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of concurrent threads (default: 10)')

    # Parse arguments
    args = parser.parse_args()

    # Validate input: either a domain or a list of domains must be provided
    if not args.domain and not args.domains_list:
        print(f"{Fore.RED}Error: You must provide either a single domain with -d or a domains list with -D.")
        exit(1)

    # If a domains list is provided, check all domains in the list
    domains = []
    if args.domains_list:
        try:
            with open(args.domains_list, 'r') as file:
                domains = [line.strip() for line in file.readlines() if line.strip()]
        except Exception as e:
            print(f"{Fore.RED}Error reading the domains list file '{args.domains_list}': {e}")
            exit(1)
    else:
        domains.append(args.domain)

    # Run the check for each domain
    for domain in domains:
        check_directories(domain, args.list, args.threads)
