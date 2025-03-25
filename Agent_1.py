import streamlit as st
from tavily import TavilyClient
import pandas as pd
import io
import os
from config import CONFIG 

# Set Tavily API Key
os.environ["TAVILY_API_KEY"] = CONFIG["TAVILY_API_KEY"]
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# Function to generate company-specific search queries
def generate_search_query(company_name, industry):
    return [
        f"Top competitors of {company_name} in the {industry} industry",
        f"{company_name} annual report and strategic goals",
        f"How {company_name} is adopting AI in operations and customer experience",
        f"Industry leaders in {industry} and their AI adoption strategies",
        f"Market trends in {industry} industry related to AI, ML, and automation",
    ]

# Function to perform market research using Tavily
def perform_market_research(company_name, industry):
    if not company_name or not industry:
        return "⚠️ Please provide valid inputs for company and industry."

    queries = generate_search_query(company_name, industry)
    research_results = []

    st.subheader("🔍 Market Research Insights")  # Section Title

    for query in queries:
        try:
            response = tavily_client.search(query=query, search_depth="basic")
            top_links = response.get("results", [])[:3]  # Selecting Top 3 results

            # Display search category
            st.markdown(f"### 🔹 {query}")
            selected_links = []
            
            for res in top_links:
                selected_links.append(res["url"])
                research_results.append({
                    "Use Cases": query,
                    "Description": "Relevant market research insights",
                    "Reference": res["url"]
                })

            # Display selected links in bullet format
            for link in selected_links:
                st.markdown(f"- 🔗 [{link}]({link})")

        except Exception as e:
            research_results.append({
                "Use Cases": query,
                "Description": f"⚠️ Error fetching results: {str(e)}",
                "Reference": "N/A"
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(research_results, columns=["Use Cases", "Description", "Reference"])

    # Display formatted DataFrame
    st.markdown("### 📊 Market Research Summary")
    st.dataframe(df)

    # Save to an in-memory Excel file (No Local Storage)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    
    output.seek(0)

    # Provide a download button
    st.download_button(
        label="⬇️ Download Market Research Report",
        data=output,
        file_name=f"market_research_{company_name.replace(' ', '_')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
