import re

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" /' \
      '"Debian APT-HTTP/1.3 (0.9.7.9)" '

remote_addr = re.compile(r'(?P<ip>([^(](\d{1,3})\.){3}(\d{1,3}))')
request_datetime = re.compile(r'(?P<date>(\d{2})/([a-zA-Z]+)/(\d{4}):(\d{2}).{3}(:(\d{2})).{2}\d{4})')
request_type = re.compile(r'(?P<rtype>([A-Z]{3}))+\s')
requested_resource = re.compile(r'(?P<resource>(/[a-z]*/[a-z]*_\d))')
response_code = re.compile(r'(?P<code>(\s(\d{2,})))')
response_size = re.compile(r'(?P<size>(\s\d?\s))')


print(f'{remote_addr.search(raw).group()}, {request_datetime.search(raw).group()}, {request_type.search(raw).group()},'
      f'{requested_resource.search(raw).group()}, {response_code.search(raw).group()},'
      f'{response_size.search(raw).group()}')
