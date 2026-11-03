import streamlit as st

st.title("BCAS Login System")

# පාස්වර්ඩ් එක ටයිප් කරනකොට තරු (*) විදිහට පේන්න type="password" දාන්න
adminpass = st.text_input("Password", type="password")

if st.button("Login"):
  if adminpass == "bc123":
    st.success("✅ Login Successful! Click below to open the app:")
    # යූසර්ට ක්ලික් කරලා අර ඇප් එකට යන්න ලස්සන බටන් එකක් දෙනවා
    st.link_button(
        "🚀 Open Smart Class App", "smart-class-64k6m26ap9jxd5qtjdtadx"
    )

  elif adminpass == "":
    st.warning("⚠️ Please enter your password.")

  else:
    st.error("❌ Invalid Password. Please try again.")
