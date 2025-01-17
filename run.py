from fastapi import FastAPI
import gradio as gr

from app import app

runapp=FastAPI()

runapp=gr.mount_gradio_app(runapp,app,path='/')