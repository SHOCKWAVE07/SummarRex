# interface.py
import gradio as gr
from chatbot.logic import CustomChatGPT


def launch_interface(roles, role_selected):
    iface = gr.Interface(
        fn=CustomChatGPT,
        inputs=[gr.Textbox(label="Enter Your Input"), gr.Dropdown(roles, default=role_selected, label="Select Your Role:")],
        outputs=gr.Textbox(),
        title="SummeRex(Personalized Chatbot)",
    )

    iface.launch()
