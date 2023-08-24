import gradio as gr
import onnxruntime as rt
from transformers import AutoTokenizer
import torch, json

with open("tag_types_encoded.json", "r") as fp:
  encode_tag_types = json.load(fp)

tags = list(encode_tag_types.keys())

tokenizer = AutoTokenizer.from_pretrained("roberta-base")

inf_session = rt.InferenceSession('quote-text-classifier-quantized.onnx')
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

def classify_book_genre(text):
  input_ids = tokenizer(text)['input_ids'][:512]
  logits = inf_session.run([output_name], {input_name: [input_ids]})[0]
  logits = torch.FloatTensor(logits)
  probs = torch.sigmoid(logits)[0]
  return dict(zip(tags, map(float, probs))) 

label = gr.outputs.Label(num_top_classes=5)
#interface with i/o
iface = gr.Interface(fn=classify_book_genre, inputs="text", outputs=label)
iface.launch(inline=False)
					