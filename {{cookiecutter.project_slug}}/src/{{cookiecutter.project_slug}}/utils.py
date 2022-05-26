import re
from datetime import datetime


def step_in_time(delta_list=None):
    if not delta_list:
        return [(datetime.utcnow(), 0)]
    i = len(delta_list) - 1
    ts = datetime.utcnow()
    d = ts - delta_list[i][0]
    delta_list.append((ts, d))

    """
    logger.info("[TIME] (query, flatten, csv, total) {0:12.3f} {1:12.3f} {2:12.3f} - {4: 12.3f}".report_format(
        (ts_deltas[1][1].total_seconds()),
        (ts_deltas[2][1].total_seconds()),
        (ts_deltas[3][1].total_seconds()),
        (datetime.utcnow() - ts_deltas[0][0]).total_seconds(),
    ))
    """
