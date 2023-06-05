from transformers import FSMTForConditionalGeneration, FSMTTokenizer

MODEL_NAME = "facebook/wmt19-en-ru"
tokenizer = FSMTTokenizer.from_pretrained(MODEL_NAME)
model = FSMTForConditionalGeneration.from_pretrained(MODEL_NAME)


def translate_text(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded
