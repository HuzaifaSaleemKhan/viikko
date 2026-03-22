# Viikkonumero – Finnish Week Number App
# Created by: HSKSwati

import streamlit as st
from datetime import date, timedelta
import isoweek

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Viikkonumero – Finland",
    page_icon="🇫🇮",
    layout="centered",
)

# ── Translations ──────────────────────────────────────────────────────────────
T = {
    "fi": {
        "title": "Viikkonumero",
        "week": "Viikko",
        "today": "Tänään",
        "day_of_year": "Vuodenpäivä",
        "days_left": "Päiviä jäljellä",
        "week_range": "Viikon päivät",
        "holidays_title": "Juhlapyhät 2026",
        "week_short": "vk",
        "day_unit": "päivää",
        "footer": "Suomen juhlapyhät · ISO 8601 viikkonumerointi",
        "months": [
            "tammikuuta","helmikuuta","maaliskuuta","huhtikuuta",
            "toukokuuta","kesäkuuta","heinäkuuta","elokuuta",
            "syyskuuta","lokakuuta","marraskuuta","joulukuuta",
        ],
    },
    "sv": {
        "title": "Veckonummer",
        "week": "Vecka",
        "today": "Idag",
        "day_of_year": "Dag på året",
        "days_left": "Dagar kvar",
        "week_range": "Veckans dagar",
        "holidays_title": "Helgdagar 2026",
        "week_short": "v",
        "day_unit": "dagar",
        "footer": "Finlands helgdagar · ISO 8601 veckonumrering",
        "months": [
            "januari","februari","mars","april","maj","juni",
            "juli","augusti","september","oktober","november","december",
        ],
    },
    "en": {
        "title": "Week Number",
        "week": "Week",
        "today": "Today",
        "day_of_year": "Day of year",
        "days_left": "Days remaining",
        "week_range": "Week dates",
        "holidays_title": "Public holidays 2026",
        "week_short": "wk",
        "day_unit": "days",
        "footer": "Finnish public holidays · ISO 8601 week numbering",
        "months": [
            "January","February","March","April","May","June",
            "July","August","September","October","November","December",
        ],
    },
}

HOLIDAYS_2026 = {
    "fi": [
        (date(2026,1,1),  "Uudenvuodenpäivä"),
        (date(2026,1,6),  "Loppiainen"),
        (date(2026,4,3),  "Pitkäperjantai"),
        (date(2026,4,5),  "Pääsiäispäivä"),
        (date(2026,4,6),  "2. pääsiäispäivä"),
        (date(2026,5,1),  "Vappu"),
        (date(2026,5,14), "Helatorstai"),
        (date(2026,5,24), "Helluntaipäivä"),
        (date(2026,6,19), "Juhannusaatto"),
        (date(2026,6,20), "Juhannuspäivä"),
        (date(2026,11,1), "Pyhäinpäivä"),
        (date(2026,12,6), "Itsenäisyyspäivä"),
        (date(2026,12,24),"Jouluaatto"),
        (date(2026,12,25),"Joulupäivä"),
        (date(2026,12,26),"Tapaninpäivä"),
    ],
    "sv": [
        (date(2026,1,1),  "Nyårsdagen"),
        (date(2026,1,6),  "Trettondag"),
        (date(2026,4,3),  "Långfredag"),
        (date(2026,4,5),  "Påskdagen"),
        (date(2026,4,6),  "Annandag påsk"),
        (date(2026,5,1),  "Valborg"),
        (date(2026,5,14), "Kristi himmelsfärd"),
        (date(2026,5,24), "Pingstdagen"),
        (date(2026,6,19), "Midsommarafton"),
        (date(2026,6,20), "Midsommardagen"),
        (date(2026,11,1), "Alla helgons dag"),
        (date(2026,12,6), "Självständighetsdagen"),
        (date(2026,12,24),"Julafton"),
        (date(2026,12,25),"Juldagen"),
        (date(2026,12,26),"Annandag jul"),
    ],
    "en": [
        (date(2026,1,1),  "New Year's Day"),
        (date(2026,1,6),  "Epiphany"),
        (date(2026,4,3),  "Good Friday"),
        (date(2026,4,5),  "Easter Sunday"),
        (date(2026,4,6),  "Easter Monday"),
        (date(2026,5,1),  "May Day"),
        (date(2026,5,14), "Ascension Day"),
        (date(2026,5,24), "Whit Sunday"),
        (date(2026,6,19), "Midsummer Eve"),
        (date(2026,6,20), "Midsummer Day"),
        (date(2026,11,1), "All Saints' Day"),
        (date(2026,12,6), "Independence Day"),
        (date(2026,12,24),"Christmas Eve"),
        (date(2026,12,25),"Christmas Day"),
        (date(2026,12,26),"Boxing Day"),
    ],
}

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.week-hero {
    text-align: center;
    padding: 2rem 0 1.5rem;
}
.week-hero .lbl {
    font-size: 0.85rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 0.25rem;
}
.week-hero .num {
    font-size: 7rem;
    font-weight: 500;
    line-height: 1;
    color: #003580;
}
.week-hero .range {
    font-size: 1rem;
    color: #888;
    margin-top: 0.4rem;
}

.metric-row {
    display: flex;
    gap: 12px;
    margin: 1.5rem 0;
}
.metric-card {
    flex: 1;
    background: #f7f8fa;
    border-radius: 10px;
    padding: 1rem;
}
.metric-card .m-lbl {
    font-size: 0.75rem;
    color: #999;
    margin-bottom: 4px;
}
.metric-card .m-val {
    font-size: 1.1rem;
    font-weight: 500;
    color: #111;
}

.holiday-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}
.holiday-table th {
    text-align: left;
    font-size: 0.75rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #999;
    padding: 0 0 0.5rem;
    border-bottom: 1px solid #eee;
}
.holiday-table td {
    padding: 0.55rem 0;
    border-bottom: 1px solid #f0f0f0;
    color: #222;
}
.holiday-table td.date-col { color: #888; width: 80px; }
.holiday-table td.week-col { color: #bbb; text-align: right; font-size: 0.8rem; }
.today-row td { font-weight: 500; color: #003580 !important; }

hr.divider { border: none; border-top: 1px solid #eee; margin: 1.5rem 0; }

.footer-txt { font-size: 0.75rem; color: #bbb; text-align: center; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# ── Language selector ─────────────────────────────────────────────────────────
col_l, col_r = st.columns([3, 1])
with col_r:
    lang = st.selectbox("", ["FI", "SV", "EN"], label_visibility="collapsed")

lang_key = lang.lower()
t = T[lang_key]

# ── Calculations ──────────────────────────────────────────────────────────────
today = date.today()
iso_week = today.isocalendar()[1]
iso_year = today.isocalendar()[0]

# Week start (Monday) and end (Sunday)
w = isoweek.Week(iso_year, iso_week)
week_start = w.monday()
week_end   = w.sunday()

months = t["months"]

def fmt_date(d):
    return f"{d.day}. {months[d.month - 1][:3]}"

def fmt_date_long(d):
    return f"{d.day}. {months[d.month - 1]} {d.year}"

day_of_year = today.timetuple().tm_yday
days_left   = (date(today.year, 12, 31) - today).days

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="week-hero">
    <div class="lbl">{t['week']}</div>
    <div class="num">{iso_week}</div>
    <div class="range">{fmt_date(week_start)} – {fmt_date(week_end)}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Metric cards ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="metric-row">
    <div class="metric-card">
        <div class="m-lbl">{t['today']}</div>
        <div class="m-val">{fmt_date_long(today)}</div>
    </div>
    <div class="metric-card">
        <div class="m-lbl">{t['day_of_year']}</div>
        <div class="m-val">{t['day_of_year'].split()[0] if lang_key=='fi' else ''} {day_of_year}.</div>
    </div>
    <div class="metric-card">
        <div class="m-lbl">{t['days_left']}</div>
        <div class="m-val">{days_left} {t['day_unit']}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Holidays table ────────────────────────────────────────────────────────────
st.markdown(f"#### {t['holidays_title']}")

holidays = HOLIDAYS_2026[lang_key]
rows_html = ""
for hdate, hname in holidays:
    week_num = hdate.isocalendar()[1]
    row_class = "today-row" if hdate == today else ""
    rows_html += f"""
    <tr class="{row_class}">
        <td class="date-col">{hdate.day}.{hdate.month}.</td>
        <td>{hname}</td>
        <td class="week-col">{t['week_short']} {week_num}</td>
    </tr>"""

st.markdown(f"""
<table class="holiday-table">
  <thead>
    <tr>
      <th>Pvm</th>
      <th>{t['holidays_title'].split()[0]}</th>
      <th style="text-align:right">{t['week_short'].upper()}</th>
    </tr>
  </thead>
  <tbody>{rows_html}</tbody>
</table>
""", unsafe_allow_html=True)

st.markdown(f'<p class="footer-txt">{t["footer"]}</p>', unsafe_allow_html=True)
