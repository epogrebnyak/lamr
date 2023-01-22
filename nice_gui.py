"""NiceGUI, our open-source library for building web-based user interfaces, 
continues to thrive. With NiceGUI, you can focus on writing Python code 
while the web development details are handled behind the scenes. 
This makes it ideal for a wide range of projects including short scripts, 
dashboards, robotics projects, IoT solutions, smart home automation, 
and machine learning.

Of course there are valid use cases for splitting frontend and backend 
technologies. NiceGUI is for those who don’t want to leave the Python
ecosystem and like to reap the benefits of having all code in one place. 
There are other options like Streamlit, Dash, Anvil, JustPy, and Pynecone.

https://www.reddit.com/r/Python/comments/10d6ugv/nicegui_let_any_browser_be_the_frontend_for_your/
"""

from nicegui import ui

ui.label("Hello NiceGUI!")
ui.button("BUTTON", on_click=lambda: ui.notify("button was pressed"))

ui.run()
