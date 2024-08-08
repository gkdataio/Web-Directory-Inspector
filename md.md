Checking directories for domain: http://example.com Using file:
directories.txt Number of threads: 10

Testing 79 directories.

200 OK: http://example.com/admin - Size: 1234 bytes Status 404:
http://example.com/login - Size: 567 bytes Status 301:
http://example.com/dashboard - Size: 890 bytes ...

Finished checking directories.

+--------------+-------+ \| Status \| Count \| +--------------+-------+
\| 200 OK \| 5 \| \| 300 Redirect \| 3 \| \| 400 Error \| 2 \| \| Other
\| 0 \| +--------------+-------+

200 OK URLs with Content Size:
+------------------------------------------+---------------+ \| URL \|
Size (bytes) \|
+------------------------------------------+---------------+ \|
http://example.com/admin \| 1234 \| \| http://example.com/another-page
\| 5678 \| \| http://example.com/some-other-page \| 2345 \| ...
+------------------------------------------+---------------+
