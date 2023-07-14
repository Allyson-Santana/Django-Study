from logging import (
    # consts
    CRITICAL, ERROR, WARNING, INFO, DEBUG,

    # functions
    critical, error, warning, info, debug,

    # Case you want to use handlers
    FileHandler, StreamHandler, Filter, LogRecord,

    basicConfig
)

class FilterLogRecord(Filter):
    def filter(self, record: LogRecord):
        if 'cartão' in record.msg:
            return False

        return True

file_handler = FileHandler('loggings/loggings.log', 'a')
file_handler.setLevel(WARNING)

# stream_handler = StreamHandler()

file_handler.addFilter(FilterLogRecord())

basicConfig(
    level=DEBUG, # some case not use FileHandler
    # filename='loggings/loggings.log', # some case not use stream_handler
    # filemode='a', # some case not use StreamHandler
    format='%(levelname)s %(asctime)s %(module)s %(message)s',
    handlers=[StreamHandler(), file_handler],
)

try:
    x = int(input("Digite um numero:"))
    print( x / x)
except ZeroDivisionError:
    warning("Tentativa de divisão por zero")


critical("DEU cartão")