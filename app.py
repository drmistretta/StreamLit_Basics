# streamlit_app.py
import streamlit as st
import pandas as pd
from datetime import date

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
# 4) Server/host side: rendering for all devices
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

# ────────────────────────────────────────────────────────────────────────────────
# 5) Cloud services to store/retrieve data (indicative monthly pricing)
# ────────────────────────────────────────────────────────────────────────────────
st.header("5) Common cloud data options (with free tiers where available)")
st.markdown("""
> Prices vary by **region**, **storage class/tier**, **API operations**, and **egress**. Values here reflect commonly cited headline rates as of **Aug 2025**; always check the provider page for your region and workload details.
""")

rows = [
    {
        "Service": "Amazon S3 (object storage)",
        "Typical pricing": "S3 Standard ~ **$0.023/GB-mo** (first 50TB)",
        "Free tier": "AWS Free Tier: 5 GB for 12 months",
        "Learn more": "https://aws.amazon.com/s3/pricing/ • https://www.cloudzero.com/blog/s3-pricing/"
    },
    {
        "Service": "Google Cloud Storage (object storage)",
        "Typical pricing": "Region-dependent; Standard often **~$0.02–$0.026/GB-mo**",
        "Free tier": "New-account credits; otherwise pay-as-you-go",
        "Learn more": "https://cloud.google.com/storage/pricing • https://cloud.google.com/storage/pricing-examples"
    },
    {
        "Service": "Azure Blob Storage (object storage)",
        "Typical pricing": "Hot tier commonly cited **~$0.018/GB-mo** (first 50TB)",
        "Free tier": "No permanent free tier",
        "Learn more": "https://azure.microsoft.com/en-us/pricing/details/storage/blobs/ • https://www.cloudzero.com/blog/azure-blob-storage-pricing/"
    },
    {
        "Service": "Supabase (Postgres + auth + storage)",
        "Typical pricing": "**Free** tier; paid from **$10/mo** (usage-based beyond)",
        "Free tier": "Yes",
        "Learn more": "https://supabase.com/pricing • https://uibakery.io/blog/supabase-pricing"
    },
    {
        "Service": "Firebase (Firestore + Storage via GCS)",
        "Typical pricing": "**Spark** free plan; **Blaze** pay-as-you-go (GCP rates apply)",
        "Free tier": "Yes (Spark)",
        "Learn more": "https://firebase.google.com/pricing • https://firebase.google.com/docs/projects/billing/firebase-pricing-plans"
    },
    {
        "Service": "MongoDB Atlas (managed MongoDB)",
        "Typical pricing": "Free **M0**; paid shared from **~$9/mo** (region/size vary)",
        "Free tier": "Yes (M0)",
        "Learn more": "https://www.mongodb.com/pricing • https://www.mongodb.com/products/platform/atlas-cloud-providers/aws/pricing"
    },
    {
        "Service": "Neon (managed Postgres)",
        "Typical pricing": "**Free** plan $0; paid plans **$5/mo minimum** + usage",
        "Free tier": "Yes",
        "Learn more": "https://neon.com/pricing • https://neon.com/docs/introduction/plans"
    },
    {
        "Service": "Airtable (cloud DB/spreadsheet)",
        "Typical pricing": "Team **$20/user/mo (annual)**; Business **$45/user/mo (annual)**",
        "Free tier": "Yes",
        "Learn more": "https://airtable.com/pricing • https://support.airtable.com/docs/airtable-plans"
    },
    {
        "Service": "Google Sheets (via Google Workspace)",
        "Typical pricing": "Business Standard **$16.80/user/mo** (flex; **$14** annual)",
        "Free tier": "Trials only; no permanent free Workspace tier",
        "Learn more": "https://workspace.google.com/pricing • https://9to5google.com/2025/01/15/google-workspace-price-increase-2025/"
    },
]
st.dataframe(pd.DataFrame(rows), use_container_width=True)

st.divider()
st.subheader("Deployment notes for your course (GitHub → Streamlit Community Cloud)")
st.markdown("""
- Put your code in a public GitHub repo with `requirements.txt`.
- On **Streamlit Community Cloud**, connect your GitHub, pick the repo/branch, and set the **main file path** (e.g., `streamlit_app.py`).
- For secrets (API keys, DB URLs), use the platform’s **Secrets** UI—never commit secrets to Git.
- For private/enterprise needs and governed data, consider **Streamlit in Snowflake**.
""")

# End

