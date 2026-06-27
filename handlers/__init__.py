from .ping import register_ping
from .start import register_start
from .log import register_logs
from .run import register_run
def register_handlers(bot):
    register_ping(bot)
    register_start(bot)
    register_logs(bot)
    register_run(bot)