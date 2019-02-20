def censor(text,word):
  censored=""
  for c in word:
    censored+="*"
  text=text.replace(word,censored)
  return text

print(censor("this is a line","line"))