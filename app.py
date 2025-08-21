# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import date
import time   # NEW import for caching demo

st.set_page_config(page_title="Streamlit for Educators", layout="wide")

st.title("Streamlit for Educators: Teaching Notes & Demos")
st.caption(f"Last updated: {date.today().isoformat()} • Deployed from GitHub (recommended for your course).")

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
# 2) What popular web applications use Streamlit?
# ────────────────────────────────────────────────────────────────────────────────
st.header("2) Popular apps & showcases built with Streamlit")
st.markdown("""
- **Official Gallery:** Hundreds of public apps across ML, education, data viz, and science.  
  - https://streamlit.io/gallery
- **Case studies (production/internal):**
  - **Delta Dental** (decision support): https://blog.streamlit.io/how-delta-dental-uses-streamlit-to-make-lightning-fast-decisions/
  - **Open Insurance (Snowflake story)** (self-service data apps): https://www.snowflake.com/en/customers/all-customers/case-study/open-insurance/

*Teaching tip:* For K–12 PD, pick 2–3 gallery apps aligned to your cohort (e.g., image classification demos, classroom analytics) and walk through the code → widget → rerun cycle.
""")

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

with st.expander("Optional: tiny live demo to illustrate reruns"):
    val = st.slider("Move me to trigger a rerun", 0, 100, 25)
    st.write(f"Reruns feel instantaneous—current slider value: **{val}**")

# NEW ─────────────────────────────────────────────────────────────────────────────
# Live demo: Caching dataset loading (with timer)
# ────────────────────────────────────────────────────────────────────────────────
st.subheader("Caching Demo: Loading a Dataset (with timer)")

@st.cache_data
def load_dataset(n_rows: int = 5):
    """Simulate a slow dataset load, but cache results for faster repeat access."""
    time.sleep(3)  # simulate slow loading
    data = pd.DataFrame({
        "Number": range(1, n_rows + 1),
        "Square": [x**2 for x in range(1, n_rows + 1)]
    })
    return data

rows = st.slider("How many rows to load?", 5, 50, 5)

t0 = time.perf_counter()
with st.spinner("Loading dataset... (cached after first load)"):
    df = load_dataset(rows)
elapsed = time.perf_counter() - t0

cached_hint = "✅ Likely **CACHED**" if elapsed < 1.0 else "🕒 **FRESH** (not cached yet)"
st.success(f"Done in {elapsed:.3f} seconds — {cached_hint}")
st.dataframe(df, use_container_width=True)
st.metric(label="Elapsed load time (s)", value=f"{elapsed:.3f}")

rows = [
    {
        "Service": "Amazon S3 (object storage)",
        "Typical pricing": "S3 Standard ~ **$0.023/GB-mo** (first 50TB)",
        "Free tier": "AWS Free Tier: 5 GB for 12 months",
        "Best use case": "General-purpose object storage; great for datasets, images, or logs",
        "Learn more": "https://aws.amazon.com/s3/pricing/ • https://www.cloudzero.com/blog/s3-pricing/"
    },
    {
        "Service": "Google Cloud Storage (object storage)",
        "Typical pricing": "Region-dependent; Standard often **~$0.02–$0.026/GB-mo**",
        "Free tier": "New-account credits; otherwise pay-as-you-go",
        "Best use case": "Similar to S3; integrates easily with Google Workspace and AI tools",
        "Learn more": "https://cloud.google.com/storage/pricing • https://cloud.google.com/storage/pricing-examples"
    },
    {
        "Service": "Azure Blob Storage (object storage)",
        "Typical pricing": "Hot tier commonly cited **~$0.018/GB-mo** (first 50TB)",
        "Free tier": "No permanent free tier",
        "Best use case": "Best if your school already uses Microsoft Azure or Office 365",
        "Learn more": "https://azure.microsoft.com/en-us/pricing/details/storage/blobs/ • https://www.cloudzero.com/blog/azure-blob-storage-pricing/"
    },
    {
        "Service": "Supabase (Postgres + auth + storage)",
        "Typical pricing": "**Free** tier; paid from **$10/mo** (usage-based beyond)",
        "Free tier": "Yes",
        "Best use case": "Good for web apps needing a database + authentication (like student projects)",
        "Learn more": "https://supabase.com/pricing • https://uibakery.io/blog/supabase-pricing"
    },
    {
        "Service": "Firebase (Firestore + Storage via GCS)",
        "Typical pricing": "**Spark** free plan; **Blaze** pay-as-you-go (GCP rates apply)",
        "Free tier": "Yes (Spark)",
        "Best use case": "Great for mobile/web apps with real-time sync and authentication",
        "Learn more": "https://firebase.google.com/pricing • https://firebase.google.com/docs/projects/billing/firebase-pricing-plans"
    },
    {
        "Service": "MongoDB Atlas (managed MongoDB)",
        "Typical pricing": "Free **M0**; paid shared from **~$9/mo** (region/size vary)",
        "Free tier": "Yes (M0)",
        "Best use case": "Flexible NoSQL database; great for JSON-style data and student APIs",
        "Learn more": "https://www.mongodb.com/pricing • https://www.mongodb.com/products/platform/atlas-cloud-providers/aws/pricing"
    },
    {
        "Service": "Neon (managed Postgres)",
        "Typical pricing": "**Free** plan $0; paid plans **$5/mo minimum** + usage",
        "Free tier": "Yes",
        "Best use case": "Lightweight Postgres with modern features; good for small student projects",
        "Learn more": "https://neon.com/pricing • https://neon.com/docs/introduction/plans"
    },
    {
        "Service": "Airtable (cloud DB/spreadsheet)",
        "Typical pricing": "Team **$20/user/mo (annual)**; Business **$45/user/mo (annual)**",
        "Free tier": "Yes",
        "Best use case": "User-friendly spreadsheet-database hybrid; perfect for lesson planning",
        "Learn more": "https://airtable.com/pricing • https://support.airtable.com/docs/airtable-plans"
    },
    {
        "Service": "Google Sheets (via Google Workspace)",
        "Typical pricing": "Business Standard **$16.80/user/mo** (flex; **$14** annual)",
        "Free tier": "Trials only; no permanent free Workspace tier",
        "Best use case": "Teachers already using Google Workspace; simple collaborative storage",
        "Learn more": "https://workspace.google.com/pricing • https://9to5google.com/2025/01/15/google-workspace-price-increase-2025/"
    },
]

st.dataframe(pd.DataFrame(rows), use_container_width=True)


# End
