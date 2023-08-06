#!/usr/bin/python3
#-*- coding: utf-8 -*-
from ldap3 import Server, Connection
import sys, os, json

# Import default vars
from pyutil import defaults
defaults = defaults.ldap

home = os.path.expanduser("~")
user_settings_file = os.path.join(home, "pyutil_settings.json")

defaults = dict(defaults)

if os.path.exists(user_settings_file):
    with open(user_settings_file) as file:
        user_defaults = json.load(file)["ldap"]
    defaults.update(user_defaults)

class Ldap:
    def __init__(self, user, password, server=None):
        """ Sort out the given variables and if neccessary fill in default variables

        Usage:
        Modify defaults in the class and use the minumum parameters:
        from pyutil import Ldap
        instance = Ldap(username, password)

        or give all parameters:
        instance = Ldap(username, password, server)
        """
        self.user = user
        self.password = password

        self.server = server if server is not None else defaults["server"]

        server = Server(self.server, use_ssl=True)
        self.__conn__ = Connection(server, self.user, self.password, auto_bind=True)

    def query(self, search_value, search_attribute=None, return_attributes=None, dn=None,):
        """Do the ldap query with the given variables

        Usage:
        result = instance.query(searchvalue, search_attribute return_attributes, dn)

        "search_value" is  the value to match to the ldap object, usually "firstname.lastname@example.org"
        "search_attribute" is the ldap attribute to match the "match_value" to, defaults to "userPrincipalName"
        "return_attributes" is a list of attributes you want to retrieve, for instance ["pwdlastset", "lastlogon"]
        "dn" is the tree you want to start the search in, usually similar to "OU=OrgUnit,DC=example,DC=org"
        """
        self.dn = dn if dn is not None else defaults["dn"]
        self.return_attributes = return_attributes if return_attributes is not None else defaults["return_attributes"]
        self.search_attribute = search_attribute if search_attribute is not None else defaults["search_attribute"]


        self.__conn__.search(self.dn,'(&('+search_attribute+'='+search_value+'))', attributes=self.return_attributes)
        response = json.loads(self.__conn__.response_to_json())
        #status, result, response, _ = conn.search(dn, '(objectClass=inetOrgPerson)', search_scope=SUBTREE)  # usually you don't need the original request (4th element of the returned tuple)
        return response["entries"][0]["attributes"]