sen="i am waking up and it's morning so morning is beautiful"

split_sen=sen.split()

sent_dict={}

for i in split_sen:
    if i not in sent_dict:
        sent_dict[i]=1
    elif i in sent_dict:
        sent_dict[i]= sent_dict[i]+1

print(sent_dict)