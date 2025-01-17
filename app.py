import gradio as gr
import pandas as pd
import os
import pathlib


APP_PATH = str(pathlib.Path(__file__).parent.resolve())
items_df=pd.read_excel(os.path.join(APP_PATH, os.path.join("data", "Itemnumbers.xlsx")))
lines=items_df['Line'].unique().tolist()

def line_change(line,machine):
    
    machines=items_df[items_df["Line"]==line]["Machines"].tolist()
    #print(machines)
    return gr.Dropdown(choices=machines)
name=[""]
def machine_change(machine,itemnumber):
    
    machines=items_df[items_df["Machines"]==machine]["Item No"].tolist()
    name.insert(1,machines[0])
    
    return name[1]
    
def submit_fun(line,machine):
    if line==None:
        raise gr.Error("Line is Not selected")
    elif machine==None:
        raise gr.Error("Machine is Not selected")

        


with gr.Blocks(theme=gr.themes.Citrus(font=[gr.themes.GoogleFont("Ubuntu"), "Arial" ,"sans-serif"]),title="SEG-TEF",) as app:
    gr.Label("Breakdown Log",container=False,color="teal")
    line = gr.Dropdown(choices=lines,label="Select Line")
    machine= gr.Dropdown(label="Select Machine")
    itemnumber= gr.Textbox(label="Select Machine",)
    natureofbreakdown=gr.Textbox(label="Nature of breakdown")
    submit=gr.Button("Submit")
    gr.ClearButton(components=[line,machine,itemnumber],value='clear')
    status_label=gr.Label("",container=False)
   
    submit.click(fn=submit_fun, inputs=[line,machine], outputs=[])

    line.change(fn=line_change, inputs=[line,machine], outputs=[machine])
    machine.change(fn=machine_change, inputs=[machine,itemnumber], outputs=[itemnumber])

    
   
    app.launch(debug=True)