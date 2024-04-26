#Important libraries
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Getting the response from the model
def responseofLLAMA (input_text, no_of_words, blog_type):

    llm = CTransformers(model = "/Users/usmanali/LLM's/ScriptGenius/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type = "llama",
                        config ={
                            'temperature' : 0.01,
                            'max_new_tokens' : 256
                        })
    #The template of the prompt given to the model
    Tempelate = """
                    Write a blog for {blog_type} job profile for a topic {input_text} 
                    within the {no_of_words} of words
                """
    prompt = PromptTemplate(input_variables= ['blog_type','input_text','no_of_words'],
                            template=Tempelate)
    
    # Generating the response from the model
    response = llm(prompt.format(blog_type = blog_type, input_text = input_text, no_of_words = no_of_words))

    return response
    
    
    
#UI of application by uisng stramlit
st.set_page_config(
    page_icon = '🥷🏼',
    page_title = "ScriptGenius",
    layout = 'centered',
    initial_sidebar_state = 'collapsed'
)

#Header
st.header("Welcome to the ScriptGenius 🥷🏼")
#Input text from user
input_text = st.text_input("Let AI know about the Blog-Topic")

#Two important details for blog
col1 ,col2 = st.columns([5,5])

with col1:
    blog_size = st.text_input("Number of Words:")
with col2:
    blog_type = st.selectbox("Choose the Perfect Role:",
                             ('Software Engineer', 'Data Scientist', 'Researchers', 'Common People'),
                             index = 0)
submit = st.button("Generate")

if submit:
    st.write(responseofLLAMA (input_text, blog_size, blog_type))