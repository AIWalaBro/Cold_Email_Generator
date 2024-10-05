import streamlit as st
from portfolio import Portfolio
from chains import Chain
from utils import clean_text
import os
from langchain_community.document_loaders import WebBaseLoader


def create_streamlit_application(llm, portfolio, clean_text):
    st.title("📧 Lead Generator via Cold Email")
    url_input = st.text_input("Enter a URL:", value = "https://jobs.nike.com/job/R-40156?from=job%20search%20funnel")
    submit_button = st.button("Submit")


    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links  = portfolio.query_links(skills)
                email  = llm.write_email(job, links)
                st.code(email, language = "markdown")

        except Exception as e:
            st.error(f" An error Ocurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Lead Generator via Cold Email", page_icon="📧")
    create_streamlit_application(chain, portfolio, clean_text)

