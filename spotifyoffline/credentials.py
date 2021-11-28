from argparse import ArgumentParser
from yaml import safe_load

def getCredentialsFilename() -> str:
    parser = ArgumentParser()
    parser.add_argument("credentials", help = "credentials filename")
    arguments = parser.parse_args()
    return arguments.credentials

def fetchCredentials(credentials: str) -> dict:
    with open(credentials) as credentials:
        credentials = safe_load(credentials)
    return credentials