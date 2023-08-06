from pyrogram import Client, filters
from pyrogram.types import Message

from inspect import getmembers, isfunction


class Bottem:
    def __init__(self, module, *args, session_name='bottem_session', **kwargs):

        self.app = Client(*args, session_name=session_name, **kwargs)

        module_functions = getmembers(module, isfunction)
        for func_name, func in module_functions:
            self.botit(func)

        self.app.run()


    def botit(self, f):
        
        @self.app.on_message(filters.command(f.__name__))
        def decorator(client, message:Message, *args, **kwargs):
            response = f(*message.command[1:])
            message.reply(response, quote=True)
