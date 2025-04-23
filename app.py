import streamlit as st
from data_fetch.wikipedia_fetch import get_wikipedia_summary
from data_fetch.arxiv_fetch import get_arxiv_abstracts
from summarizer import summarize_text

st.title("🧠 AI Research Agent (Free Stack)")

topic = st.text_input("Enter your research topic:")

if topic:
    st.subheader("📚 Wikipedia Summary")
    wiki = get_wikipedia_summary(topic)
    st.text_area("Wikipedia", wiki, height=200)

    st.subheader("📄 ArXiv Paper Abstracts")
    papers = get_arxiv_abstracts(topic)

    for p in papers:
        st.markdown(f"**{p['title']}**\n\n{p['summary']}\n\n[Read more]({p['url']})")

    combined_text = wiki + "\n".join([p["summary"] for p in papers])

    st.subheader("✏️ AI Summary (DistilBART)")
    with st.spinner("Summarizing..."):
        summary = summarize_text(combined_text)
    st.text_area("Summary", summary, height=250)

    st.download_button("Download Report", summary, file_name=f"{topic.replace(' ', '_')}_summary.txt")