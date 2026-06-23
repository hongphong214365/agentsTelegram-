from .ping import register_ping
from .start import register_start
def register_handlers(bot):
    register_ping(bot)
    register_start(bot)