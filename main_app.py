import gradio as gr
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoConfig,
    pipeline,
)
import torch
from translator import translate_text  # импортируем функцию переводчика


model_name = "sagard21/python-code-explainer"
tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name)

if torch.cuda.is_available():
    model = model.to('cuda')  # запускаем модель на GPU, если доступно
model.eval()

pipe = pipeline("summarization", model=model_name, config=config, tokenizer=tokenizer)


def generate_text(text_prompt):
    response = pipe(text_prompt)
    english_explanation = response[0]['summary_text']
    russian_explanation = translate_text(english_explanation)  # переводим объяснение кода с англ на рус язык
    return english_explanation, russian_explanation


textbox1 = gr.Textbox(value="""
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack""")
textbox2 = gr.Textbox()
textbox3 = gr.Textbox()

if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Interface(fn=generate_text, inputs=textbox1, outputs=[textbox2, textbox3])
    demo.launch()  # запускаем Gradio-интерфейс
