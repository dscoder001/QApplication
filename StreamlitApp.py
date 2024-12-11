from pathlib import Path
import PyPDF2
import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model


if 'index_generated' not in st.session_state:
    st.session_state.index_generated = False

if 'query_engine' not in st.session_state:
    st.session_state.query_engine = None


def on_document_change():
    st.session_state.index_generated = False
    
def main():
    st.set_page_config("QA with Documents")
    doc=st.file_uploader("Upload your document", on_change=on_document_change)


    if doc and not st.session_state.index_generated:
        Path("Data").mkdir(exist_ok=True)
        Path("Data/uploaded.pdf").touch(exist_ok=True)
        with open(f"Data/uploaded.pdf", 'wb') as f: 
            f.write(doc.read())
        
        document=load_data(doc)
        model=load_model()
        query_engine=download_gemini_embedding(model,document)
        
        st.session_state.query_engine=query_engine
    
        # print("Index regenerated")
        st.session_state.index_generated = True
   

    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            query_engine=st.session_state.query_engine
            if not query_engine:
                st.error("Please upload your document again")

            response = query_engine.query(user_question)
            st.write(response.response)

                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    