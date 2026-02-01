import streamlit as st
import streamlit.components.v1 as components

# =========================
# Customize these
# =========================
PAGE_TITLE = "Valentine?"
GIF_URL = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDZ2emhpOHl1cGk2aGxuY2N3NGwzNW4xcmVoMG1oOXVjMTB5cDVwayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qFmdpUKAFZ6rMobzzu/giphy.gif"  # <-- put YOUR gif link here
# Tip: use a direct .gif URL or a Giphy "media.giphy.com/media/<id>/giphy.gif" link.

st.set_page_config(page_title=PAGE_TITLE, page_icon="💘", layout="centered")

# Optional: remove Streamlit chrome a bit
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      .block-container {padding-top: 2rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    :root {{
      --pink: #ffd1e8;
      --hotpink: #ff4da6;
      --red: #ff1f4b;
      --card: rgba(255,255,255,0.72);
      --shadow: 0 18px 45px rgba(0,0,0,0.12);
    }}

    html, body {{
      height: 100%;
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
      overflow: hidden;
    }}

    /* Pink background with floating hearts */
    body {{
      background: radial-gradient(circle at 15% 20%, #ffe6f2 0%, var(--pink) 35%, #ffc2dd 70%, #ffb3d6 100%);
      position: relative;
    }}

    /* Heart pattern overlay */
    .hearts {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      opacity: 0.35;
      background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='72' height='72' viewBox='0 0 72 72'%3E%3Cpath fill='%23ff1f4b' fill-opacity='0.35' d='M36 61s-20-12.7-28.3-25.8C.9 23.5 7.8 12 19.8 12c6.1 0 11.2 3.3 14.2 7.6C37 15.3 42.1 12 48.2 12 60.2 12 67.1 23.5 64.3 35.2 56 48.3 36 61 36 61z'/%3E%3C/svg%3E");
      background-size: 96px 96px;
      animation: none;
    }}

    @keyframes drift {{
      from {{ transform: translateY(0px); }}
      to   {{ transform: translateY(-120px); hookup: none; }}
    }}

    .wrap {{
      position: relative;
        min-height: 100vh;
        display: grid;
        place-items: center;
        padding: 1px;
        transform: scale(0.88);
        transform-origin: center;
    }}

    .card {{
      width: min(720px, 94vw);
      min-height: 420px;
      background: var(--card);
      border: 2px solid rgba(255,255,255,0.55);
      border-radius: 28px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(10px);
      padding: 34px 26px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 18px;
      position: relative;
    }}

    h1 {{
      margin: 0;
      font-size: clamp(30px, 4.2vw, 46px);
      color: #b8003a;
      text-align: center;
      letter-spacing: -0.5px;
      text-shadow: 0 2px 0 rgba(255,255,255,0.55);
    }}

    .subtitle {{
      margin-top: -6px;
      font-size: 16px;
      color: rgba(150, 0, 60, 0.75);
      text-align: center;
    }}

    .arena {{
      width: min(520px, 92vw);
      height: 210px;
      position: relative;
      border-radius: 20px;
      background: rgba(255,255,255,0.45);
      border: 2px dashed rgba(255, 77, 166, 0.35);
      overflow: hidden;
      display: grid;
      place-items: center;
    }}

    .btn {{
      border: none;
      border-radius: 999px;
      padding: 14px 26px;
      font-size: 18px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 10px 22px rgba(0,0,0,0.12);
      transition: transform 120ms ease, filter 120ms ease;
      user-select: none;
    }}

    .btn:active {{
      transform: scale(0.97);
    }}

    #yes {{
      background: linear-gradient(180deg, #ff5db1, #ff2f86);
      color: white;
    }}

    #yes:hover {{
      filter: brightness(1.05);
      transform: translateY(-1px);
    }}

    #no {{
      background: white;
      color: #c7003f;
      border: 2px solid rgba(199, 0, 63, 0.25);
      position: absolute;
      left: 56%;
      top: 58%;
      transform: translate(-50%, -50%);
    }}

    #no:hover {{
      filter: brightness(0.98);
    }}

    .yes-container {{
      display: flex;
      gap: 16px;
      align-items: center;
      justify-content: center;
      margin-top: 6px;
    }}

    .result {{
      display: none;
      text-align: center;
      padding-top: 8px;
    }}

    .result h2 {{
      margin: 10px 0 10px;
      font-size: clamp(26px, 3.6vw, 38px);
      color: var(--red);
    }}

    .gif {{
      width: min(420px, 86vw);
      border-radius: 18px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.18);
      border: 3px solid rgba(255,255,255,0.6);
    }}

    .tiny {{
      margin-top: 10px;
      font-size: 13px;
      color: rgba(120,0,50,0.65);
    }}

    /* little corner hearts */
    .corner {{
      position: absolute;
      width: 64px;
      height: 64px;
      opacity: 0.65;
      filter: drop-shadow(0 8px 10px rgba(0,0,0,0.08));
    }}
    .c1 {{ left: 18px; top: 18px; transform: rotate(-12deg); }}
    .c2 {{ right: 18px; top: 18px; transform: rotate(10deg); }}
    .c3 {{ left: 18px; bottom: 18px; transform: rotate(9deg); }}
    .c4 {{ right: 18px; bottom: 18px; transform: rotate(-10deg); }}

    @media (max-width: 420px) {{
      .arena {{ height: 240px; }}
      #no {{ left: 50%; top: 65%; }}
    }}
  </style>
</head>
<body>
  <div class="hearts"></div>
  <div class="wrap">
    <div class="card" id="card">
      <svg class="corner c1" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
        <path fill="#ff1f4b" d="M36 61s-20-12.7-28.3-25.8C.9 23.5 7.8 12 19.8 12c6.1 0 11.2 3.3 14.2 7.6C37 15.3 42.1 12 48.2 12 60.2 12 67.1 23.5 64.3 35.2 56 48.3 36 61 36 61z"/>
      </svg>
      <svg class="corner c2" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
        <path fill="#ff1f4b" d="M36 61s-20-12.7-28.3-25.8C.9 23.5 7.8 12 19.8 12c6.1 0 11.2 3.3 14.2 7.6C37 15.3 42.1 12 48.2 12 60.2 12 67.1 23.5 64.3 35.2 56 48.3 36 61 36 61z"/>
      </svg>
      <svg class="corner c3" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
        <path fill="#ff1f4b" d="M36 61s-20-12.7-28.3-25.8C.9 23.5 7.8 12 19.8 12c6.1 0 11.2 3.3 14.2 7.6C37 15.3 42.1 12 48.2 12 60.2 12 67.1 23.5 64.3 35.2 56 48.3 36 61 36 61z"/>
      </svg>
      <svg class="corner c4" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg">
        <path fill="#ff1f4b" d="M36 61s-20-12.7-28.3-25.8C.9 23.5 7.8 12 19.8 12c6.1 0 11.2 3.3 14.2 7.6C37 15.3 42.1 12 48.2 12 60.2 12 67.1 23.5 64.3 35.2 56 48.3 36 61 36 61z"/>
      </svg>

      <h1>Will you be my valentine? 💘</h1>
      <div class="subtitle">Choose wisely 😇</div>

      <div class="arena" id="arena">
        <div class="yes-container" id="yesContainer">
          <button class="btn" id="yes">Yes</button>
        </div>
        <button class="btn" id="no">No</button>
      </div>

      <div class="result" id="result">
        <h2>yey!! I am so happy!!</h2>
        <img class="gif" src="{GIF_URL}" alt="Valentine gif" />
        <div class="tiny">💗💗💗</div>
      </div>
    </div>
  </div>

  <script>
    const arena = document.getElementById("arena");
    const noBtn = document.getElementById("no");
    const yesBtn = document.getElementById("yes");
    const result = document.getElementById("result");

    // Move "No" button to a random position inside the arena
    function moveNoButton() {{
      const arenaRect = arena.getBoundingClientRect();
      const btnRect = noBtn.getBoundingClientRect();

      // Keep inside with padding
      const pad = 12;
      const maxX = arenaRect.width - btnRect.width - pad;
      const maxY = arenaRect.height - btnRect.height - pad;

      const x = Math.max(pad, Math.random() * maxX);
      const y = Math.max(pad, Math.random() * maxY);

      noBtn.style.left = x + "px";
      noBtn.style.top = y + "px";
      noBtn.style.transform = "translate(0,0)";
    }}

    // Run away on hover AND on attempted click/tap
    noBtn.addEventListener("mouseenter", moveNoButton);
    noBtn.addEventListener("mousedown", (e) => {{ e.preventDefault(); moveNoButton(); }});
    noBtn.addEventListener("touchstart", (e) => {{
      e.preventDefault();
      moveNoButton();
    }}, {{ passive: false }});

    // Also make it occasionally jitter if user gets too close (fun)
    arena.addEventListener("mousemove", (e) => {{
      const btn = noBtn.getBoundingClientRect();
      const dx = (btn.left + btn.width/2) - e.clientX;
      const dy = (btn.top + btn.height/2) - e.clientY;
      const dist = Math.sqrt(dx*dx + dy*dy);
      if (dist < 90) moveNoButton();
    }});

    // Yes shows the happy message + gif
    yesBtn.addEventListener("click", () => {{
      arena.style.display = "none";
      result.style.display = "block";
      // confetti-ish hearts (simple)
      for (let i = 0; i < 16; i++) {{
        const s = document.createElement("div");
        s.textContent = "💖";
        s.style.position = "absolute";
        s.style.left = (10 + Math.random()*80) + "%";
        s.style.top = (10 + Math.random()*70) + "%";
        s.style.fontSize = (18 + Math.random()*26) + "px";
        s.style.opacity = "0.85";
        s.style.transform = "translate(-50%,-50%) rotate(" + (Math.random()*30-15) + "deg)";
        s.style.pointerEvents = "none";
        document.getElementById("card").appendChild(s);
        setTimeout(() => s.remove(), 2200);
      }}
    }});

    // Start with a little initial shuffle so it’s not perfectly centered
    setTimeout(moveNoButton, 350);
  </script>
</body>
</html>
"""

components.html(html, height=650, scrolling=False)