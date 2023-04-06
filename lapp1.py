import nltk 
print(nltk.__version__) 
nltk.download() 
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good.""" 
tokens = nltk.word_tokenize(sentence) 
print(tokens) 
from nltk.tokenize import sent_tokenize 
para="""Cake is a form of sweet food made from flour, sugar,
and other ingredients, that is usually baked.In their oldest forms,
cakes were modifications of bread, 
but cakes now cover a wide range of preparations that can be simple or elaborate, 
and that share features with other desserts such as pastries, meringues, 
custards, and pies.The most commonly used cake ingredients include flour, 
sugar, eggs, butter or oil or margarine, a liquid, and leavening agents, 
such as baking soda or baking powder.""" 
tokenized_para=sent_tokenize(para) 
print(tokenized_para) 
print(type(tokenized_para))