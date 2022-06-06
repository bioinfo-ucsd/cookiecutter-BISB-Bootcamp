from cookiecutter.utils import simple_filter
from dateutil.parser import parse
import datetime

@simple_filter
def strftime(date, fmt='%B %d, %Y', add_days = 0):
    date = parse(date) + datetime.timedelta(days=add_days)
    native = date.replace(tzinfo=None)
    return native.strftime(fmt) 