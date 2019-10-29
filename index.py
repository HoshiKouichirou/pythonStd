text = "りんご ごりら らっぱ ぱす すいか"
text  = text.split(" ")
ans = ["しりとり"]
def getLastWord():
  lastWord = len(ans)-1
  return ans[lastWord][len(ans[lastWord])-1]
def start():
  lastWord = getLastWord()
  if len(text) != 0:
    for val in text:
      if val[0] == lastWord:
        ans.append(val)
        text.remove(val)
        start()
        break
  else:
    print("FINISH", ans)
start()