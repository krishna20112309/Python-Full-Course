letter='''Dear <|Name|>,
You are Selected !

Date: <|DATE|> '''
name=input("Enter you Name\n")
date=input("Enter Date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|DATE|>",date)

print(letter)


