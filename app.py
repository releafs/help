import streamlit as st
import os

# Set up the app title and initial instructions
st.title("Releafs Support System")
st.write("""
Welcome to the Releafs Support System! This guide will take you step-by-step through setting up MetaMask, 
connecting to the Base network, funding your wallet, applying for allowlist access, and minting Releafs tokens.
""")

# Helper function to load content from a Markdown file
def load_step_content(step_file):
    file_path = os.path.join("contents", step_file)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return content
    else:
        return "Content not available."

# Define the steps and corresponding file names
steps = {
    "Step 1: Set Up MetaMask Wallet": "step1.md",
    "Step 2: Connect MetaMask to Base Network": "step2.md",
    "Step 3: Fund MetaMask Wallet with Base Tokens": "step3.md",
    "Step 4: Apply for Allowlist Access": "step4.md",
    "Step 5: Mint Releafs Tokens": "step5.md"
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_step = st.sidebar.radio("Choose a step:", list(steps.keys()))

# Display the selected step's content
st.header(selected_step)
content = load_step_content(steps[selected_step])
st.markdown(content)

# Confirmation buttons at the end of each step
if st.button("Confirm Completion"):
    st.success(f"You’ve completed {selected_step}. Proceed to the next step from the sidebar.")

# Final congratulations message when the last step is completed
if selected_step == "Step 5: Mint Releafs Tokens":
    st.balloons()
    st.write("""
    Congratulations on completing the Releafs setup! You’re now ready to mint and manage Releafs tokens.
    Remember to keep your MetaMask and recovery phrases secure.
    """)
