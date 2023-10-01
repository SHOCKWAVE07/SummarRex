import gradio as gr
from chatbot.interface import launch_interface
from chatbot.roles import roles, role_selected

if __name__ == "__main__":
    launch_interface(roles, role_selected)
