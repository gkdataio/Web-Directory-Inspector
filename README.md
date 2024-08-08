![Web Directory Inspector](https://github.com/gkdataio/Web-Directory-Inspector/blob/259ab697255071abfd1e0619fe6c1b42bde4c119/128127389128381289391.png)

Web Directory Inspector is a simple and efficient tool designed to check the availability and status of multiple directories on a given domain. It provides detailed information about the HTTP status codes and content sizes of the checked URLs, utilizing multi-threading for faster processing.

## Features

- **Multi-threaded**: Efficiently checks multiple directories concurrently.
- **HTTP Status Codes**: Displays detailed status codes including 200 OK, 300 Redirect, 400 Error, and other statuses.
- **Content Size**: Shows the size of the content for each URL.
- **Summary Tables**: Provides a clean and formatted summary of the results.

## Installation

To install the required dependencies, use:

```
pip install httpx colorama tabulate
```

## Usage

```
python3 quickhttpx.py -d http://example.com -l directories.txt -t 20
```

- \`-d\` or \`--domain\`: The domain to check (e.g., http://example.com)
- \`-l\` or \`--list\`: Path to the file containing the list of directories
- \`-t\` or \`--threads\`: Number of concurrent threads (default: 10)

## Example Output

![example](https://github.com/gkdataio/Web-Directory-Inspector/blob/f3707388c028a2e41d2fff1227042df586bdfa6a/c2794bc47e196889dc091886fdad24e5.png)

## Author

- [Garrett Kohlrusch](https://www.linkedin.com/in/kohlrusch)
