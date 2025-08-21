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
