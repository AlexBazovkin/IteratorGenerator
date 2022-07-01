import datetime
import os


def logger(path=f'{os.getcwd()}\\logfile.log'):

    def _logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, "a", encoding="utf-8") as logfile:
                logfile.write(f'Execution start time: {datetime.datetime.now()}\n'
                              f'Function name: "{old_function.__name__}"\n'
                              f'Input data: {args, kwargs}\n')
                result = old_function(*args, **kwargs)
                logfile.write(f'Output data: {result}\n\n')
                return result
        return new_function
    return _logger
