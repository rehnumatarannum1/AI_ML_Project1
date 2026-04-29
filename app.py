import streamlit as st
from api import generate_note,generate_quiz,generate_audio


#Title
st.title("Notes and Quiz Generator :memo:")
st.divider()

#Sidebar
with st.sidebar:
    st.header(":gear: Controls")
    #image
    images=st.file_uploader("Images :framed_picture:",type=['jpg','jpeg','png','heic'],accept_multiple_files=True)
    if images:
        if len(images)>3:
            st.error("Upload at most 3 notes :framed_picture:")
        else:
            st.subheader("Images Uploaded :heart_eyes:")
            col=st.columns(len(images)) #create columns according to the number of images
            for i,img in enumerate(images): #i->column index; img->image index
                with col[i]:
                    st.image(img)
    #selectbox
    level=st.selectbox("Difficulty level of the Quiz :worried:",('Easy','Medium','Hard'),index=None)

    #Button
    clicked=st.button("Generate AI response",type="primary")


if clicked:
   if not images:
       st.error("Upload atleast 1 note :framed_picture:")
   if not level:
       st.error("Select a difficulty level")

   if images and level:
       
       #notesContainer
       with st.container(border=True):
           st.subheader(":spiral_notepad: Notes")
           #API
           with st.spinner("AI is generating your notes..."):
              notes=generate_note(images)
              st.markdown(notes)
       
       #audioContainer
       with st.container(border=True):
            st.subheader(":headphones: Audio ")
            with st.spinner("AI is generating your audio..."):
               clean_notes=notes.replace('*',"") #clearing markdown
               clean_notes=clean_notes.replace('#',"")
               audio=generate_audio(clean_notes)
               st.audio(audio)

       #quizContainer
       with st.container(border=True):
           st.subheader(f":brain: Quiz: {level}")
           with st.spinner("AI is generating your quiz..."):
                quiz=generate_quiz(images,level)
                st.markdown(quiz)
