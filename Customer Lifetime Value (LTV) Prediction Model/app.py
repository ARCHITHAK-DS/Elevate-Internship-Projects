import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import joblib
import os

# ── Page config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer LTV Predictor",
    page_icon="💎",
    layout="centered",
)

# ── Glassmorphism CSS ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
    font-family: 'Inter', sans-serif !important;
    min-height: 100vh;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }

/* Main content area */
[data-testid="stMain"] > div {
    background: transparent !important;
}
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    max-width: 780px !important;
}

/* Glass card panels */
.glass-card {
    background: rgba(255,255,255,0.07);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 1.75rem 2rem;
    margin-bottom: 1.25rem;
}

/* Text colors */
h1, h2, h3, p, label, .stMarkdown, div {
    color: rgba(255,255,255,0.9) !important;
}

/* Section labels */
.section-label {
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.35) !important;
    margin-bottom: 0.5rem;
}

/* Sliders */
[data-testid="stSlider"] > div > div > div {
    background: rgba(255,255,255,0.12) !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stThumbValue"] {
    color: #c4b8ff !important;
    background: transparent !important;
}
.stSlider > label {
    color: rgba(255,255,255,0.55) !important;
    font-size: 0.8rem !important;
    font-weight: 400 !important;
}

/* Predict button */
.stButton > button {
    background: linear-gradient(135deg, #7b61ff 0%, #00d4ff 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 2rem !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    font-family: 'Inter', sans-serif !important;
    width: 100% !important;
    letter-spacing: 0.3px;
    cursor: pointer;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* Metric cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
    padding: 1rem 1.1rem !important;
}
[data-testid="stMetricLabel"] > div {
    color: rgba(255,255,255,0.4) !important;
    font-size: 0.72rem !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}
[data-testid="stMetricValue"] > div {
    color: #ffffff !important;
    font-size: 1.5rem !important;
    font-weight: 600 !important;
}

/* Info / success / warning boxes */
[data-testid="stInfo"], [data-testid="stSuccess"], [data-testid="stWarning"] {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
    color: rgba(255,255,255,0.85) !important;
}

/* Divider */
hr { border-color: rgba(255,255,255,0.1) !important; }

/* Matplotlib chart background */
.stPlotlyChart, .stImage { border-radius: 14px; overflow: hidden; }

/* Sidebar (if any) */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.05) !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.1) !important;
}
</style>
""", unsafe_allow_html=True)


# ── Helper: load or mock model ────────────────────────────────────
def load_model():
    if os.path.exists("ltv_model.pkl"):
        return joblib.load("ltv_model.pkl")
    return None


def rule_based_ltv(recency, frequency, monetary, tenure, avg_qty, uniq_prod):
    """
    Fallback heuristic when no trained model file is found.
    Replace with model.predict([[...]]) once you have ltv_model.pkl.
    """
    aov            = monetary / max(frequency, 1)
    recency_score  = max(0, 1 - recency / 365)
    freq_score     = min(frequency / 50, 1)
    monetary_score = min(monetary / 5000, 1)
    tenure_score   = min(tenure / 730, 1)
    product_score  = min(uniq_prod / 50, 1)

    ltv = (
        monetary  * 0.40 * (recency_score * 1.5 + 0.5) +
        frequency * aov  * 0.20 * freq_score +
        tenure    * 0.80 * tenure_score +
        uniq_prod * 12   * product_score +
        avg_qty   * 8
    )
    return round(max(ltv, 0), 2)


def get_segment(ltv):
    if ltv >= 1200:
        return "⭐ VIP",    "#ffd54f", "rgba(255,193,7,0.25)",  "rgba(255,193,7,0.5)"
    elif ltv >= 600:
        return "High",      "#c4b8ff", "rgba(123,97,255,0.2)",  "rgba(123,97,255,0.45)"
    elif ltv >= 200:
        return "Medium",    "#80eaff", "rgba(0,212,255,0.15)",  "rgba(0,212,255,0.35)"
    else:
        return "Low",       "#aaaaaa", "rgba(255,255,255,0.07)","rgba(255,255,255,0.18)"


def get_action(segment):
    actions = {
        "⭐ VIP": (
            "Invest in exclusive loyalty rewards",
            "Top-tier customer. Offer early product access, a dedicated account manager, "
            "and personalised loyalty perks. Highest ROI per £ spent on retention."
        ),
        "High": (
            "Upsell and cross-sell premium products",
            "Strong purchase signals upgrade potential. Target with premium bundles, "
            "subscription offers, and recommendations based on their product variety."
        ),
        "Medium": (
            "Re-engagement campaign with personalised offers",
            "Decent frequency but room to grow. Run email campaigns with personalised "
            "discounts and product suggestions to push toward the High segment."
        ),
        "Low": (
            "Low-cost retention or graceful exit",
            "Evaluate whether retention cost exceeds expected returns. Use low-cost "
            "push notifications or a win-back coupon only. Remove from paid campaigns."
        ),
    }
    return actions.get(segment, ("—", "—"))


# ── RFM bar chart ─────────────────────────────────────────────────
def rfm_chart(r_score, f_score, m_score):
    fig, ax = plt.subplots(figsize=(6, 1.8))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    labels  = ["Recency", "Frequency", "Monetary"]
    values  = [r_score, f_score, m_score]
    colors  = ["#ff61d8", "#7b61ff", "#00d4ff"]
    y_pos   = [0.65, 0.35, 0.05]

    for i, (lbl, val, col, yp) in enumerate(zip(labels, values, colors, y_pos)):
        # Track
        ax.barh(yp, 1,   height=0.18, color=(1, 1, 1, 0.08), left=0,
                align="center", zorder=1)
        # Fill
        ax.barh(yp, val, height=0.18, color=col, left=0,
                align="center", zorder=2)
        ax.text(-0.02, yp, lbl, va="center", ha="right",
                fontsize=7.5, color=(1, 1, 1, 0.5),
                fontfamily="monospace")
        ax.text(1.02, yp, f"{int(val*100)}",
                va="center", ha="left",
                fontsize=7.5, color=col)

    ax.set_xlim(-0.18, 1.12)
    ax.set_ylim(-0.1, 0.85)
    ax.axis("off")
    plt.tight_layout(pad=0.2)
    return fig


# ── LTV gauge chart ───────────────────────────────────────────────
def ltv_gauge(ltv, max_ltv=3000):
    fig, ax = plt.subplots(figsize=(5, 2.6), subplot_kw=dict(aspect="equal"))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    theta_start, theta_end = 180, 0
    pct   = min(ltv / max_ltv, 1.0)
    theta = theta_start - pct * 180

    # Background arc
    arc_bg = mpatches.Wedge((0.5, 0.2), 0.38, 0, 180,
                             width=0.10, color=(1, 1, 1, 0.08))
    ax.add_patch(arc_bg)

    # Filled arc — gradient via segments
    n_seg = 60
    for i in range(n_seg):
        t0 = 180 - (i / n_seg) * 180 * pct
        t1 = 180 - ((i+1) / n_seg) * 180 * pct
        r  = i / n_seg
        col = (
            0.48 + 0.52 * r,          # R  purple→cyan
            0.38 * r,                  # G
            1.0  - 0.37 * r,          # B
        )
        seg = mpatches.Wedge((0.5, 0.2), 0.38, t1, t0,
                              width=0.10, color=col, zorder=3)
        ax.add_patch(seg)

    ax.text(0.5, 0.26, f"£{ltv:,.0f}",
            ha="center", va="center",
            fontsize=19, fontweight="600",
            color="#ffffff", transform=ax.transAxes)
    ax.text(0.5, 0.10, "Predicted future LTV",
            ha="center", va="center",
            fontsize=7, color=(1, 1, 1, 0.4),
            transform=ax.transAxes)

    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.0,  0.70)
    ax.axis("off")
    plt.tight_layout(pad=0.1)
    return fig


# ══════════════════════════════════════════════════════════════════
#  APP LAYOUT
# ══════════════════════════════════════════════════════════════════

# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-bottom:2rem;">
    <div style="display:inline-block; background:rgba(123,97,255,0.25);
         border:1px solid rgba(123,97,255,0.45); color:#c4b8ff;
         font-size:0.72rem; padding:4px 16px; border-radius:20px;
         letter-spacing:0.8px; margin-bottom:0.9rem;">
        XGBoost · RFM Model
    </div>
    <h1 style="font-size:2rem; font-weight:600; color:#fff;
               letter-spacing:-0.5px; margin:0 0 0.4rem;">
        Customer LTV Predictor
    </h1>
    <p style="color:rgba(255,255,255,0.45); font-size:0.88rem; font-weight:300;">
        Enter customer behaviour metrics to predict future lifetime value
    </p>
</div>
""", unsafe_allow_html=True)

# ── Input panel ───────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">RFM inputs</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    recency   = st.slider("Recency — days since last purchase", 1, 365, 30)
    monetary  = st.slider("Total past spend (£)", 10, 10000, 600, step=10)
    avg_qty   = st.slider("Avg quantity per order", 1, 30, 4)
with col2:
    frequency = st.slider("Frequency — number of orders", 1, 100, 8)
    tenure    = st.slider("Tenure — days as a customer", 1, 730, 180)
    uniq_prod = st.slider("Unique products purchased", 1, 100, 12)

aov = monetary / max(frequency, 1)
st.markdown(f"""
<div style="background:rgba(0,212,255,0.07); border:1px solid rgba(0,212,255,0.18);
            border-radius:10px; padding:0.65rem 1rem; margin-top:0.5rem;">
    <span style="font-size:0.72rem; color:rgba(255,255,255,0.4);">Computed AOV</span>
    <span style="font-size:0.95rem; font-weight:500; color:#80eaff;
                 margin-left:0.6rem;">£{aov:.2f}</span>
    <span style="font-size:0.7rem; color:rgba(255,255,255,0.3);
                 margin-left:0.4rem;">(Total spend ÷ Frequency)</span>
</div>
""", unsafe_allow_html=True)

predict_clicked = st.button("Predict LTV →")
st.markdown('</div>', unsafe_allow_html=True)


# ── Result panel ──────────────────────────────────────────────────
if predict_clicked:

    model = load_model()

    if model is not None:
        features = np.array([[recency, frequency, monetary, aov,
                               avg_qty, uniq_prod, tenure]])
        ltv = float(model.predict(features)[0])
        ltv = max(round(ltv, 2), 0)
        source_note = "Prediction from your trained XGBoost model."
    else:
        ltv = rule_based_ltv(recency, frequency, monetary,
                             tenure, avg_qty, uniq_prod)
        source_note = (
            "**No `ltv_model.pkl` found** — using heuristic estimate. "
            "Run your notebook first to train and save the model, "
            "then place `ltv_model.pkl` in the same folder as `app.py`."
        )

    seg_label, seg_color, seg_bg, seg_border = get_segment(ltv)
    action_title, action_body = get_action(seg_label)

    # Scores for visual bars
    r_score = max(0, 1 - recency / 365)
    f_score = min(frequency / 50, 1)
    m_score = min(monetary / 5000, 1)

    # ── Result header
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Prediction result</div>',
                unsafe_allow_html=True)

    # Gauge chart
    gauge_fig = ltv_gauge(ltv)
    st.pyplot(gauge_fig, use_container_width=True)
    plt.close(gauge_fig)

    # Segment badge
    st.markdown(f"""
    <div style="text-align:center; margin:-0.5rem 0 1.25rem;">
        <span style="display:inline-block;
                     background:{seg_bg};
                     border:1px solid {seg_border};
                     color:{seg_color};
                     font-size:0.82rem; font-weight:500;
                     padding:6px 22px; border-radius:20px;">
            {seg_label}
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Metric cards
    m1, m2, m3 = st.columns(3)
    conf_map = {"⭐ VIP": "High", "High": "High", "Medium": "Medium", "Low": "Low"}
    pct_map  = {"⭐ VIP": "Top 10%", "High": "Top 25%",
                "Medium": "Top 50%", "Low": "Bottom 50%"}
    m1.metric("Confidence tier",  conf_map.get(seg_label, "—"))
    m2.metric("Avg order value",  f"£{aov:.0f}")
    m3.metric("LTV percentile",   pct_map.get(seg_label, "—"))

    st.markdown('</div>', unsafe_allow_html=True)

    # ── RFM breakdown
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">RFM score breakdown</div>',
                unsafe_allow_html=True)
    rfm_fig = rfm_chart(r_score, f_score, m_score)
    st.pyplot(rfm_fig, use_container_width=True)
    plt.close(rfm_fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Marketing action
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Marketing action</div>',
                unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.04);
                border:1px solid rgba(255,255,255,0.1);
                border-radius:12px; padding:1rem 1.25rem;">
        <div style="font-size:0.85rem; font-weight:500;
                    color:rgba(255,255,255,0.8); margin-bottom:0.4rem;">
            {action_title}
        </div>
        <div style="font-size:0.78rem; color:rgba(255,255,255,0.45);
                    line-height:1.6;">
            {action_body}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Model source note
    if model is None:
        st.markdown(f"""
        <div style="background:rgba(255,193,7,0.08);
                    border:1px solid rgba(255,193,7,0.25);
                    border-radius:10px; padding:0.75rem 1rem;
                    font-size:0.75rem; color:rgba(255,255,255,0.5);">
            ℹ️  {source_note}
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem;
            font-size:0.7rem; color:rgba(255,255,255,0.2);">
    Customer LTV Predictor · XGBoost + RFM · Built with Streamlit
</div>
""", unsafe_allow_html=True)
