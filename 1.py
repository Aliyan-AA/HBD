import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import random

# Set page configuration with a festive theme
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Pacifico&display=swap');
    
    .main-header {
        font-family: 'Dancing Script', cursive;
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(to right, #FF4B91, #FF9EAA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    
    .sub-header {
        font-family: 'Pacifico', cursive;
        font-size: 2rem;
        font-weight: 600;
        color: #9747FF;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .message {
        font-size: 1.3rem;
        line-height: 1.6;
        color: #333;
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 158, 170, 0.3);
        margin-bottom: 30px;
    }
    
    .heart {
        display: inline-block;
        color: #FF4B91;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    @keyframes heartbeat {
        0% { transform: scale(1); }
        25% { transform: scale(1.1); }
        50% { transform: scale(1); }
        75% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    .sparkle {
        display: inline-block;
        animation: sparkle 1.5s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0% { opacity: 0.4; }
        50% { opacity: 1; }
        100% { opacity: 0.4; }
    }
    
    .sticker {
        display: inline-block;
        font-size: 3rem;
        margin: 10px;
        animation: spin 3s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .floating-balloon {
        position: absolute;
        animation-name: float-balloon;
        animation-timing-function: ease-in-out;
        animation-iteration-count: infinite;
        font-size: 2rem;
    }
    
    @keyframes float-balloon {
        0% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0); }
    }
    
    .btn-special {
        background-image: linear-gradient(to right, #FF4B91, #FF9EAA);
        color: white;
        padding: 12px 24px;
        border-radius: 50px;
        border: none;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 75, 145, 0.4);
        transition: all 0.3s ease;
        display: block;
        width: 100%;
        text-align: center;
        margin: 20px auto;
        text-decoration: none;
    }
    
    .btn-special:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 15px rgba(255, 75, 145, 0.6);
    }
    
    .memories-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        margin-top: 30px;
    }
    
    .memory-card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        width: 250px;
        max-width: 100%;
    }
    
    .memory-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .memory-content {
        padding: 15px;
    }
    
    .memory-title {
        font-weight: bold;
        margin-bottom: 5px;
        color: #333;
    }
    
    .memory-date {
        font-size: 0.8rem;
        color: #777;
        margin-bottom: 10px;
    }
    
    .memory-text {
        color: #444;
        font-size: 0.9rem;
    }
    
    .birthday-gift {
        width: 100%;
        max-width: 400px;
        height: 300px;
        background: linear-gradient(to bottom right, #FF4B91, #FF9EAA);
        border-radius: 10px;
        margin: 0 auto;
        position: relative;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    
    .birthday-gift:hover {
        transform: scale(1.05);
    }
    
    .gift-lid {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 30%;
        background: #FF9EAA;
        border-radius: 10px 10px 0 0;
        z-index: 2;
        transition: all 0.5s ease;
    }
    
    .gift-bow {
        position: absolute;
        top: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 60px;
        background: #FF4B91;
        z-index: 3;
        border-radius: 50%;
    }
    
    .birthday-gift.opened .gift-lid {
        top: -60%;
        transform: rotateZ(-20deg);
    }
    
    .gift-message {
        font-family: 'Dancing Script', cursive;
        font-size: 1.8rem;
        color: white;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        opacity: 0;
        transition: opacity 0.5s ease 0.3s;
    }
    
    .birthday-gift.opened .gift-message {
        opacity: 1;
    }
    
    /* Confetti animation */
    .confetti {
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: #f2d74e;
        opacity: 0;
        animation: confetti-fall 3s ease-in infinite;
    }
    
    @keyframes confetti-fall {
        0% {
            transform: translateY(-100px) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(1000px) rotate(720deg);
            opacity: 0;
        }
    }
    
    .container-3d {
        perspective: 1000px;
        margin: 50px auto;
        width: 100%;
        max-width: 800px;
    }
    
    .cake-3d {
        width: 100%;
        height: 400px;
        position: relative;
        transform-style: preserve-3d;
        animation: rotate-cake 15s linear infinite;
    }
    
    @keyframes rotate-cake {
        0% { transform: rotateY(0deg); }
        100% { transform: rotateY(360deg); }
    }
</style>
""", unsafe_allow_html=True)

# Create some floating balloons at random positions
balloons = ["🎈", "🎁", "🎊", "✨", "🎉"]
for i in range(10):
    left_pos = random.randint(5, 95)
    delay = random.randint(1, 5)
    duration = random.uniform(3, 6)
    balloon = random.choice(balloons)
    
    st.markdown(f"""
    <div class="floating-balloon" style="left: {left_pos}%; animation-duration: {duration}s; animation-delay: {delay}s;">
        {balloon}
    </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown(f'<h1 class="main-header">Happy Birthday!</h1>', unsafe_allow_html=True)

# Column layout for message and 3D cake
col1, col2 = st.columns([1, 1])

with col1:
    # Display personalized birthday message
    st.markdown('<h2 class="sub-header">To My Wonderful Wife</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="message">
        <p>On this special day, I want to celebrate the amazing person you are.</p>
        <p>Your smile brightens my days, your love strengthens my heart, and your presence makes life beautiful.</p>
        <p>Thank you for being my partner, my best friend, and the love of my life.</p>
        <p>Wishing you a day filled with joy, laughter, and all the things that make you happy!</p>
        <p>With all my love,</p>
        <p>Your Husband <span class="heart">❤️</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Memory cards
    st.markdown('<h2 class="sub-header">Our Special Memories</h2>', unsafe_allow_html=True)
    
    # Create a layout for memory cards
    memory_col1, memory_col2 = st.columns(2)
    
    with memory_col1:
        st.markdown("""
        <div class="memory-card">
            <div class="memory-content">
                <div class="memory-title">Our First Date</div>
                <div class="memory-date">That wonderful beginning</div>
                <div class="memory-text">Remember how we laughed the whole evening? That's when I knew you were special.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="memory-card">
            <div class="memory-content">
                <div class="memory-title">That Summer Vacation</div>
                <div class="memory-date">Sun, sand, and smiles</div>
                <div class="memory-text">Walking on the beach at sunset, making plans for our future together.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with memory_col2:
        st.markdown("""
        <div class="memory-card">
            <div class="memory-content">
                <div class="memory-title">Our Wedding Day</div>
                <div class="memory-date">The day we said "I do"</div>
                <div class="memory-text">You've never looked more beautiful than the moment you walked down the aisle.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="memory-card">
            <div class="memory-content">
                <div class="memory-title">Last Year's Birthday</div>
                <div class="memory-date">Another year of joy</div>
                <div class="memory-text">Celebrating you is always my favorite occasion. Here's to another amazing year!</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    # 3D Birthday Cake using Plotly
    st.markdown('<h2 class="sub-header">A Special 3D Birthday Cake</h2>', unsafe_allow_html=True)
    
    # Create 3D cake using Plotly
    def create_3d_cake():
        # Base layer of the cake
        u = np.linspace(0, 2*np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x = 1 * np.outer(np.cos(u), np.sin(v))
        y = 1 * np.outer(np.sin(u), np.sin(v))
        z = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v)) - 0.5  # Bottom layer
        
        cake_bottom = go.Surface(
            x=x*1.5, y=y*1.5, z=z*0.5, 
            colorscale=[[0, '#FF9EAA'], [1, '#FF4B91']], 
            opacity=0.9,
            showscale=False
        )
        
        # Middle layer
        z2 = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v)) + 0.25
        cake_middle = go.Surface(
            x=x*1.2, y=y*1.2, z=z2*0.5, 
            colorscale=[[0, '#F8C8DC'], [1, '#FFACC7']], 
            opacity=0.9,
            showscale=False
        )
        
        # Top layer
        z3 = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v)) + 1
        cake_top = go.Surface(
            x=x*0.8, y=y*0.8, z=z3*0.5, 
            colorscale=[[0, '#FFCAD4'], [1, '#FFAFC5']], 
            opacity=0.9,
            showscale=False
        )
        
        # Candles (create multiple candles)
        candle_positions = [
            (0.5, 0, 1.4), (-0.5, 0, 1.4), (0, 0.5, 1.4), (0, -0.5, 1.4), (0, 0, 1.6)
        ]
        
        candles = []
        flames = []
        
        for i, (cx, cy, cz) in enumerate(candle_positions):
            # Candle
            candle_z = np.linspace(1.2, cz, 20)
            candle_x = np.full_like(candle_z, cx)
            candle_y = np.full_like(candle_z, cy)
            
            candles.append(go.Scatter3d(
                x=candle_x, y=candle_y, z=candle_z,
                mode='lines',
                line=dict(color='#FFF8D6', width=8),
                showlegend=False
            ))
            
            # Flame
            flame_r = 0.1
            flame_theta = np.linspace(0, 2*np.pi, 20)
            flame_height = 0.15
            
            for h in np.linspace(0, flame_height, 10):
                r = flame_r * (1 - h/flame_height)
                flame_x = cx + r * np.cos(flame_theta)
                flame_y = cy + r * np.sin(flame_theta)
                flame_z = np.full_like(flame_theta, cz + h)
                
                flames.append(go.Scatter3d(
                    x=flame_x, y=flame_y, z=flame_z,
                    mode='lines',
                    line=dict(color='#FFCC33', width=5),
                    showlegend=False
                ))
        
        # Create the figure
        fig = go.Figure(data=[cake_bottom, cake_middle, cake_top] + candles + flames)
        
        # Add "Happy Birthday" text floating above the cake
        text_points = []
        text = "Happy Birthday!"
        text_radius = 1.6
        text_height = 2.0
        text_offset = len(text) / 2 * 0.2  # Adjust based on text length
        
        for i, char in enumerate(text):
            angle = 2 * np.pi * i / len(text) - np.pi / 2
            text_points.append(
                go.Scatter3d(
                    x=[text_radius * np.cos(angle)],
                    y=[text_radius * np.sin(angle)],
                    z=[text_height],
                    mode='text',
                    text=[char],
                    textposition='middle center',
                    textfont=dict(
                        size=18,
                        color='#FF4B91'
                    ),
                    showlegend=False
                )
            )
        
        fig.add_traces(text_points)
        
        # Update layout
        fig.update_layout(
            title="",
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
                aspectmode='manual',
                aspectratio=dict(x=1, y=1, z=0.8)
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            height=500,
            width=600
        )
        
        return fig
    
    # Display 3D cake
    cake_fig = create_3d_cake()
    st.plotly_chart(cake_fig, use_container_width=True)
    
    # Special gift animation
    st.markdown('<h2 class="sub-header">A Special Gift</h2>', unsafe_allow_html=True)
    
    # Interactive gift
    gift_placeholder = st.empty()
    
    if st.button("Open Your Gift 🎁", use_container_width=True):
        # Show the open gift
        gift_placeholder.markdown("""
        <div class="birthday-gift opened">
            <div class="gift-lid"></div>
            <div class="gift-bow"></div>
            <div class="gift-message">I love you!</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add confetti
        for i in range(10):
            left = random.randint(0, 100)
            duration = random.uniform(3, 6)
            delay = random.uniform(0, 2)
            size = random.randint(5, 15)
            color = random.choice(['#f2d74e', '#FF4B91', '#9747FF', '#95BDFF', '#FF9EAA'])
            
            st.markdown(f"""
            <div class="confetti" style="left: {left}%; animation-duration: {duration}s; animation-delay: {delay}s; width: {size}px; height: {size}px; background-color: {color};"></div>
            """, unsafe_allow_html=True)
        
        # Show birthday message
        st.balloons()
        st.markdown("""
        <div style="text-align: center; margin-top: 30px; font-family: 'Dancing Script', cursive; font-size: 2rem; color: #FF4B91;">
            Wishing you the happiest birthday ever!
        </div>
        """, unsafe_allow_html=True)
    else:
        # Show the closed gift
        gift_placeholder.markdown("""
        <div class="birthday-gift">
            <div class="gift-lid"></div>
            <div class="gift-bow"></div>
            <div class="gift-message">I love you!</div>
        </div>
        """, unsafe_allow_html=True)

# Create a 3D visualization of birthday celebration data
st.markdown('<h2 class="sub-header">Special Birthday Celebration in 3D</h2>', unsafe_allow_html=True)

# Generate some birthday-themed data
years = list(range(2010, 2026))
happiness = [random.uniform(7, 10) for _ in range(len(years))]
gifts = [random.randint(3, 10) for _ in range(len(years))]
celebrations = [random.randint(1, 5) for _ in range(len(years))]

# Create an interactive 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=years,
    y=happiness,
    z=gifts,
    mode='markers',
    marker=dict(
        size=celebrations,
        sizemode='diameter',
        sizeref=0.25,
        sizemin=5,
        color=happiness,
        colorscale='Plasma',
        opacity=0.8,
        colorbar=dict(title="Happiness Level"),
        symbol='circle',
        line=dict(color='rgb(204, 204, 204)', width=1)
    ),
    text=[f"Year: {y}<br>Happiness: {h:.1f}<br>Gifts: {g}<br>Celebrations: {c}" 
          for y, h, g, c in zip(years, happiness, gifts, celebrations)],
    hoverinfo='text'
)])

# Update the layout with a love theme
fig.update_layout(
    title="Our Birthday Celebrations Through the Years",
    scene=dict(
        xaxis=dict(title="Year"),
        yaxis=dict(title="Happiness Level"),
        zaxis=dict(title="Number of Gifts"),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    height=600,
)

st.plotly_chart(fig, use_container_width=True)

# Birthday wishes animation
st.markdown('<h2 class="sub-header">Birthday Wishes</h2>', unsafe_allow_html=True)

wishes = [
    "May your day be as wonderful as you are!",
    "Wishing you health, love, and happiness!",
    "May all your dreams come true!",
    "Here's to another year of beautiful moments!",
    "Celebrating the amazing person you are!",
    "May your day be filled with love and laughter!",
    "You deserve all the happiness in the world!",
    "Thank you for being you. Happy Birthday!",
    "Here's to celebrating you today and always!"
]

wish_placeholder = st.empty()

# Show all wishes at once
if st.button("See Birthday Wishes 💫", use_container_width=True):
    wishes_html = ""
    for wish in wishes:
        wishes_html += f"""
        <div style="text-align: center; margin: 20px 0; padding: 20px; background: linear-gradient(45deg, rgba(255,75,145,0.1), rgba(255,158,170,0.1)); border-radius: 10px; transition: all 0.5s ease;">
            <span style="font-size: 1.4rem; font-family: 'Pacifico', cursive; color: #9747FF;">
                {wish} <span class="sparkle">✨</span>
            </span>
        </div>
        """
    
    wish_placeholder.markdown(wishes_html, unsafe_allow_html=True)

# Add floating emoji stickers
st.markdown("""
<div style="text-align: center; margin: 40px 0;">
    <span class="sticker">🎂</span>
    <span class="sticker">🎁</span>
    <span class="sticker">🎈</span>
    <span class="sticker">🎉</span>
    <span class="sticker">❤️</span>
</div>
""", unsafe_allow_html=True)

# Footer with love message
st.markdown("""
<div style="text-align: center; margin-top: 60px; margin-bottom: 40px; font-family: 'Dancing Script', cursive; font-size: 2rem;">
    With all my love, today and always...
</div>
""", unsafe_allow_html=True)