import requests
import kaggle
import os
import streamlit as st

# Set your Kaggle API credentials
os.environ["KAGGLE_USERNAME"] = "your_kaggle_username"
os.environ["KAGGLE_KEY"] = "your_kaggle_api_key"

def fetch_kaggle_datasets(use_case):
    """Fetch up to 5 relevant Kaggle datasets for a given AI use case."""
    try:
        datasets = kaggle.api.dataset_list(search=use_case)[:5]
        return [f"{idx+1}. [Kaggle Dataset]({f'https://www.kaggle.com/{dataset.ref}'})" 
                for idx, dataset in enumerate(datasets)] if datasets else []
    except Exception as e:
        return [f"⚠️ Error fetching Kaggle datasets: {str(e)}"]

def fetch_github_repos(use_case):
    """Fetch up to 5 top GitHub repositories for a given AI use case."""
    github_url = f"https://api.github.com/search/repositories?q={use_case.replace(' ', '+')}&sort=stars&per_page=5"
    try:
        response = requests.get(github_url)
        if response.status_code == 200:
            return [f"{idx+1}. [GitHub Repo]({repo['html_url']})" 
                    for idx, repo in enumerate(response.json().get('items', []))] or []
    except Exception as e:
        return [f"⚠️ Error fetching GitHub repositories: {str(e)}"]

def fetch_resources(use_case):
    """Fetch Kaggle datasets and GitHub repositories for a given AI use case."""
    kaggle_links = fetch_kaggle_datasets(use_case) or []  # ✅ Ensure it's always a list
    github_links = fetch_github_repos(use_case) or []     # ✅ Ensure it's always a list

    return {
        "use_case": use_case,
        "kaggle_links": kaggle_links,
        "github_links": github_links
    }

def main():
    """Streamlit UI for AI resources"""
    st.title("🔍 AI Resource Finder")

    use_case = st.text_input("Enter AI Use Case", "Natural Language Processing")
    if st.button("Fetch Resources"):
        resources = fetch_resources(use_case) or {}  # ✅ Ensure it's always a dictionary
        
        st.subheader(f"📌 AI Resources for {use_case}")

        st.markdown("### 📊 Kaggle Datasets")
        for link in resources.get("kaggle_links", []):  # ✅ Handle missing keys safely
            st.markdown(link)

        st.markdown("### 🛠️ GitHub Repositories")
        for link in resources.get("github_links", []):  # ✅ Handle missing keys safely
            st.markdown(link)

        # Format content for download
        resource_content = f"# 🔍 AI Resource Collection: {use_case}\n\n"
        resource_content += "## 📊 Kaggle Datasets\n" + "\n".join(resources.get("kaggle_links", [])) + "\n\n"
        resource_content += "## 🛠️ GitHub Repositories\n" + "\n".join(resources.get("github_links", [])) + "\n"

        # Provide download button
        st.download_button_
