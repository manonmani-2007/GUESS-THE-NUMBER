
import streamlit as st
import random
st.write("reloaded")
st.set_page_config(page_title="Guess The Number", page_icon="🎯")
st.title("🎯 Guess The Number Game")
st.sidebar.header("🎯Difficulty Level")
difficulty=st.sidebar.radio("Choose Level:",["🟢Easy","🟡Medium","🔴Hard"])
if difficulty=="🟢Easy":
    max_range=50
    value=15
elif difficulty=="🟡Medium":
    max_range=100
    value=10
else:
    max_range=200
    value=7
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, max_range)
    st.session_state.attempts = 0
    st.session_state.max_attempts=value
    st.session_state.game_over=False
if st.session_state.max_attempts!=value:
     st.session_state.max_attempts=value
     st.session_state.secret=random.randint(1,max_range)
     st.session_state.attempts=0
     st.session_state.game_over=False
if "score" not in st.session_state:
    st.session_state.score=100
if "attempts" not in st.session_state:
    st.session_state.attempts=0
if "game_over" not in st.session_state:
    st.session_state.game_over=False
st.sidebar.header("🎮Game Info")
st.sidebar.write("Guess the Secret Number👀")
st.sidebar.write(f"Range 1-{max_range}")
st.sidebar.write(f"MAximum Attempts:{st.session_state.max_attempts}")
st.write(f"I have chosen a number between 1 and {max_range}")
left=st.session_state.max_attempts-st.session_state.attempts
st.info(f"⌛Attempts Left:{left}")
st.info(f"⭐Score:{st.session_state.score}")
c1,c2,c3=st.columns([1,2,1])
with c2:
    guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=max_range,
    step=1
)
    
    
    if st.button("🎲 Guess",use_container_width=True) and not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.secret:
            st.warning("🔽 Too low")
            st.session_state.score-=10
        elif guess > st.session_state.secret:
            st.warning("🔼 Too high")
            st.session_state.score-=10
        else:
            st.success(f"🎉 Correct! Final Score:{st.session_state}")
            st.write(f"You guessed it in {st.session_state.attempts} attempts")
            st.balloons()
            st.session_state.game_over=True
        if st.session_state.attempts>st.session_state.max_attempts and not st.session_state.game_over:
            st.error("😓Maximum Attempts Reached")
            st.write(f"The secret number was {st.session_state.secret}")
            st.session_state.game_over=True 
    st.divider()
    if st.button("🔄️ Restart Game"):
        del st.session_state.secret
        st.rerun()
        st.success("New Game Restarted!🎮")
    
