from sys import stdout
from loguru import logger

# 2020/10/25 22:45 | process.py # 23 #
# 2020/10/25 22:45 | plog.py    # 01 #
log_format = [
    '{time: YYYY-MM-DD hh:mm:ss}',
    '{file: <10} => {function: <10} => {line: 03d}',
    '<R>{level: ^13}</R>',
    '{message}'
]
logger.remove()
logger.add(
    sink=stdout,
    level='TRACE',
    format= ' | '.join(log_format)
)