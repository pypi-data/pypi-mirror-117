from addongen.__slashcommand__ import slashcommand
from addongen.__entityquery__ import __entityquery__
from addongen.__componentbinding__ import __componentbinding__
from addongen.__entitybinding__ import __entitybinding__
from addongen.__eventbinding__ import __eventbinding__
from addongen.__systemevent__ import __systemevent__


class registerSystem(__systemevent__, __eventbinding__, __entitybinding__, __componentbinding__, __entityquery__, slashcommand):
    def __init__(self, majorVersion: int, minorVersion: int):
        self.__js__ = server.registerSystem(majorVersion, minorVersion)


# https://bedrock.dev/docs/stable/Scripting#log(Message)
def log(Message: str):
    server.client.log(Message)
