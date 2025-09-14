import streamlit as st

def app():
    # Page configuration
    st.set_page_config(page_title="USB-PCB Connector Design", layout="wide")

    # Custom CSS styles
    st.markdown("""
        <style>
            .stApp {
                background-image: url("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg");
                background-size: cover;
                background-attachment: fixed;
            }
            .stApp::before {
                content: "";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.9); /* White overlay */
                z-index: 0;
            }
            .block-container {
                position: relative;
                z-index: 1;
                color: #000000;
            }
            .custom-header {
                font-size: 2.8rem;
                font-weight: bold;
                text-align: center;
                margin-top: 2rem;
                margin-bottom: 2rem;
                color: #000000;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main content container
    with st.container():
        # Custom heading
        st.markdown('<div class="custom-header">KiCad Project Conclusion.</div>', unsafe_allow_html=True)

        # Title
        st.title("How I Designed a USB-PCB Connector Using KiCad 9, Conclusion")



        # =====================
        # Conclusion Section
        # =====================
        st.subheader("✅ 3D view of my USB-PCB Connector")
        st.markdown("""
       
        """)
        st.video("3d.mp4", start_time=0)

        
        st.markdown("<h1>KiCad<br><small>(Video Demonstration on what I've learnt so far about KiCad)</small></h1>", unsafe_allow_html=True)
        st.subheader("🎥 Video Demonstration Part 1")
        st.video("pt1.MOV", start_time=0)
        st.markdown("---")
        st.subheader("🎥 Video Demonstration Part 2")
        st.video("pt2.MOv", start_time=0)

        st.markdown('</div>', unsafe_allow_html=True)

        # ========================
        # Media Section (Images/Video)
        # ========================
        
# Run the app
app()
