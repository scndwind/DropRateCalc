import streamlit as st
import random

# Function to simulate the drop based on the character type
def run_simulation(drop_rate, orb_count, gimme_chance, drop_chance, attempts, character):
    successful_drops = 0
    total_drops = 0
    probability = 0

    if character == "Divine Knight":
        # Divine Knight (Divine Knight): Adjust drop rate based on orb count
        effective_drop_rate = drop_rate + (orb_count / 100)  # Each 100 Orb Count adds 1x to the drop rate
        probability = 1 / drop_chance * effective_drop_rate  # Adjust probability with Orb Count
    elif character == "Void Walker":
        # Void Walker: Adjust based on Gimme-Gimme chance
        probability = 1 / drop_chance * drop_rate  # Base drop rate
    else:
        # Any other character, use regular drop rate
        probability = 1 / drop_chance * drop_rate  # Standard probability

    # Run the simulation for the specified number of attempts
    for attempt in range(attempts):
        if character == "Void Walker":
            if random.random() <= gimme_chance / 100:  # Gimme-Gimme triggers 2x drops
                if random.random() <= probability:
                    successful_drops += 1
                    total_drops += 2  # Gimme-Gimme gives 2 drops
            else:
                if random.random() <= probability:
                    successful_drops += 1
                    total_drops += 1  # Normal drop
        else:
            if random.random() <= probability:
                successful_drops += 1
                total_drops += 1  # Normal drop

    # Calculate actual chance
    actual_chance = (1 - (1 - probability) ** attempts) * 100

    # Return results
    return successful_drops, total_drops, actual_chance

# Streamlit user interface (UI)
st.title("Drop Rate Simulation")

# Inputs from the user
drop_rate = st.number_input("Enter Drop Rate (e.g., 11.76)", min_value=0.0, value=11.76)
character = st.selectbox("Choose your character", ["Divine Knight", "Void Walker", "Other"]).lower()

orb_count = 0
gimme_chance = 0
if character == "Divine Knight":
    orb_count = st.number_input("Orb Count", min_value=0, value=0)
elif character == "Void Walker":
    gimme_chance = st.number_input("Gimme-Gimme Chance %", min_value=0.0, max_value=100.0, value=56.0)

drop_chance = st.number_input("Drop Chance (e.g., 2000000 for 1/2000000)", min_value=1, value=2000000)
attempts = st.number_input("Enter Number of Attempts", min_value=1, value=100)

# Button to run the simulation
if st.button("Run Simulation"):
    successful_drops, total_drops, actual_chance = run_simulation(drop_rate, orb_count, gimme_chance, drop_chance, attempts, character)
    
    # Display the results
    st.write(f"Drop Rate: {drop_rate}x")
    if character == "Divine Knight":
        st.write(f"Orb Count: {orb_count}")
    elif character == "Void Walker":
        st.write(f"Gimme-Gimme Chance: {gimme_chance}%")
    st.write(f"Drop Chance: 1 in {drop_chance:,}")
    st.write(f"Attempts: {attempts:,}")
    st.write(f"\nOut of {attempts:,} attempts, you got {successful_drops} successful attempts.")
    st.write(f"Total drops: {total_drops}")
    st.write(f"Actual chance: {actual_chance:.2f}%")
