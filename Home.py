import streamlit as st
import random
from PIL import Image
import time
import urllib.request
import streamlit as st
import time

from streamlit.components.v1 import html


# Navigate to another page
# Called like an Event
def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


nameToImg = {'Michael Jackson' : 'https://pm1.aminoapps.com/6726/a81ade5179d30ca4362763a833066aec113fd436v2_hq.jpg',
             'The Rock' : 'https://i.pinimg.com/736x/93/09/d4/9309d424be1cb7a5a301f9c15a75ffd3.jpg',
             'Oprah' : 'https://deadline.com/wp-content/uploads/2020/04/oprah-winfrey.jpg',
             'Default' : 'https://abs.twimg.com/sticky/default_profile_images/default_profile_400x400.png'}

if 'character' not in st.session_state:
    st.session_state['character'] = 'Default'

placeholder = st.empty()
placeholder.image(nameToImg[st.session_state['character']], width=500)

col1, col2 = st.columns([.5,1])

with col1:
    st.session_state['character'] = st.selectbox(
        'Who am I?',
        ('Default', 'Michael Jackson', 'The Rock', 'Oprah'),
        placeholder='Default')

# atualiza imagem apos selectbox mudar valor
placeholder.image(nameToImg[st.session_state['character']], width=500)


with st.sidebar:
    st.image(nameToImg[st.session_state['character']])

with col2:
    if st.button(label="Fight!"):
        nav_page("Chat")

# html_string = """
#             <audio controls autoplay hidden="hidden">
#               <source src="https://www.orangefreesounds.com/wp-content/uploads/2022/04/Small-bell-ringing-short-sound-effect.mp3" type="audio/mp3">
#             </audio>
#             """

# sound = st.empty()
# sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
# time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
# sound.empty()  # optionally delete the element afterwards
