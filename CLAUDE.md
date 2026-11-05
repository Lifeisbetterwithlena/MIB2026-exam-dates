# MIB2026 exam dates

Static GitHub Pages site for a class exam calendar. Read `README.md` for the full workflow.

Rules for every change:

- All dates live in `index.html`. After any change to a date, a tag, a course name or a row, run `python3 build_ics.py` and include `MIB2026-exam-dates.ics` in the commit.
- Rows marked with a tag containing "tbc" are not exported to the calendar. Remove the tag only when the date is confirmed.
- Keep `data-date` in YYYY-MM-DD format on every dated row. Counters use Shanghai time.
- Do not rename courses without telling the user: event IDs are built from course and type, so a rename creates duplicates for people who imported earlier.
- Do not invent dates. If a date is unknown, put the row in "Dates not added yet".
- Language: English, no German gendered forms.
- Never push without the user asking.
