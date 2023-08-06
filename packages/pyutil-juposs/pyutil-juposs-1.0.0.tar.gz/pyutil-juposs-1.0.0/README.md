# How to install?

python3 -m pip install --upgrade pip

wget https://github.com/juposs/pyutil/raw/v1.0/dist/pyutil-1.0-py3-none-any.whl

pip3 install 

# Defaults
Custom defaults can be stored in $HOME/pyutil_settings.json

See https://github.com/juposs/pyutil/blob/v1.0/pyutil_settings.json_sample

Everything that is not defined in $HOME/pyutil_settings.json will be read from

"$HOME/.local/lib/python3.X/site-packages/pyutil/defaults.py"

# Usage:

    ldap:
        from pyutil import Ldap

        Modify defaults and use the minumum parameters:
        instance = Ldap("binduser@example.org", "strongpass", "john.doe@example.org")

        or give all parameters:
        instance = Ldap("binduser@example.org", "strongpass", "john.doe@example.org", "userPrincipalName", "OU=OrgUnit,DC=example,DC=org", "server.example.org")

        then run query with that instance:
        result = instance.query("pwdlastset")
        result2 = instance.query("extensionAttribute12")

        This will search for ldap object where userPrincipalName equals john.doe@example.org and return the value of pwdlastlet to the variable "result" and return whatever is in extensionAttribute12 to variable "result2"

    mail:
        from pyutil import Mail

        Modify defaults and use the minumum parameters:
        instance = Mail()

        or give all parameters:
        email = Mail("no-rely@example.org", "mailserver.example.org", "25", true, "/path/to/myfile.txt")
        email = Mail("no-rely@example.org", "mailserver.example.org", "25", false)

        then send the mail with that instance:
        instance.send(subject, text, receipient1 [, receipient2])

    logging:
        from pyutil import Logger

        Modify defaults and use the minumum parameters:
        logfile1 = Logger()

        or give all parameters:
        logfile1 = Logger("/path/to/logfile", maxBytes=1000, backupCount=10)

        Logfile will rotate after reaching maxBytes, default is '0', never rotate
        If rotation enabled, it will keep 'backupCount' files, default is 10

        then log stuff, for instance:
        log1.info("info")
        log1.warning("Warning")
        log1.error("Error")
        log1.debug("Debug")
