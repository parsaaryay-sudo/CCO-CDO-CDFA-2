"""Visual theme: colours, CSS, and small HTML components (dark radar / ATC console look)."""
from __future__ import annotations

# --- palette -----------------------------------------------------------------
BG = "#0b1220"
PANEL = "#101a2e"
LINE = "#1f2d4a"
GRID = "#1b2a47"
GREEN = "#39ff88"      # primary accent (radar green)
AMBER = "#ffb020"      # warnings
CYAN = "#38bdf8"       # secondary data
RED = "#ff4d5e"        # conflicts
TEXT = "#dbe7ff"
MUTED = "#8ea3c7"
AIRCRAFT_COLORS = [GREEN, CYAN, AMBER, "#c084fc", "#f472b6", "#a3e635"]

FONT_STACK = "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
MONO_STACK = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

FOOTER_TEXT = ("This tool is for educational purposes only and must not be used for real ATC "
               "operations or procedure design.")


def H(s: str) -> str:
    """Strip indentation and blank lines so Markdown never treats HTML as a code block."""
    return "\n".join(line.strip() for line in s.strip().splitlines() if line.strip())


_BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
:root{--bg:#0b1220;--panel:#101a2e;--panel2:#0d1626;--line:#1f2d4a;--green:#39ff88;--amber:#ffb020;
--cyan:#38bdf8;--red:#ff4d5e;--text:#dbe7ff;--muted:#8ea3c7;
--sans:Inter,system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
--mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace;}
html,body,.stApp,[class*="css"]{font-family:var(--sans);}
.stApp{background:radial-gradient(1100px 560px at 85% -8%,rgba(57,255,136,.07),transparent 60%),
radial-gradient(900px 500px at -8% 8%,rgba(56,189,248,.06),transparent 55%),var(--bg);color:var(--text);}
header[data-testid="stHeader"]{background:transparent;}
#MainMenu,footer{visibility:hidden;}
.block-container{padding-top:1.6rem;padding-bottom:5.5rem;max-width:1280px;}
h1,h2,h3,h4{font-family:var(--sans);letter-spacing:-.015em;color:var(--text);}
h2{font-weight:700;margin-top:1.6rem;}
h3{font-weight:650;}
p,li,label,.stMarkdown{color:var(--text);}
a{color:var(--cyan);}
hr{border-color:var(--line);}
/* sidebar */
section[data-testid="stSidebar"]{background:#09101d;border-right:1px solid var(--line);}
section[data-testid="stSidebar"] [role="radiogroup"]{gap:.15rem;}
section[data-testid="stSidebar"] [role="radiogroup"] label{padding:.5rem .7rem;border-radius:10px;border:1px solid transparent;transition:background .15s,border-color .15s;}
section[data-testid="stSidebar"] [role="radiogroup"] label:hover{background:rgba(57,255,136,.06);}
section[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked){background:rgba(57,255,136,.12);border-color:rgba(57,255,136,.5);}
.brand{display:flex;align-items:center;gap:.7rem;margin:.2rem 0 1rem;}
.brand .dot{width:14px;height:14px;border-radius:50%;background:var(--green);box-shadow:0 0 14px var(--green);}
.brand b{font-size:1.05rem;letter-spacing:.01em;}
.brand span{display:block;color:var(--muted);font-size:.78rem;font-weight:400;}
/* buttons, inputs */
.stButton>button,.stDownloadButton>button{background:linear-gradient(180deg,#14284a,#0f1d36);color:var(--green);
border:1px solid rgba(57,255,136,.45);border-radius:10px;font-weight:600;transition:box-shadow .15s,border-color .15s;}
.stButton>button:hover,.stDownloadButton>button:hover{border-color:var(--green);box-shadow:0 0 16px rgba(57,255,136,.28);color:#eafff3;}
.stButton>button:focus-visible,.stDownloadButton>button:focus-visible{outline:2px solid var(--cyan);outline-offset:2px;}
input,textarea,[data-baseweb="select"]>div{background-color:#0c1628 !important;color:var(--text) !important;}
[data-testid="stNumberInput"] input{font-family:var(--mono);}
[data-testid="stExpander"]{border:1px solid var(--line);border-radius:14px;background:var(--panel);}
[data-testid="stExpander"] summary{font-weight:600;}
[data-testid="stVerticalBlockBorderWrapper"]{border-color:var(--line);border-radius:16px;}
[data-testid="stDataFrame"]{border:1px solid var(--line);border-radius:12px;}
/* hero */
.hero{display:grid;grid-template-columns:1fr auto;gap:2rem;align-items:center;padding:2rem 2.2rem;border:1px solid var(--line);
border-radius:22px;background:linear-gradient(135deg,rgba(16,26,46,.95),rgba(9,16,29,.95));box-shadow:0 0 60px rgba(57,255,136,.06) inset;}
.hero-kicker{color:var(--green);font-family:var(--mono);font-size:.85rem;margin-bottom:.6rem;}
.hero-title{font-size:clamp(2rem,4.4vw,3.6rem);font-weight:800;line-height:1.05;margin:0 0 .8rem;letter-spacing:-.03em;color:#f2f7ff;}
.hero-sub{color:var(--muted);font-size:1.08rem;max-width:46ch;line-height:1.55;margin:0 0 1.1rem;}
.chip{display:inline-block;margin:0 .4rem .4rem 0;padding:.25rem .7rem;border-radius:999px;border:1px solid var(--line);
background:#0c1628;font-family:var(--mono);font-size:.82rem;color:var(--text);}
.chip.g{border-color:rgba(57,255,136,.55);color:var(--green);} .chip.c{border-color:rgba(56,189,248,.55);color:var(--cyan);}
.chip.a{border-color:rgba(255,176,32,.55);color:var(--amber);}
/* pure-CSS radar sweep */
.radar{position:relative;width:230px;height:230px;border-radius:50%;border:1px solid rgba(57,255,136,.6);overflow:hidden;
background:repeating-radial-gradient(circle at center,transparent 0 37px,rgba(57,255,136,.22) 38px 39px),
linear-gradient(rgba(57,255,136,.2),rgba(57,255,136,.2)) center/1px 100% no-repeat,
linear-gradient(rgba(57,255,136,.2),rgba(57,255,136,.2)) center/100% 1px no-repeat;
box-shadow:0 0 44px rgba(57,255,136,.2),inset 0 0 44px rgba(57,255,136,.1);}
.radar::after{content:"";position:absolute;inset:0;border-radius:50%;
background:conic-gradient(from 0deg,rgba(57,255,136,0) 0deg,rgba(57,255,136,0) 280deg,rgba(57,255,136,.55) 360deg);animation:sweep 6s linear infinite;}
.blip{position:absolute;width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green);opacity:.25;}
.blip.b1{left:62%;top:30%;animation:ping 6s linear infinite;animation-delay:.9s;}
.blip.b2{left:30%;top:64%;animation:ping 6s linear infinite;animation-delay:3.6s;}
.blip.b3{left:70%;top:68%;background:var(--amber);box-shadow:0 0 10px var(--amber);animation:ping 6s linear infinite;animation-delay:5s;}
@keyframes sweep{to{transform:rotate(360deg);}}
@keyframes ping{0%,8%{opacity:1;}60%,100%{opacity:.2;}}
@media (prefers-reduced-motion:reduce){.radar::after,.blip{animation:none !important;}}
/* cards */
.card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.25rem;margin-bottom:.9rem;}
.card h4{margin:.1rem 0 .5rem;font-size:1.05rem;}
.card p,.card li{color:var(--text);line-height:1.55;font-size:.97rem;}
.card ul{padding-left:1.15rem;margin:.3rem 0;}
.card.g{border-left:3px solid var(--green);} .card.c{border-left:3px solid var(--cyan);} .card.a{border-left:3px solid var(--amber);}
.page-title{font-size:clamp(1.8rem,3.2vw,2.7rem);font-weight:800;letter-spacing:-.03em;margin:.2rem 0 .3rem;}
.page-sub{color:var(--muted);max-width:75ch;margin-bottom:1rem;}
.mgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin:.6rem 0 1.1rem;}
.mcard{background:linear-gradient(180deg,#111d34,#0c1627);border:1px solid var(--line);border-radius:16px;padding:.95rem 1.1rem;position:relative;}
.mlabel{color:var(--muted);font-size:.82rem;margin-bottom:.35rem;}
.mvalue{font-family:var(--mono);font-size:1.85rem;font-weight:700;color:#f2f7ff;line-height:1.1;}
.munit{font-family:var(--mono);font-size:.9rem;color:var(--muted);margin-left:.3rem;font-weight:400;}
.mnote{color:var(--muted);font-size:.78rem;margin-top:.4rem;line-height:1.35;}
.badge{display:inline-block;padding:.12rem .55rem;border-radius:999px;font-size:.72rem;font-weight:700;letter-spacing:.04em;margin-top:.5rem;font-family:var(--mono);}
.badge.ok{color:var(--green);border:1px solid rgba(57,255,136,.6);background:rgba(57,255,136,.1);}
.badge.warn{color:var(--amber);border:1px solid rgba(255,176,32,.65);background:rgba(255,176,32,.1);}
.badge.conflict{color:var(--red);border:1px solid rgba(255,77,94,.7);background:rgba(255,77,94,.12);}
.mcard.s-ok{box-shadow:0 0 0 1px rgba(57,255,136,.12),0 0 22px rgba(57,255,136,.06);}
.mcard.s-warn{box-shadow:0 0 0 1px rgba(255,176,32,.22),0 0 22px rgba(255,176,32,.08);}
.mcard.s-conflict{box-shadow:0 0 0 1px rgba(255,77,94,.35),0 0 26px rgba(255,77,94,.14);}
.callout{border-radius:12px;padding:.8rem 1rem;margin:.6rem 0;border:1px solid var(--line);background:#0c1628;line-height:1.5;}
.callout.ok{border-color:rgba(57,255,136,.55);} .callout.bad{border-color:rgba(255,77,94,.6);}
.callout.info{border-color:rgba(56,189,248,.5);} .callout.alert{border-color:rgba(255,77,94,.75);background:rgba(255,77,94,.1);}
.ref{font-family:var(--mono);font-size:.86rem;color:var(--muted);}
.cmp{width:100%;border-collapse:separate;border-spacing:0;border:1px solid var(--line);border-radius:14px;overflow:hidden;font-size:.95rem;}
.cmp th{background:#0f1c35;color:var(--green);text-align:left;padding:.7rem .9rem;border-bottom:1px solid var(--line);}
.cmp td{padding:.65rem .9rem;border-bottom:1px solid var(--line);background:#0c1527;vertical-align:top;}
.cmp tr:last-child td{border-bottom:none;} .cmp td:first-child{color:var(--cyan);font-weight:600;}
.table-scroll{overflow-x:auto;}
/* fixed footer */
.fixed-footer{position:fixed;left:0;right:0;bottom:0;z-index:99;text-align:center;padding:.5rem .8rem;font-size:.78rem;color:var(--muted);
background:rgba(8,13,24,.96);border-top:1px solid var(--line);}
@media (max-width:760px){.hero{grid-template-columns:1fr;padding:1.3rem;} .radar{margin:0 auto;width:170px;height:170px;}
.mvalue{font-size:1.45rem;} .block-container{padding-left:1rem;padding-right:1rem;}}
"""

# Presentation mode: larger type, higher contrast, secondary UI hidden.
_PRESENTATION_CSS = """
.stApp{background:#050a14;}
.stApp p,.stApp li,.stApp label,.stApp .stMarkdown,.card p,.card li{font-size:1.28rem !important;color:#ffffff !important;line-height:1.6 !important;}
.stApp [data-testid="stWidgetLabel"] p{font-size:1.15rem !important;}
.card h4{font-size:1.5rem !important;}
.mvalue{font-size:3rem !important;} .mlabel,.mnote{font-size:1.05rem !important;color:#d6e4ff !important;} .badge{font-size:.95rem !important;}
.page-title{font-size:3.2rem !important;} .page-sub{font-size:1.3rem !important;color:#d6e4ff !important;}
.cmp{font-size:1.2rem !important;} .hero-sub{font-size:1.35rem !important;color:#d6e4ff !important;}
.card,.mcard,[data-testid="stExpander"],.hero{border-color:#4a6aa8 !important;}
[data-testid="stCaptionContainer"],[class*="st-key-sec-"]{display:none !important;}
section[data-testid="stSidebar"] *{font-size:1.1rem;}
"""


def css(presentation: bool) -> str:
    return "<style>" + H(_BASE_CSS + (_PRESENTATION_CSS if presentation else "")) + "</style>"


# --- HTML components -----------------------------------------------------------
_STATUS_LABEL = {"ok": "OK", "warn": "WARNING", "conflict": "CONFLICT"}


def hero() -> str:
    return H("""
    <div class="hero">
      <div>
        <div class="hero-kicker">Interactive ATC classroom lab</div>
        <h1 class="hero-title">CCO, CDO and CDFA</h1>
        <p class="hero-sub">See how continuous climb, continuous descent and continuous final approach
        save fuel, cut noise and remove CFIT risk, and how controllers and CNS/ATM tools make them possible.</p>
        <span class="chip g">CCO</span><span class="chip c">CDO</span><span class="chip a">CDFA</span>
        <span class="chip">CNS</span><span class="chip">ATM / TBO</span>
      </div>
      <div class="radar" aria-hidden="true"><span class="blip b1"></span><span class="blip b2"></span><span class="blip b3"></span></div>
    </div>""")


def metric_card(label: str, value: str, unit: str = "", status: str | None = None, note: str = "") -> str:
    badge = f'<div class="badge {status}">{_STATUS_LABEL[status]}</div>' if status else ""
    unit_html = f'<span class="munit">{unit}</span>' if unit else ""
    note_html = f'<div class="mnote">{note}</div>' if note else ""
    cls = f" s-{status}" if status else ""
    return (f'<div class="mcard{cls}"><div class="mlabel">{label}</div>'
            f'<div class="mvalue">{value}{unit_html}</div>{note_html}{badge}</div>')


def metric_grid(cards: list[str]) -> str:
    return '<div class="mgrid">' + "".join(cards) + "</div>"


def card(title: str, body_html: str, tone: str = "") -> str:
    return f'<div class="card {tone}"><h4>{title}</h4>{body_html}</div>'


def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def callout(text: str, kind: str = "info") -> str:
    return f'<div class="callout {kind}">{text}</div>'


def footer() -> str:
    return f'<div class="fixed-footer">{FOOTER_TEXT}</div>'
