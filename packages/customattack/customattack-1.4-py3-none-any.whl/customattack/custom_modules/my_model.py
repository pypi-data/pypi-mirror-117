import transformers
import torch

from customattack.models.helpers import lstm_for_classification
from customattack.models.helpers import resnet_for_classfication
from customattack.models.wrappers import pytorch_text_model_wrapper
from customattack.models.wrappers import pytorch_visual_model_wrapper
from customattack.models.wrappers import HuggingFaceModelWrapper

resnet = resnet_for_classfication.resnet50()
model = resnet.from_pretrained("/home/local/ASUAD/ujeong1/PycharmProjects/Adversarial_UI/pretrained/resnet50")
# model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet50', pretrained=True)
model_wrapper = pytorch_visual_model_wrapper.PyTorchVisualModelWrapper(model)

# lstm = lstm_for_classification.LSTMForClassification(num_labels=4)
# model = lstm.from_pretrained("/home/local/ASUAD/ujeong1/PycharmProjects/Adversarial_UI/pretrained/lstm")# Why relative path not working?
# model_wrapper = pytorch_text_model_wrapper.PyTorchModelWrapper(model, model.tokenizer)

# model = transformers.AutoModelForSequenceClassification.from_pretrained("textattack/bert-base-uncased-ag-news")
# tokenizer = transformers.AutoTokenizer.from_pretrained("textattack/bert-base-uncased-ag-news")
# model_wrapper = HuggingFaceModelWrapper(model, tokenizer)
# attack_args = customattack.AttackArgs(
#     num_examples=20,
#     log_to_csv="log.csv",
#     checkpoint_interval=5,
#     checkpoint_dir="checkpoints",
#     disable_stdout=True
# )
#
# attacker = customattack.Attacker(attack, dataset, attack_args)
# attacker.attack_dataset()