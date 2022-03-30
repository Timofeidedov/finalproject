import markovify
with open("horos.txt",encoding='utf8') as f:
    text_a = f.read()
with open("books.txt",encoding='utf8') as f1:
    text_b = f1.read()
model_a = markovify.Text(text_a)
model_b = markovify.Text(text_b)
model = markovify.combine([ model_a, model_b ], [ 2, 1 ])
