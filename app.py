import streamlit as st

st.set_page_config(page_title="My webpage",layout="wide")


rad=st.sidebar.radio("Navigation",["Home","Math Notes","Science Notes","Chinese Notes","English Notes"])

if rad == "Home":
     #----HEADER SECTION----
        with st.container():
         st.subheader("This is a coding project from a student in Cathigh, class 2-5")
        st.title("Bright Learning")
        st.write("The main idea of the website is to share a few tips to make our learning better but fun")
        st.write("This is a prototype app, if there is and problem please email hu_siyuan@students.edu.sg")
     #----Purpose of app----
        with st.container():
         st.write("---")
        left_column,right_column=st.columns(2)
        with left_column:
         st.header("Purpose and Goals")
         st.write("##")
         st.write(
                  """
                      In this app you will get to:

                       -better understand each Subject

                       -get motivated in different kinds of learning
             
                       -enjoy everthing while learning

                       If you find all of this interesting then what are you waiting for, jump in!
                   """
                 )
    #----Some Credits and Acknoledgments----
        with st.container():
         st.write("---")
         left_column,right_column=st.columns(2)
         with left_column:
          st.header("Credits and Acknoledgements")
          st.write("##")
          st.write(" I would like to give credit to  Streamlit which provided me confidence and the ability to make the websites and also a thanks to the many tutoriouls that I watch on Youtube.I would also like to thank my friends who encouraged me to take up this new skill and create this platform.Thank you!")



if rad =="Math Notes":
  #----Header----
    with st.container():
      st.title("Math notes section")
  #----Some motivtion----
      with st.container():
       st.write("---")
      left_column,right_column=st.columns(2)
      with right_column:
        st.image('4565686_2423223.jpg', caption='Math is fun')
      with left_column:
          st.header("Correcting Misconceptions")
          st.write("##")
          st.write(
                    """
                         Firstly, you must undesrstand some things about Math:

                              1.Math is not that hard

                              2.You need to understand the different concepts and logics of Math

                              3.disect the complicated equations to simpler equations

                              4.Practise different type of questions

                         Therefore, you should not be scared of Math. 
                         
                         To be honest, it is more like a interesting subject, how they make sophisticated things to display into simpler numeric and graphical things.
                    """
                   )




if rad == "Science Notes":
  #----Header----
   with st.container():
      st.title("Science notes section")
       #----Some motivtion----
      with st.container():
       st.write("---")
      left_column,right_column=st.columns(2)
      with left_column:
          st.header("Correcting Misconceptions")
          st.write("##")
          st.write(
                    """
                         Firstly, you must undesrstand some things about Science:

                              1.Science is split into 3 main components

                              2.You need to understand the different theories(basically just try to memorise the key terms)

                              3.Other than memorise, awide read up about topics revolving around science

                              4.Being able to appy all your knowledge not only in exam but understand why some things appears to be this way in the world

                         Therefore, science might be hard for some, but it is manageble
                         
                         Furthermore, you can choose to focus on which sector of science:Physics;Chemistry;Biology
                    """
                   )

if rad == "Chinese Notes":
  #----Header----
  with st.container():
    st.title("Chinese")
   #----Some motivtion----
    with st.container():
       st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
          st.header("Correcting Misconceptions")
          st.write("##")
          st.write(
                    """
                         Firstly, you must undesrstand some things about Chinese:

                              1.Chinese is very simple, the most important thing is to read widely

                              2.Memorise some chinese characters that would be commonly used or usually tested

                              3.Try using more chinese in our daily lives


                         Therefore, chinese only appears to be hard, we just need to overcome our frustration in chinese
                         
                    """
                   )

if rad =="English Notes":
  #----Header----
   with st.container():
     st.title("English")
     #----Some motivtion----
     with st.container():
       st.write("---")
     left_column,right_column=st.columns(2)
     with left_column:
          st.header("Correcting Misconceptions")
          st.write("##")
          st.write(
                    """
                         Firstly, you must undesrstand some things about English:

                              1.We need to ready very widely, including different topics or style, such as novles, articles and etc

                              2.Make sure our grammer and vocablurary is appropriate

                              3.Speak and write in proper english and not other. (eg.Singlish)


                         Therefore, when you have gotten a bad grade in English, it does not mean you are bad in it, but you lack the contextual knowledge and the proper way of using English
                         
                    """
          )

 







     