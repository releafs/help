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
        "file": "step4.md",
        "link": "https://docs.google.com/forms/d/e/1FAIpQLScY_QzJp-O1obN4_fuOqqqsrE-D2Mx3ZaLxqQIRrngG9Dl_5w/viewform?usp=sf_link"
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

# Initialize session state to remember button clicks
if "user_needs" not in st.session_state:
    st.session_state.user_needs = {step: None for step in steps.keys()}

# Initialize needs_tutorial outside the button block to avoid scope issues
needs_tutorial = False

# Questionnaire with larger question fonts and button color indication on selection
st.header("Questionnaire")
for idx, (step_name, step_info) in enumerate(steps.items(), start=1):
    # Display the question in a larger font using Markdown
    st.markdown(f"<h3 style='font-size:22px;'>{step_info['question']}</h3>", unsafe_allow_html=True)
    
    # Define Yes and No buttons with conditional styling for selected states
    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            f"{'✅ ' if st.session_state.user_needs[step_name] == 'Yes' else ''}Yes, I need help with {step_name}",
            key=f"yes_{step_name}",
            help="Click to select Yes",
            args=(step_name, "Yes")
        ):
            st.session_state.user_needs[step_name] = "Yes"

    with col2:
        if st.button(
            f"{'✅ ' if st.session_state.user_needs[step_name] == 'No' else ''}No, I am comfortable with {step_name}",
            key=f"no_{step_name}",
            help="Click to select No",
            args=(step_name, "No")
        ):
            st.session_state.user_needs[step_name] = "No"
    
# Generate tutorial based on responses
if st.button("Generate Customized Guide"):
    st.write("### Your Customized Releafs Guide")
    
    # Display tutorials for each step title, and content only for steps marked as "Yes"
    for idx, (step_name, step_info) in enumerate(steps.items(), start=1):
        # Display content or note for each step depending on selection
        if st.session_state.user_needs[step_name] == "Yes":
            if step_name == "Apply for Allowlist Access":
                st.subheader(f"Step {idx}: {step_name}")
                st.markdown(
                    f"[Click here to apply for the allowlist.]({step_info['link']})",
                    unsafe_allow_html=True
                )
            else:
                content = load_step_content(step_info["file"])
                st.subheader(f"Step {idx}: {step_name}")
                st.markdown(content)
            needs_tutorial = True
        else:
            st.subheader(f"Step {idx}: {step_name}")
            st.write("_No assistance required for this step._")

    if not needs_tutorial:
        st.info("It seems like you don’t need any tutorials. If you still need help, feel free to review the questions or reach out to our support team.")

# Completion message, only shown if tutorials were generated
if needs_tutorial:
    st.write("""
    ### Congratulations!
    You have completed the necessary steps to set up your MetaMask and mint Releafs tokens. If you have further questions, don't hesitate to ask.
    """)
    st.balloons()
