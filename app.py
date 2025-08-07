import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit Page Setup
st.set_page_config(page_title="WiCSADA - Wireless Channel Simulator", layout="centered")

# Title and Description
st.title("📡 WiCSADA - Wireless Channel Simulator and Diversity Analyzer")
st.markdown("""
This tool demonstrates basic wireless channel behaviors and performance:
- **AWGN Channel**
- **Rayleigh Fading**
- **2x2 MIMO Capacity Estimation**
""")

# Sidebar - Channel Selection
st.sidebar.header("Simulation Controls")
channel_type = st.sidebar.selectbox("Select Channel Type", ["AWGN", "Rayleigh Fading", "MIMO (2x2)"])
snr_db = st.sidebar.slider("SNR (dB)", 0, 30, 10)

# Function: AWGN Channel
def simulate_awgn(snr_db):
    snr_linear = 10 ** (snr_db / 10)
    N = 1000
    x = np.ones(N)
    noise = np.random.randn(N) / np.sqrt(snr_linear)
    y = x + noise
    fig, ax = plt.subplots()
    ax.plot(y, label="Received Signal")
    ax.set_title(f"AWGN Channel Output (SNR = {snr_db} dB)")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    ax.legend()
    return fig

# Function: Rayleigh Fading
def simulate_rayleigh():
    N = 1000
    h = (np.random.randn(N) + 1j * np.random.randn(N)) / np.sqrt(2)
    fig, ax = plt.subplots()
    ax.plot(np.abs(h), label="Rayleigh Envelope")
    ax.set_title("Rayleigh Fading Envelope")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    ax.legend()
    return fig

# Function: 2x2 MIMO Capacity
def simulate_mimo_2x2(snr_db):
    snr_linear = 10 ** (snr_db / 10)
    H = (np.random.randn(2, 2) + 1j * np.random.randn(2, 2)) / np.sqrt(2)  # 2x2 Rayleigh channel
    U, S, Vh = np.linalg.svd(H)
    capacity = np.sum(np.log2(1 + (snr_linear / 2) * (S**2))).real

    fig, ax = plt.subplots()
    ax.bar(["Stream 1", "Stream 2"], (np.log2(1 + (snr_linear / 2) * (S**2))).real)
    ax.set_title(f"2x2 MIMO Channel Capacity ≈ {capacity:.2f} bits/s/Hz")
    ax.set_ylabel("Capacity (bits/s/Hz)")
    ax.grid(True)

    return fig

# Display based on selection
if channel_type == "AWGN":
    st.subheader("AWGN Channel Simulation")
    fig = simulate_awgn(snr_db)
    st.pyplot(fig)

elif channel_type == "Rayleigh Fading":
    st.subheader("Rayleigh Fading Channel Simulation")
    fig = simulate_rayleigh()
    st.pyplot(fig)

elif channel_type == "MIMO (2x2)":
    st.subheader("2x2 MIMO Channel Capacity Estimation")
    fig = simulate_mimo_2x2(snr_db)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Developed for **FI1926 - Advances in Wireless Communication**, Anna University ©")
