# --- Add near the top (after imports) ---
import streamlit as st
import pandas as pd
from datetime import date
import time

# 1) Cache heavy/static data (your cloud services table)
@st.cache_data
def get_cloud_table() -> pd.DataFrame:
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
            "Best use case": "Web apps needing Postgres + authentication (student projects, quick prototypes)",
            "Learn more": "https://supabase.com/pricing • https://uibakery.io/blog/supabase-pricing"
        },
        {
            "Service": "Firebase (Firestore + Storage via GCS)",
            "Typical pricing": "**Spark** free plan; **Blaze** pay-as-you-go (GCP rates apply)",
            "Free tier": "Yes (Spark)",
            "Best use case": "Mobile/web apps with real-time sync and auth",
            "Learn more": "https://firebase.google.com/pricing • https://firebase.google.com/docs/projects/billing/firebase-pricing-plans"
        },
        {
            "Service": "MongoDB Atlas (managed MongoDB)",
            "Typical pricing": "Free **M0**; paid shared from **~$9/mo** (region/size vary)",
            "Free tier": "Yes (M0)",
            "Best use case": "Flexible NoSQL for JSON-style data and student APIs",
            "Learn more": "https://www.mongodb.com/pricing • https://www.mongodb.com/products/platform/atlas-cloud-providers/aws/pricing"
        },
        {
            "Service": "Neon (managed Postgres)",
            "Typical pricing": "**Free** plan $0; paid plans **$5/mo minimum** + usage",
            "Free tier": "Yes",
            "Best use case": "Lightweight Postgres with modern features for small projects",
            "Learn more": "https://neon.com/pricing • https://neon.com/docs/introduction/plans"
        },
        {
            "Service": "Airtable (cloud DB/spreadsheet)",
            "Typical pricing": "Team **$20/user/mo (annual)**; Business **$45/user/mo (annual)**",
            "Free tier": "Yes",
            "Best use case": "Spreadsheet–database hybrid; lesson planning & small datasets",
            "Learn more": "https://airtable.com/pricing • https://support.airtable.com/docs/airtable-plans"
        },
        {
            "Service": "Google Sheets (via Google Workspace)",
            "Typical pricing": "Business Standard **$16.80/user/mo** (flex; **$14** annual)",
            "Free tier": "Trials only; no permanent free Workspace tier",
            "Best use case": "Simple collaborative data tables for teachers on Workspace",
            "Learn more": "https://workspace.google.com/pricing • https://9to5google.com/2025/01/15/google-workspace-price-increase-2025/"
        },
    ]
    return pd.DataFrame(rows)

# 2) Put the small rerun demo in a fragment so only that area updates (best-effort)
#    Use st.fragment if available; otherwise fall back to a normal function.
if hasattr(st, "fragment"):
    @st.fragment
    def rerun_demo_fragment():
        with st.expander("Optional: tiny live demo to illustrate reruns"):
            val = st.slider("Move me to trigger a rerun (isolated)", 0, 100, 25, key="rerun_demo_slider")
            st.write(f"Reruns feel instantaneous—current slider value: **{val}**")
else:
    def rerun_demo_fragment():
        # Fallback: same UI; caching elsewhere still avoids heavy recompute costs.
        with st.expander("Optional: tiny live demo to illustrate reruns"):
            val = st.slider("Move me to trigger a rerun", 0, 100, 25, key="rerun_demo_slider")
            st.write(f"Reruns feel instantaneous—current slider value: **{val}**")
