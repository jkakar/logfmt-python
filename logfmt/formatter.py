import numbers
import logging


def format_line(extra):
    outarr = []
    for k, v in extra.items():
        if v is None:
            outarr.append("%s=" % k)
            continue

        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, numbers.Number):
            pass
        else:
            if isinstance(v, (dict, object)):
                v = str(v)
            v = '"%s"' % v.replace('"', '\\"')
        outarr.append("%s=%s" % (k, v))
    return " ".join(outarr)


class LogfmtFormatter(logging.Formatter):
    def format(self, record):
        return ' '.join([
            'at=%' % record.levelname,
            'msg="%"' % record.getMessage().replace('"', '\\"'),
            'process=%' % record.processName,
            format_line(getattr(record, 'context', {})),
        ])
