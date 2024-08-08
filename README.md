# Web Directory Inspector

Web Directory Inspector is a powerful and efficient tool designed to check the availability and status of multiple directories on a given domain. It provides detailed information about the HTTP status codes and content sizes of the checked URLs, utilizing multi-threading for faster processing.

## Features

- **Multi-threaded**: Efficiently checks multiple directories concurrently.
- **HTTP Status Codes**: Displays detailed status codes including 200 OK, 300 Redirect, 400 Error, and other statuses.
- **Content Size**: Shows the size of the content for each URL.
- **Summary Tables**: Provides a clean and formatted summary of the results.

## Installation

To install the required dependencies, use:

\`\`\`bash
pip install httpx colorama tabulate
\`\`\`

## Usage

\`\`\`bash
python web_directory_inspector.py -d http://example.com -l directories.txt -t 20
\`\`\`

- \`-d\` or \`--domain\`: The domain to check (e.g., http://example.com)
- \`-l\` or \`--list\`: Path to the file containing the list of directories
- \`-t\` or \`--threads\`: Number of concurrent threads (default: 10)

## Example Output

\`\`\`
Checking directories for domain: http://example.com
Using file: directories.txt
Number of threads: 10

Testing 79 directories.

200 OK: http://example.com/admin - Size: 1234 bytes
Status 404: http://example.com/login - Size: 567 bytes
Status 301: http://example.com/dashboard - Size: 890 bytes
...

Finished checking directories.

+--------------+-------+
| Status       | Count |
+--------------+-------+
| 200 OK       | 5     |
| 300 Redirect | 3     |
| 400 Error    | 2     |
| Other        | 0     |
+--------------+-------+

200 OK URLs with Content Size:
+------------------------------------------+---------------+
| URL                                      | Size (bytes)  |
+------------------------------------------+---------------+
| http://example.com/admin                 | 1234          |
| http://example.com/another-page          | 5678          |
| http://example.com/some-other-page       | 2345          |
...
+------------------------------------------+---------------+
\`\`\`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Your Name](https://www.linkedin.com/in/yourprofile)
