# MIB2026 exam dates

Exam and deadline overview for the MIB2026 class at Asia Europe Business School.

Live page: https://lifeisbetterwithlena.github.io/MIB2026-exam-dates/

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole page (text, styles, scripts). All dates live here. |
| `MIB2026-exam-dates.ics` | Calendar file for the "Subscribe" link. Generated, do not edit by hand. |
| `build_ics.py` | Builds the `.ics` file from the dates in `index.html`. |
| `CLAUDE.md` | Short rules for Claude when it edits this project. |

## Updating a date (every time something changes)

1. Edit the row in `index.html`.
2. Run `python3 build_ics.py` in this folder. It rewrites `MIB2026-exam-dates.ics`.
3. Check the page locally (see below).
4. Commit and push, including the `.ics` file:

```
git add index.html MIB2026-exam-dates.ics
git commit -m "Update dates"
git push
```

5. Wait about a minute for GitHub Pages. Hard-refresh the live page (Cmd + Shift + R) to skip the browser cache.

Skipping step 2 means the page and the subscribed calendars show different dates.

## How a date row works

```html
<li data-date="2027-01-12">
  <div class="date">12 Jan<small>Tue</small></div>
  <div class="what">
    <div class="course finance"><i class="dot"></i><span class="name">International Finance</span></div>
    <div class="type">Exam <span class="in"></span></div>
  </div>
</li>
```

- `data-date` (YYYY-MM-DD) drives the "in N days" counter (Shanghai time) and the calendar export.
- The course class sets the color: `supply`, `chinese`, `beginners`, `finance`, `econ`, `strategy`, `ib`. A new course needs a color token in the `:root` blocks, a CSS class, and a legend entry.
- Not confirmed yet: add `<span class="tag">... tbc</span>` to the type. The word **tbc** in the tag keeps the row out of the calendar download and the `.ics` file.
- Once a date is confirmed, remove the tag, then run `python3 build_ics.py`.
- Dates that are not known at all go in the section "Dates not added yet" without `data-date`.
- Rows are grouped by month. Keep them in date order within a month.

## Calendar features

- **Download .ics file:** built in the browser from the page, per course. Event IDs come from course and type, so importing again usually updates events instead of duplicating them.
- **Subscribe:** uses `MIB2026-exam-dates.ics` from this repo. Apple Calendar keeps the reminders, Google Calendar ignores them and refreshes slowly.
- Reminders: 9:00 three days before and 9:00 one day before.
- If a course is renamed, event IDs change, so people who imported earlier may see duplicates once.

## Checking the page locally

- Quickest: `open index.html` in the terminal, then refresh the browser after each save.
- Auto-reload: the "Live Server" extension in VS Code.
- Or: `python3 -m http.server 8000` and open `http://localhost:8000`.

## Publishing

GitHub Pages serves the `main` branch from the root folder (Settings, Pages). Every push to `main` redeploys the site.

## Open items

Keep this list current when dates get confirmed.

- Economic Theory midterm: expected 24 Nov, not confirmed.
- Basic Chinese final: probably 14 Jan.
- Supply Chain report: mid Dec, about 10 days after the presentation.
- Dates not added yet: Chinese for Beginner final, Intermediate and Advanced Chinese, International Business case discussion and personal report.
