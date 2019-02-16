from functools import wraps


def wrapmsg(verbosity):
    """Decorate function with start/end message acc. to verbosity parameter."""
    def _makeverbose(func):
        """Decorate function with wrapper."""
        @wraps(func)
        def _function_wrapper(*args, **kwargs):
            try:
                if verbosity >= 2:
                    v = 1
                elif verbosity >= 1:
                    v = 0
                else:
                    raise ValueError
                print(func.__name__, _getmsg(func.__name__, "start")[v])
                func(*args, **kwargs)
                print(func.__name__, _getmsg(func.__name__, "end")[v])
            except (TypeError, ValueError):
                func(*args, **kwargs)
        return _function_wrapper
    return _makeverbose


@wrapmsg(1)
def my_func():
    print("my_func doing stuff")

@wrapmsg(2)
def my_func2():
    print("my_func2 doing stuff")


def _getmsg(func, keyword):
    switcher = {
        "my_func": {
            "start": ["start", "beginning now"],
            "end": ["done", "well done"],
            "error": ["oh", "we have a problem"]
            },
        "copytree": {
            "start": [
                "now copying",
                "now copies dirs and subdirs with permissions and timestampsp"
                ],
            "end": ["ended", "ended"],
            },
        "createZip": {
            "start": [
                "now zipping",
                "now zipping dirs and subdirs"
                ],
            "end": ["ended", "ended"],
            },
        }
    message = switcher.get(func, {}).get(keyword, [
        "undef. msg", "longmsg to be defined"
        ])
    return message


# my_func()
# my_func2()
