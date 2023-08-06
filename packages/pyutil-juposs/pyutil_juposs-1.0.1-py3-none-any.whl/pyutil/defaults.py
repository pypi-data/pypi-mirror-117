ldap = {
    "server": "example.org",
    "search_attribute": "userPrincipalName",
    "dn": "OU=OrgUnit,DC=example,DC=org",
    "return_attributes": ["lastlogon"],
}

mail = {
    "server": "mailserver.example.org",
    "port": 25,
    "sendfile": "False",
    "filepath": "None",
    "sender": "no-reply@example.org",
    "password": "None",
}

logger = {
    "logfile_path": "pyutil.log",
    "maxBytes": 0,
    "backupCount": 10,
}
