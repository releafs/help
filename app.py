import streamlit as st
import os

# Function to load content from a Markdown file
def load_step_content(step_file):
    file_path = os.path.join("contents", step_file)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return content
    else:
        return "Content not available."

# Define the steps with questions and file paths
steps = {
    "Set Up MetaMask Wallet": {
        "question": "Do you need help setting up a MetaMask wallet?",
        "file": "step1.md"
    },
    "Connect MetaMask to Base Network": {
        "question": "Do you need guidance on connecting MetaMask to the Base network?",
        "file": "step2.md"
    },
    "Fund MetaMask Wallet with Base Tokens": {
        "question": "Do you need assistance with funding your MetaMask wallet with Base tokens?",
        "file": "step3.md"
    },
    "Apply for Allowlist Access": {
        "question": "Do you need help applying for the Releafs allowlist?",
        "file": "step4.md"
    },
    "Mint Releafs Tokens": {
        "question": "Would you like a guide on minting Releafs tokens on OpenSea?",
        "file": "step5.md"
    }
}

# Set up the app title and introduction
st.title("Releafs Support System")
st.write("""
Welcome to the Releafs Support System! Please answer the questions below to let us know which steps you need assistance with. 
Based on your responses, we'll generate a tailored guide to help you set up and use your MetaMask wallet to mint Releafs tokens.
""")

# Add custom CSS to style the radio buttons to look like buttons and change color on selection
st.markdown("""
<style>
/* Increase font size of questions */
h3 {
    font-size: 24px !important;
}

/* Style the radio buttons */
div[role='radiogroup'] > label {
    display: none;
}

div[role='radiogroup'] {
    flex-direction: row;
    justify-content: flex-start;
}

div[role='radiogroup'] .streamlit-expanderHeader {
    padding: 0;
}

div[role='radiogroup'] > div {
    margin: 5px;
}

div[role='radiogroup'] > div > div {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 60px;
    width: 100%;
    background-color: #0073e6;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

div[role='radiogroup'] > div:hover > div {
    background-color: #005bb5;
}

div[role='radiogroup'] > div:focus > div {
    outline: none;
    box-shadow: none;
}

div[role='radiogroup'] > div:active > div {
    background-color: #005bb5;
}

div[role='radiogroup'] > div[selected] > div {
    background-color: grey !important;
}

</style>
""", unsafe_allow_html=True)

# Initialize session state to remember selections
if 'user_needs' not in st.session_state:
    st.session_state.user_needs = {}

needs_tutorial = False

# Questionnaire with questions and custom-styled radio buttons
st.header("Questionnaire")
for step_name, step_info in steps.items():
    st.markdown(f"<h3>{step_info['question']}</h3>", unsafe_allow_html=True)
    options = ["Yes", "No"]
    default_index = options.index(st.session_state.user_needs.get(step_name, "Yes")) if step_name in st.session_state.user_needs else 0
    selection = st.radio(
        label="",
        options=options,
        index=default_index,
        key=step_name,
        label_visibility='collapsed'
    )
    st.session_state.user_needs[step_name] = selection

# Generate tutorial based on responses
if st.button("Generate Customized Guide"):
    st.write("### Your Customized Releafs Guide")
    for step_name, step_info in steps.items():
        if st.session_state.user_needs[step_name] == "Yes":
            st.subheader(step_name)
            content = load_step_content(step_info["file"])
            st.markdown(content)
            needs_tutorial = True

    if not needs_tutorial:
        st.info("It seems like you don’t need any tutorials. If you still need help, feel free to review the questions or reach out to our support team.")

# Completion message
if needs_tutorial:
    st.write("""
    ### Congratulations!
    You have completed the necessary steps to set up your MetaMask and mint Releafs tokens. If you have further questions, don't hesitate to ask.
    """)
    st.balloons()
