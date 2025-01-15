# import random
# import json
# import streamlit as st

# # Load dataset
# def load_data(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         return json.load(file)

# # Main function
# def main():
#     # Configure Streamlit page
#     st.set_page_config(
#         page_title="Movie Quiz Game",
#         page_icon="🎥",
#         layout="centered"
#     )

#     # Hide menu and footer
#     st.markdown(
#         """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         body {
#             background-color: #E3FDFD;
#             font-family: 'Arial', sans-serif;
#         }
#         .stButton>button {
#             background-color: #71C9CE;
#             color: white;
#             border-radius: 5px;
#             font-size: 16px;
#             font-weight: bold;
#         }
#         .stButton>button:hover {
#             background-color: #A6E3E9;
#         }
#         h1, h2, h3 {
#             color: #71C9CE;
#         }
#         .question {
#             font-weight: bold;
#             color: #71C9CE;
#             margin-bottom: 10px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Initialize session state variables
#     if "quiz_started" not in st.session_state:
#         st.session_state.quiz_started = False
#     if "score" not in st.session_state:
#         st.session_state.score = 0
#     if "current_question" not in st.session_state:
#         st.session_state.current_question = 0

#     # Load quiz data
#     data = load_data('data.json')

#     # Title and greeting
#     st.title("🎥 Movie Quiz Game")
#     if not st.session_state.quiz_started:
#         name = st.text_input("Enter your name to start:")
#         if name:
#             st.session_state.name = name
#             st.session_state.quiz_started = True

#     # Quiz logic
#     if st.session_state.quiz_started:
#         if "selected_movie" not in st.session_state:
#             movie_names = [movie['movie'] for movie in data]
#             movie_choice = st.selectbox("Choose a movie:", movie_names)
#             if st.button("Start Quiz"):
#                 st.session_state.selected_movie = next(
#                     movie for movie in data if movie['movie'] == movie_choice)
#                 st.session_state.questions = random.sample(
#                     st.session_state.selected_movie['questions'], k=min(10, len(st.session_state.selected_movie['questions'])))

#         # Display quiz questions
#         if "selected_movie" in st.session_state:
#             current_question = st.session_state.current_question
#             questions = st.session_state.questions

#             if current_question < len(questions):
#                 question = questions[current_question]
#                 st.markdown(
#                     f"<div class='question'>Q{current_question+1}: {question['question']}</div>", unsafe_allow_html=True)

#                 options = question['options']
#                 selected_option = st.radio(
#                     "Select your answer:", options, key=f"q{current_question}")

#                 if st.button("Submit Answer", key=f"submit{current_question}"):
#                     if selected_option.lower() == question['answer'].lower():
#                         st.session_state.score += 1
#                         st.success("Correct!")
#                     else:
#                         st.error(
#                             f"Wrong! The correct answer is: {question['answer']}")

#                     st.session_state.current_question += 1
#             else:
#                 st.write(
#                     f"Your final score is: {st.session_state.score}/{len(questions)}")
#                 if st.button("Restart Quiz"):
#                     st.session_state.clear()

# if __name__ == "__main__":
#     main()



import random
import json
import time
import streamlit as st

# Load dataset
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Main function
def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="MQ Test",
        page_icon="🎥",
        layout="centered"
    )

    # Hide menu and footer
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {
            background-color: #E3FDFD;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #71C9CE;
            color: white;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #A6E3E9;
        }
        h1, h2, h3 {
            color: #71C9CE;
        }
        .question {
            font-weight: bold;
            color: #71C9CE;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state variables
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    # Load quiz data
    data = load_data('data.json')

    # Title and greeting
    st.title("🎥 MQ Test")
    if not st.session_state.quiz_started:
        name = st.text_input("Enter your name to start:")
        if name:
            st.session_state.name = name
            st.session_state.quiz_started = True

    # Quiz logic
    if st.session_state.quiz_started:
        if "selected_movie" not in st.session_state:
            movie_names = [movie['movie'] for movie in data]
            movie_choice = st.selectbox("Choose a movie:", movie_names)
            if st.button("Start Quiz"):
                st.session_state.selected_movie = next(
                    movie for movie in data if movie['movie'] == movie_choice)
                st.session_state.questions = random.sample(
                    st.session_state.selected_movie['questions'], k=min(10, len(st.session_state.selected_movie['questions'])))
        st.session_state.refresh_trigger = False
        # Display all quiz questions at once
        if "selected_movie" in st.session_state:
            questions = st.session_state.questions
            with st.form("quiz_form"):
                st.write(f"Answer all questions for {st.session_state.selected_movie['movie']}:")
                
                # Create a dictionary to hold selected answers
                selected_answers = {}

                for i, question in enumerate(questions):
                    st.markdown(
                        f"<div class='question'>Q{i+1}: {question['question']}</div>", unsafe_allow_html=True)
                    options = question['options']
                    selected_answers[i] = st.radio(
                        "Select your answer:", options, index=None, key=f"q{i}")

                # Submit button for the entire form
                submit_button = st.form_submit_button("Submit All Answers")
                # print(st.session_state.score)
                if submit_button:
                    # Calculate score and prepare feedback
                    score = 0
                    feedback = []  # To store feedback for each question
                    for i, question in enumerate(questions):
                        if selected_answers[i] == None:
                            feedback.append(f"Q{i+1}: 👁️‍🗨️ OOPS you forgot! The correct answer is: {question['answer']}")
                        elif selected_answers[i].lower() == question['answer'].lower():
                            score += 1
                            feedback.append(f"Q{i+1}: ✅ Correct! The answer is: {question['answer']}")
                        else:
                            feedback.append(f"Q{i+1}: ❌ Incorrect. The correct answer is: {question['answer']}")

                    st.session_state.score = score
                    st.write(f"Your final score is: {score}/{len(questions)}")

                    # Display feedback for each question
                    st.subheader("Question Feedback")
                    for fb in feedback:
                        st.write(fb)

                    # Show balloons if all answers are correct
                    if st.session_state.score == len(questions):
                        st.balloons()

                    

if __name__ == "__main__":
    main()

