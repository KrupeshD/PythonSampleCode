import datetime
def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))

log('Hi there!')
log('Hi again!', when="2015-07-08 16:41:48.859657")