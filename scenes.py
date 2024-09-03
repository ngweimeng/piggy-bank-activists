import streamlit as st
from streamlit_extras.stoggle import stoggle
import time
import random

###############################################
#
#               1st Scene: Budgeting
#
################################################

def introScene():

    st.header("Budgeting 101")

    # Update Metrics
    if st.session_state.player_career == "Doctor":
        st.session_state["debt"] = 300
    elif st.session_state.player_career == "Technician":
        st.session_state["debt"] = 0
    elif st.session_state.player_career == "Teacher":
        st.session_state["debt"] = 75

    # possible actions
    actions = ["Option 1", "Option 2", "Option 3"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("images/budget.webp", caption="Did you know? In 2023, the median gross monthly salary for fresh university graduates in Singapore is $4,313.")
    with col2:
        st.markdown(
                f"""
                <div class='container'>
                    <p>Congratulations, {st.session_state.player_name}! You've just graduated and received your first paycheck!</p>
                    <p>But now, reality sets in—you realize no one has ever taught you how to manage your finances. After some research, you discover that the most important step after getting your salary is to allocate it between Expenditure, Savings, and Investment.</p>
                    <p>How would you like to allocate your first paycheck?</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('''
    Here are three options for you to consider:
- Option 1: 70% Expenses, 0% Investment, 30% Savings
- Option 2: 65% Expenses, 15% Investment, 20% Savings
- Option 3: 50% Expenses, 30% Investment, 20% Savings

***Note: Investments offer a **10% return on investment per round.***

''')
    st.divider()
    # Create the selectbox
    selected_action = st.selectbox("Select an action:", actions, placeholder="Choose an option", on_change=None, index=None)
    # Immediately display the selected action
    st.write(f"You chose to: {selected_action}")

    # Create the button for confirmation
    if st.button("Confirm Action"):
        st.write(f"Action confirmed: {selected_action}")

        if selected_action == "Option 1":
            st.session_state.player_budget = 1
            st.session_state["counter"] += 1
            st.session_state.place = "insuranceScene"  # Moving our character to next scene
            st.rerun()  

        if selected_action == "Option 2":
            st.session_state.player_budget = 2
            st.session_state["counter"] += 1
            st.session_state.place = "insuranceScene"
            st.rerun()
        
        if selected_action == "Option 3":
            st.session_state.player_budget = 3
            st.session_state["counter"] += 1
            st.session_state.place = "insuranceScene"  # Moving our character to next scene
            st.rerun()

###############################################
#
#               Buy Insurance Scene     
#
################################################

def insuranceScene():

    st.header("For a rainy day")

    # possible actions
    actions = ["Buy Insurance", "No Insurance"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("images/insurance.webp", caption="Did you know? In Singapore, there's a type of insurance called 'Critical Illness Insurance' that covers more than 30 different serious illnesses! This crucial safety net can protect your financial future when life takes an unexpected turn!")
    with col2:
        st.markdown(
            f"""
            <div class='container'>
                <p>As you embark on your financial journey, you're faced with another important decision: Should you buy insurance?</p>
                <p>Insurance can provide you with a safety net, protecting you against unexpected events like accidents, illnesses, or other unforeseen circumstances. However, it also comes with a cost that will affect your monthly budget. Consider your financial goals and current situation carefully before making a decision.</p>
                <p>What will you choose?</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('''
    Here are two options for you to consider:
- Option 1: Buy Insurance
- Option 2: No Insurance

***Note: Choosing to buy insurance will increase your debt by 100. However, it can safeguard you against unexpected events that could potentially deplete your cash reserves.***
''')
    st.divider()
    # Create the selectbox
    selected_action = st.selectbox("Select an action:", actions, placeholder="Choose an option", on_change=None, index=None)

    # Immediately display the selected action
    st.write(f"You chose to: {selected_action}")

    # Create the button for confirmation
    if st.button("Confirm Action"):
        st.write(f"Action confirmed: {selected_action}")

        if selected_action == "Buy Insurance":
            st.session_state.player_insurance = 1
            st.session_state["counter"] += 1
            st.session_state["debt"] += 50
            st.session_state.place = "bonusScene"  # Moving our character to other scene
            st.rerun()  

        if selected_action == "No Insurance":
            st.session_state.player_insurance = 0
            st.session_state["counter"] += 1
            st.session_state.place = "bonusScene"
            st.rerun()

###############################################
#
#               Bonus Scene
#
################################################

def bonusScene():

    st.header("It is your lucky day!")

    # Possible actions
    actions = ["Save", "Invest", "Spend"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("images/bonus.webp", caption="Did you know? Many Singaporeans receive an annual bonus, often referred to as the '13th-month bonus'! How you choose to use this extra money can have a big impact on your financial future.")
    with col2:
        st.markdown(
            f"""
            <div class='container'>
                <p>Congratulations, {st.session_state.player_name}! You've just received your annual bonus—a reward for all your hard work over the past year.</p>
                <p>Now comes the important question: What should you do with this extra money? You have three options:</p>
                <ul>
                    <li><strong>Save</strong>: Put the money into your savings for a rainy day or a future goal.</li>
                    <li><strong>Invest</strong>: Grow your wealth by investing in stocks, bonds, or other assets.</li>
                    <li><strong>Spend</strong>: Treat yourself or your loved ones, but remember, once it's spent, it's gone!</li>
                </ul>
                <p>Each choice has its own benefits and risks. Think about your current financial situation and your long-term goals before making a decision. What will you do with your bonus?</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('''
    Here are three options for you to consider:
- Option 1: Save. Your cash will increase by 100.
- Option 2: Invest. Your investments will increase by 100.
- Option 3: Spend. Your expenses will increase by 100.

***Note: Investments offer a **10% return on investment per round.***''')
    st.divider()
    # Create the selectbox
    selected_action = st.selectbox("Select an action:", actions, placeholder="Choose an option", index=None)

    # Immediately display the selected action
    st.write(f"You chose to: {selected_action}")

    # Create the button for confirmation
    if st.button("Confirm Action"):
        st.write(f"Action confirmed: {selected_action}")

        if selected_action == "Save":
            st.session_state["cash"] += 100
            st.session_state["counter"] += 1
            st.session_state.place = "houseScene"  # Moving our character to other scene
            st.rerun()  

        if selected_action == "Invest":
            st.session_state["investments"] += 100
            st.session_state["counter"] += 1
            st.session_state.place = "houseScene"
            st.rerun()

        if selected_action == "Spend":
            st.session_state["expenses"] += 100
            st.session_state["counter"] += 1
            st.session_state.place = "houseScene"
            st.rerun()

###############################################
#
#               House Scene
#
################################################

def houseScene():

    st.header("Say the famous 3 letters...BTO")

    # Possible actions
    actions = ["Condo", "BTO", "Rent"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("images/house.webp", caption="Did you know? In Singapore, around 78.7% of the population live in HDB (Housing & Development Board) flats, which are government-subsidized homes. About 16% of residents live in private housing, such as condominiums or landed properties, while the remaining 5.3% live in other types of housing, including rental apartments.")
    with col2:
        st.markdown(
            f"""
            <div class='container'>
                <p>Congratulations, {st.session_state.player_name}! You're now at a major crossroads in your financial journey: choosing your first home.</p>
                <p>In Singapore, you have three main options:</p>
                <ul>
                    <li><strong>Buy a Private Condo</strong>: Enjoy luxurious living, but it comes with a hefty price tag and higher mortgage payments.</li>
                    <li><strong>Apply for a BTO (Build-To-Order) Flat</strong>: A more affordable option with government subsidies, but be prepared for a waiting period before your flat is ready.</li>
                    <li><strong>Rent Forever</strong>: Flexibility and no long-term commitment, but you won’t build any equity or have a place to call your own.</li>
                </ul>
                <p>Each choice has significant financial implications. Consider your budget, long-term goals, and lifestyle preferences carefully before making a decision. What will your first home be?</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    st.markdown('''
    Here are three options for you to consider:
- Option 1: Buy a Private Condo. Debt +200, Cash -50 per round, Investment +500
- Option 2: Apply for a BTO. Debt +100, Cash -20 per round, Investment +200
- Option 3: Rent Forever. No debt, Cash -20 per round

***Note: Buying a home is a major financial decision. Consider not just the immediate costs, but also the long-term benefits and trade-offs.***''')
    st.divider()
    # Create the selectbox
    selected_action = st.selectbox("Select an action:", actions, placeholder="Choose an option", index=None)

    # Immediately display the selected action
    st.write(f"You chose to: {selected_action}")

    # Create the button for confirmation
    if st.button("Confirm Action"):
        st.write(f"Action confirmed: {selected_action}")

        if selected_action == "Condo":
            st.session_state["debt"] += 200
            st.session_state["cash"] -= 50
            st.session_state["investments"] += 500
            st.session_state["counter"] += 1
            st.session_state.place = "endScene"  # Moving our character to other scene
            st.rerun()  

        if selected_action == "Invest":
            st.session_state["debt"] += 100
            st.session_state["cash"] -= 20
            st.session_state["investments"] += 200
            st.session_state["counter"] += 1
            st.session_state.place = "endScene"
            st.rerun()

        if selected_action == "Spend":
            st.session_state["cash"] -= 20
            st.session_state["counter"] += 1
            st.session_state.place = "endScene"
            st.rerun()


###############################################
#
#               unexpected Scene
#
################################################

def unexpectScene():
    st.header("Investment Scene. WIP")

###############################################
#
#               End Scene
#
################################################

def endScene():

    st.header("You made it!")

    # Possible actions
    actions = ["Condo", "BTO", "Rent"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image("images/end.webp", caption="Did you know? In Singapore, the average retirement age has gradually increased over the years, with most Singaporeans planning to retire around the age of 65. The Central Provident Fund (CPF) plays a crucial role in retirement planning, helping citizens build a nest egg for their golden years.")
    with col2:
        st.markdown(
        f"""
        <div class='container'>
            <p>Congratulations, {st.session_state.player_name}! You've reached the end of your financial journey and it's time to reflect on your financial health as you approach retirement.</p>
            <p>Let's review the key aspects of your financial status:</p>
            <ul>
                <li><strong>Expenses:</strong> Track how much you've been spending. Have you managed to keep your expenses in check, or have they been eating into your savings?</li>
                <li><strong>Cash:</strong> This is your available liquid cash. It's important to ensure you have enough to cover your short-term needs without dipping into your investments or incurring more debt.</li>
                <li><strong>Debt:</strong> Take stock of any debts you've accumulated. Reducing debt before retirement is crucial for a stress-free financial future.</li>
                <li><strong>Investments:</strong> Your investments represent your long-term financial security. A well-balanced investment portfolio can help sustain you through retirement.</li>
            </ul>
            <p>As you move into retirement, consider how these metrics align with your goals. Do you have a solid plan to manage your expenses, reduce debt, and grow your investments? It's important to make sure that your financial decisions support a comfortable and secure retirement.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )