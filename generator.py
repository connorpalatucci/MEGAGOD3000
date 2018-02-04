import markovify

# Get raw text as string.
with open("corpuscleaned5.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text, state_size=3)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())