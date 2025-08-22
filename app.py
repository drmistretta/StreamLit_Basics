# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import date
import time
from pathlib import Path
import base64

def _img_data_uri(path: str) -> str:
    p = Path(path)
    if not p.exists():
        st.warning(f"Image not found: {path} (cwd: {Path.cwd()})")
        return ""  # graceful fallback so your page still loads
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{b64}"


st.set_page_config(page_title="Streamlit for Educators", layout="wide")

st.title("Streamlit for Educators: Teaching Notes & Demos")
st.caption(f"Last updated: {date.today().isoformat()} • Deployed from GitHub.")

# ────────────────────────────────────────────────────────────────────────────────
# 1) Brief History of Streamlit
# ────────────────────────────────────────────────────────────────────────────────
st.header("1) A Brief History of Streamlit")
st.markdown("""
Streamlit was founded in 2018 by Adrien Treuille, Amanda Kelly, and Thiago Teixeira, with public momentum growing in 2019. 
On March 2, 2022, the company was acquired by Snowflake, though it continues as an open-source Python framework that enables 
developers to transform scripts into interactive web applications with minimal boilerplate. For educators, Streamlit is 
especially valuable for rapidly prototyping classroom tools such as dashboards, simulations, and machine learning 
demonstrations without the need for extensive front-end development.
""")

st.markdown("""
**References**

Streamlit. (n.d.). *Architecture overview: Client–server execution model*. Streamlit Documentation. Retrieved August 21, 2025, from https://docs.streamlit.io/develop/concepts/architecture/architecture  

Streamlit. (2020, October 1). *Announcing Streamlit’s $21M Series A*. Streamlit Blog. Retrieved August 21, 2025, from https://blog.streamlit.io/announcing-streamlits-21m-series-a/  

Snowflake. (2022, March 2). *Snowflake announces intent to acquire Streamlit to empower developers and data scientists to mobilize the world’s data*. Snowflake Press Release. Retrieved August 21, 2025, from https://www.snowflake.com/en/news/press-releases/snowflake-announces-intent-to-acquire-streamlit-to-empower-developers-and-data-scientists-to-mobilize-the-worlds-data/  
""")

# ────────────────────────────────────────────────────────────────────────────────
# 2) Popular apps & showcases built with Streamlit (image tiles with links)
# ────────────────────────────────────────────────────────────────────────────────
st.header("2) Popular apps & showcases built with Streamlit")

# Target URLs (open in new tab)
LINK_DEMO_SETUP = "https://just-merwan.medium.com/how-to-use-streamlit-webgui-with-ros-f7a17f966552"
LINK_HANDS_ON   = "https://www.ultralytics.com/blog/run-an-interactive-ai-app-with-streamlit-and-ultralytics-yolo11"
LINK_ADAPTATION = "https://discuss.streamlit.io/t/how-to-build-an-llm-powered-chatbot-with-streamlit/42916"

# Local thumbnails (committed to your repo under images/)
IMG_DEMO_SETUP = "images/demo_setup.png"
IMG_HANDS_ON   = "images/hands_on_widget.png"
IMG_ADAPTATION = "images/adaptation_theme.png"

# Convert local images → base64 data URIs (so they always render)
SRC_DEMO_SETUP = _img_data_uri(IMG_DEMO_SETUP)
SRC_HANDS_ON   = _img_data_uri(IMG_HANDS_ON)
SRC_ADAPTATION = _img_data_uri(IMG_ADAPTATION)

st.markdown("""
<style>
.tile-wrap { text-align:center; }
.tile {
  display:block; text-decoration:none; color:inherit; border-radius:18px; overflow:hidden;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  transition: transform 160ms ease, box-shadow 160ms ease;
  background: white;
}
.tile:hover { transform: translateY(-4px); box-shadow: 0 14px 32px rgba(0,0,0,0.22); }
.tile img { width:auto; height:140px; margin:auto; display:block; object-fit:contain; }  /* <-- replace this line */
.tile h4 { margin:10px 12px 6px; font-size:1.0rem; }
.tile p  { margin:0 12px 14px; font-size:0.9rem; color:#555; }
.caption { color:#6b7280; font-size:0.85rem; margin-top:6px; }
</style>
""", unsafe_allow_html=True)


def tile(html_id: str, href: str, img_src: str, title: str, subtitle: str):
    st.markdown(
        f"""
        <div class="tile-wrap" id="{html_id}">
          <a class="tile" href="{href}" target="_blank" rel="noopener noreferrer">
            <img src="{img_src}" alt="{title}">
            <h4>{title}</h4>
            <p>{subtitle}</p>
          </a>
        </div>
        """,
        unsafe_allow_html=True
    )

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    tile(
        "demo-setup",
        LINK_DEMO_SETUP,
        SRC_DEMO_SETUP,  # <-- use data URI
        "Demo Setup",
        "Streamlit WebGUI for ROS — control & monitor robotics via a browser."
    )
    st.markdown('<div class="caption">Opens in a new tab</div>', unsafe_allow_html=True)

with c2:
    tile(
        "hands-on",
        LINK_HANDS_ON,
        SRC_HANDS_ON,  # <-- use data URI
        "Hands-on Widget",
        "YOLO11 live object detection — upload media and see detections instantly."
    )
    st.markdown('<div class="caption">Opens in a new tab</div>', unsafe_allow_html=True)

with c3:
    tile(
        "adaptation",
        LINK_ADAPTATION,
        SRC_ADAPTATION,  # <-- use data URI
        "Adaptation Theme",
        "LLM-powered chatbot blueprint — adapt as a coding/robotics helper."
    )
    st.markdown('<div class="caption">Opens in a new tab</div>', unsafe_allow_html=True)




# ────────────────────────────────────────────────────────────────────────────────
# 3) Client side
# ────────────────────────────────────────────────────────────────────────────────
st.header("3) Client side: laptops, tablets, and phones")
st.markdown("""
When you use Streamlit on a laptop, tablet, or phone, it works through the web browser. The browser is the “client,”
which means it shows the app’s visuals. The Python code, however, runs somewhere else (on the “server”). Whenever you
move a slider, click a button, or change a widget, the app’s code is re-run on the server and the updated results are
sent back to your browser almost instantly. Streamlit supports the latest versions of browsers like Chrome, Firefox,
Edge, and Safari. The layout is designed to be **responsive**, meaning it automatically changes how the information is
arranged and displayed based on the size and type of device you are using. This makes Streamlit work well on mobile
devices, though very wide tables or charts may still need small adjustments to display neatly.
""")

# ────────────────────────────────────────────────────────────────────────────────
# 4) Server/host side
# ────────────────────────────────────────────────────────────────────────────────
st.header("4) Server/host side: rendering for all devices")
st.markdown("""
The “server” is the computer that actually runs your Streamlit app’s Python code. Think of it as the engine behind the
scenes. Every time a user interacts with the app, the server re-runs the script from top to bottom, quickly updates
the results, and then sends those updates back to the client (the user’s browser). To make apps faster, Streamlit uses
**caching**, which means it can remember the results of expensive calculations or data loading so it doesn’t have to
repeat the same work every time. This setup makes it possible for many people on different devices—laptops, tablets,
or phones—to use the same app at once. You can run the server on your own computer for testing, or host it in the
cloud (like Streamlit Community Cloud or Snowflake) so anyone with the link can access it.
""")


# ------------------------
# 5) Cloud services for storing & retrieving data (prices/month)
# ------------------------
st.header("5) Cloud services for storing & retrieving data")

st.markdown("> **Note:** Storage/database prices vary by region, usage, operations, and egress. Values below are common headline rates as of **Aug 2025** (check provider pages for your region).")

data = [
    {
        "Service": "Amazon S3 (object storage)",
        "Typical Pricing / Month": "S3 Standard: ~$0.023/GB-mo (first 50TB); Free Tier 5GB for first 12 months",
        "Free Tier?": "Yes (12-month 5GB)",
        "Reference": "[AWS S3 pricing](https://aws.amazon.com/s3/pricing/); guide: [CloudZero 2025](https://www.cloudzero.com/blog/s3-pricing/); free-tier note: [nOps 2025](https://www.nops.io/blog/how-much-do-aws-s3-storage-classes-cost/)"
    },
    {
        "Service": "Google Cloud Storage (object storage)",
        "Typical Pricing / Month": "US regions commonly ~$0.02–$0.026/GB-mo (class & region vary)",
        "Free Tier?": "Limited credits for new accounts; pay-as-you-go",
        "Reference": "[GCS pricing](https://cloud.google.com/storage/pricing) & [pricing examples](https://cloud.google.com/storage/pricing-examples)"
    },
    {
        "Service": "Azure Blob Storage (object storage)",
        "Typical Pricing / Month": "Hot LRS: ~**$0.018/GB-mo** (first 50TB) in many regions",
        "Free Tier?": "No permanent free tier",
        "Reference": "Azure page: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/ ; overview: https://www.cloudzero.com/blog/azure-blob-storage-pricing/"
    },
    {
        "Service": "Supabase (Postgres + auth + storage)",
        "Typical Pricing / Month": "Free tier; paid from **$10/mo** (project); usage-based beyond",
        "Free Tier?": "Yes",
        "Reference": "https://supabase.com/pricing ; 2025 breakdown: https://uibakery.io/blog/supabase-pricing"
    },
    {
        "Service": "Firebase (Firestore + Storage via GCS)",
        "Typical Pricing / Month": "**Spark** plan free; **Blaze** pay-as-you-go (GCP rates apply)",
        "Free Tier?": "Yes (Spark)",
        "Reference": "Plans: https://firebase.google.com/docs/projects/billing/firebase-pricing-plans ; Pricing: https://firebase.google.com/pricing"
    },
    {
        "Service": "MongoDB Atlas (managed MongoDB)",
        "Typical Pricing / Month": "Free **M0**; paid shared from **~$9/mo**; serverless op-based",
        "Free Tier?": "Yes (M0)",
        "Reference": "https://www.mongodb.com/pricing ; AWS page: https://www.mongodb.com/products/platform/atlas-cloud-providers/aws/pricing"
    },
    {
        "Service": "Neon (managed Postgres)",
        "Typical Pricing / Month": "**Free** plan $0; paid plans from **$5/mo min fee** + usage",
        "Free Tier?": "Yes",
        "Reference": "Pricing: https://neon.com/pricing ; Plan details: https://neon.com/docs/introduction/plans"
    },
    {
        "Service": "Airtable (cloud spreadsheet/DB)",
        "Typical Pricing / Month": "Free tier; paid typically **$20–$24 per user/mo** (annual); Business ~$45/user/mo (annual)",
        "Free Tier?": "Yes",
        "Reference": "https://airtable.com/pricing ; Docs: https://support.airtable.com/docs/airtable-plans"
    },
    {
        "Service": "Google Sheets (via Google Workspace)",
        "Typical Pricing / Month": "Business Standard **$14 per user/mo** (annual pricing varies)",
        "Free Tier?": "No permanent free plan (except Workspace trials)",
        "Reference": "https://workspace.google.com/pricing ; plan page: https://workspace.google.com/individual/"
    },
]

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
# End
