import streamlit as st

from streamlit.components.v1 import html
from langchain_ollama import OllamaLLM


model = OllamaLLM(model="codellama:7b")




def generate_question():
    question = """ You are an interactive DSA coding questions bot specializing in generating challenging Python Data Structures and Algorithms questions. Your task is to generate a tough DSA question that tests the user’s problem-solving skills.
    Please provide a detailed question that includes:
    Problem Statement: A clear description of the problem to be solved.
    Input/Output Specifications: Define the format for the input and output.
    Constraints: Specify any constraints or limitations relevant to the problem.
    Example: Include one or more examples with input and expected output.
    Ensure that the question is both challenging and relevant to advanced DSA topics."""
    response = model.invoke(question)
    return response

@st.cache_data
def run_llm(question):
    response = model.invoke(question)
    return response
def solve_question():
    st.markdown("### Type the Question")
    question = st.text_area("_", height=200, key="question")
    
    # st.write(f"**Question:** {question}")
    prompt = f'''
    You are a DSA question solving assistant using python , You have the abilities to 
**Classify the Problem**:
- **Type Classification**: Determine the category of the problem (e.g., Arrays, Linked Lists, Trees, Graphs, Sorting, Searching, Dynamic Programming).
- **Difficulty Level**: Assess and specify the difficulty level of the problem (e.g., Easy, Medium, Hard).

**Generate Python Code Solution**:
- Provide a clear, well-commented Complete Python code solution to the given problem.
- Ensure that the code is efficient and adheres to best practices for readability and performance.

**Summarize the Problem and Solution Approach**:
- Offer a concise summary of the problem.
- Explain the approach or algorithm used to solve the problem, including key concepts and steps involved.
- Guide the user on solving the question.
- Provide hints and tips, time and space complexity analysis.
- Recommend additional problems that are similar in nature or that build upon the same concepts.

**Avoid Unwanted Responses**:
- Refrain from providing explanations, code, or suggestions that are irrelevant to the problem or outside the scope of the task.

**Additional Guidelines**:
- **Handle Edge Cases**: Ensure that the code considers and handles potential edge cases.
- **Provide Examples**: Include example inputs and outputs to illustrate how the code works.
- **Optimize for Performance**: Aim for solutions that are optimal in terms of time and space complexity, where applicable.



following the above rules genreate code for :{question} in the output format : Question,classification, pythoncode, summary,hints,similiar questions.  Also bold the headings'''
    
    if question:
        with st.spinner('Fetching response...'):
            # Fetch the response from the LLM
            response =run_llm(prompt)
            st.write(response)
        st.success('Response received!')
    
    else:
        st.info('Please enter a prompt(ctrl + enter to run).')

       
def solve(question):
    
    question = question
    
    # st.write(f"**Question:** {question}")
    prompt = f'''
    You are a DSA question solving assistant using python , You have the abilities to 
**Classify the Problem**:
- **Type Classification**: Determine the category of the problem (e.g., Arrays, Linked Lists, Trees, Graphs, Sorting, Searching, Dynamic Programming).
- **Difficulty Level**: Assess and specify the difficulty level of the problem (e.g., Easy, Medium, Hard).

**Generate Python Code Solution**:
- Provide a clear, well-commented Python code solution to the given problem.
- Ensure that the code is efficient and adheres to best practices for readability and performance.

**Summarize the Problem and Solution Approach**:
- Offer a concise summary of the problem.
- Explain the approach or algorithm used to solve the problem, including key concepts and steps involved.
- Guide the user on solving the question.
- Provide hints and tips, time and space complexity analysis.
- Recommend additional problems that are similar in nature or that build upon the same concepts.

**Avoid Unwanted Responses**:
- Refrain from providing explanations, code, or suggestions that are irrelevant to the problem or outside the scope of the task.

**Additional Guidelines**:
- **Handle Edge Cases**: Ensure that the code considers and handles potential edge cases.
- **Provide Examples**: Include example inputs and outputs to illustrate how the code works.
- **Optimize for Performance**: Aim for solutions that are optimal in terms of time and space complexity, where applicable.



following the above rules genreate code for :{question} in the output format : Question,classification, pythoncode, summary,hints,similiar questions.  Also bold the headings'''
    
    if question:
        with st.spinner('Fetching response...'):
            # Fetch the response from the LLM
            response =run_llm(prompt)
            st.write(response)
        st.success('Response received!')
    
    else:
        st.info('Please enter a prompt(ctrl + enter to run).')    
        


def interactive_problem_solving():
    st.markdown("### Interactive Problem Solving")
  
    with st.spinner('Fetching Question...'):
        # Fetch the response from the LLM
        question = generate_question()
        st.write(question)
 
    
 
    user_answer = st.text_area("Write the solution:", height=300, key="interactive_implementation")
    if st.button("Show Solution"):
            with st.spinner('solving ..'):
                response = solve(question)
                st.write(response)

        


    

def main():
    st.set_page_config(page_title="DSA.Ai", layout="wide")
    st.title("DSA.ai")

    # Sidebar for navigation
    with st.sidebar:
        st.image("C:/Users/USER/Downloads/logo.png", use_column_width=True)
        # st.header("Navigation")
        option = st.radio("Choose a section", ["Solve", "Practice"])

    # Generate a question
   

    # Show content based on the selected option
    if option == "Solve":
        solve_question()
    elif option == "Practice":
        interactive_problem_solving()

    # Add footer
    st.markdown(
        """
        <style>
        
        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            color: #555;
        }
        </style>
      
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
