#!/usr/bin/env python3
"""Builds MIB2026-exam-dates.ics from the confirmed dates in index.html.
Run after every date change:  python3 build_ics.py
Rows marked tbc are left out, the same as in the download on the page."""
import re, datetime, pathlib

here = pathlib.Path(__file__).parent
html = (here / 'index.html').read_text(encoding='utf-8')


def esc(t):
    return t.replace('\\', '\\\\').replace(';', '\\;').replace(',', '\\,')


def fold(line):
    out = []
    while len(line) > 73:
        out.append(line[:73])
        line = ' ' + line[73:]
    out.append(line)
    return '\r\n'.join(out)


def slug(course, typ):
    return re.sub(r'[^a-z0-9]+', '-', (course + ' ' + typ).lower()).strip('-')


events = []
for m in re.finditer(r'<li data-date="(\d{4}-\d{2}-\d{2})">(.*?)</li>', html, re.S):
    date, body = m.groups()
    if re.search(r'class="tag">[^<]*tbc', body, re.I):
        continue
    course = re.search(r'<span class="name">(.*?)</span>', body).group(1).strip()
    typ = re.search(r'<div class="type">(.*?)</div>', body, re.S).group(1)
    typ = re.sub(r'<span.*?</span>', '', typ, flags=re.S).strip()
    events.append((date, course, typ))

now = datetime.datetime.now(datetime.timezone.utc)
stamp = now.strftime('%Y%m%dT%H%M%SZ')
seq = str(int(now.timestamp() // 60))
lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//MIB2026 exam dates//EN', 'CALSCALE:GREGORIAN',
         'METHOD:PUBLISH', 'X-WR-CALNAME:MIB2026 exam dates',
         'REFRESH-INTERVAL;VALUE=DURATION:PT6H', 'X-PUBLISHED-TTL:PT6H']
for date, course, typ in events:
    d = datetime.date.fromisoformat(date)
    end = d + datetime.timedelta(days=1)
    summary = course + ': ' + typ
    lines += ['BEGIN:VEVENT', 'UID:' + slug(course, typ) + '@mib2026-exam-dates', 'DTSTAMP:' + stamp,
              'LAST-MODIFIED:' + stamp, 'SEQUENCE:' + seq,
              'DTSTART;VALUE=DATE:' + d.strftime('%Y%m%d'), 'DTEND;VALUE=DATE:' + end.strftime('%Y%m%d'),
              'SUMMARY:' + esc(summary)]
    for trig in ('-PT63H', '-PT15H'):
        lines += ['BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:' + esc(summary), 'TRIGGER:' + trig, 'END:VALARM']
    lines.append('END:VEVENT')
lines.append('END:VCALENDAR')

with open(here / 'MIB2026-exam-dates.ics', 'w', encoding='utf-8', newline='') as f:
    f.write('\r\n'.join(fold(l) for l in lines) + '\r\n')
print(len(events), 'events written')
