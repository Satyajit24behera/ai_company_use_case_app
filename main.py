import streamlit as st
from Agent_1 import perform_market_research
from Agent_2 import generate_ai_use_cases_with_gemini
from Agent_3 import fetch_resources
import io

# Streamlit Page Config
st.set_page_config(page_title="AI Use Case Generator", page_icon="🚀", layout="wide")

# Main UI
def main():
    st.title("🚀 AI Use Case Generator")
    st.markdown("### Generate AI-driven insights, use cases, and datasets tailored for your business!")

    with st.sidebar:
        st.header("⚙️ Input Parameters")
        company_name = st.text_input("🏢 Company Name", placeholder="Enter company name...")
        industry_name = st.text_input("🌍 Industry", placeholder="Enter industry name...")

        generate_button = st.button("🔍 Generate Insights")

    if generate_button:
        if not company_name or not industry_name:
            st.warning("⚠️ Please enter both company and industry name.")
            return

        st.success("🚀 Processing... This may take a few moments.")

        # Tabs for structured layout
        tab1, tab2, tab3 = st.tabs(["📊 Industry Research", "🤖 AI Use Cases", "📚 Resources"])

        # 📊 Industry Research
        with tab1:
            with st.spinner("Fetching industry insights..."):
                st.subheader("📊 Industry Research & Trends")
                industry_insights = perform_market_research(company_name, industry_name)
                st.success("✅ Market research completed.")


        # 🤖 AI Use Cases
        with tab2:
            with st.spinner("Generating AI use cases..."):
                st.subheader("🤖 AI-Powered Solutions")
                use_case_text = generate_ai_use_cases_with_gemini(company_name, industry_name)
                st.success("✅ AI use cases generated.")

                # Convert text output to downloadable format
                output = io.BytesIO()
                output.write(use_case_text.encode())
                output.seek(0)



        # 📚 Resources Collection
        with tab3:
            with st.spinner("Collecting relevant datasets & resources..."):
                st.subheader("📚 Relevant Datasets & Code Repositories")
                resources = fetch_resources(industry_name)
                st.success("✅ Resources fetched successfully.")

                # Kaggle Datasets
                st.markdown("### 📂 Kaggle Datasets")
                kaggle_links = resources.get("kaggle_links", [])
                if kaggle_links:
                    for link in kaggle_links:
                        st.markdown(f"- 🔗 [Kaggle Dataset]({link})")
                else:
                    st.warning("❌ No Kaggle datasets found.")

                # GitHub Repositories
                st.markdown("### 💻 GitHub Repositories")
                github_links = resources.get("github_links", [])
                if github_links:
                    for link in github_links:
                        st.markdown(f"- 🔗 [GitHub Repository]({link})")
                else:
                    st.warning("❌ No GitHub repositories found.")

if __name__ == "__main__":
    main()
