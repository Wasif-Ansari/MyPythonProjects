import pywhatkit as pw

txt =input("Enter Text: ")
# pw.text_to_handwriting(txt,"img1.png",[0,0,138])
pw.text_to_handwriting(txt,"new text.png",rgb=[0,0,0])
print("END")