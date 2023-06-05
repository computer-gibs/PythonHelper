from transformers import FSMTForConditionalGeneration, FSMTTokenizer

MODEL_NAME = "facebook/wmt19-en-ru"

# инициализируем токенизатор
tokenizer = FSMTTokenizer.from_pretrained(MODEL_NAME)

# инициализируем модель для генерации условий
model = FSMTForConditionalGeneration.from_pretrained(MODEL_NAME)


# определяем функцию для перевода текста
def translate_text(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded
