---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: > 
    def preprocess(text: str) -> str:
        text = str(text)
        text = text.replace('\\n', ' ')
        tokenized_text = text.split(' ')
        preprocessed_text = " ".join([token for token in tokenized_text if token])

        return preprocessed_text
datasets:
- sagard21/autotrain-data-code-explainer
co2_eq_emissions:
  emissions: 5.393079045128973
license: mit
pipeline_tag: summarization
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 2745581349
- CO2 Emissions (in grams): 5.3931

# Model Description

This model is an attempt to simplify code understanding by generating line by line explanation of a source code. This model was fine-tuned using the Salesforce/codet5-large model. Currently it is trained on a small subset of Python snippets.

# Model Usage

```py
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoConfig,
    pipeline,
)

model_name = "sagard21/python-code-explainer"

tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

config = AutoConfig.from_pretrained(model_name)

model.eval()

pipe = pipeline("summarization", model=model_name, config=config, tokenizer=tokenizer)

raw_code = """
def preprocess(text: str) -> str:
    text = str(text)
    text = text.replace("\n", " ")
    tokenized_text = text.split(" ")
    preprocessed_text = " ".join([token for token in tokenized_text if token])

    return preprocessed_text
"""

print(pipe(raw_code)[0]["summary_text"])

```

## Validation Metrics

- Loss: 2.156
- Rouge1: 29.375
- Rouge2: 18.128
- RougeL: 25.445
- RougeLsum: 28.084
- Gen Len: 19.000
