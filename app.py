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

# Initialize session state to remember selections
if "user_needs" not in st.session_state:
    st.session_state.user_needs = {step: None for step in steps.keys()}

# Questionnaire with clear radio buttons for selections
st.header("Questionnaire")
for step_name, step_info in steps.items():
    # Display the question with a radio selection
    st.write(f"**{step_info['question']}**")
    st.session_state.user_needs[step_name] = st.radio(
        f"Choose for {step_name}",
        options=["Yes, I need help", "No, I am comfortable"],
        index=1 if st.session_state.user_needs[step_name] == "No" else 0,
        key=step_name
    )

# Generate tutorial based on responses
if st.button("Generate Customized Guide"):
    st.write("### Your Customized Releafs Guide")
    needs_tutorial = False  # Reset inside this block in case the button is clicked multiple times
    
    # Display tutorials for steps marked as "Yes"
    for step_name, step_info in steps.items():
        if st.session_state.user_needs[step_name] == "Yes, I need help":
            st.subheader(step_name)
            content = load_step_content(step_info["file"])
            st.markdown(content)
            needs_tutorial = True

    if not needs_tutorial:
        st.info("It seems like you don’t need any tutorials. If you still need help, feel free to review the questions or reach out to our support team.")

# Completion message, only shown if tutorials were generated
if needs_tutorial:
    st.write("""
    ### Congratulations!
    You have completed the necessary steps to set up your MetaMask and mint Releafs tokens. If you have further questions, don't hesitate to ask.
    """)
    st.balloons()
