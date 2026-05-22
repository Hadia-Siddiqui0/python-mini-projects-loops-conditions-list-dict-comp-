marks={"Hadia":99,
       "Yusma":97,
       "Ayesha":98,
       "Emaan":100,
       "Yumna":95}
def maximum(std_dict):
    max_marks=next(iter(std_dict.values()))
    for x in std_dict.values():
        if (x>max_marks):
            max_marks=x
    return max_marks

def minimum(std_dict):
    min_marks=next(iter(std_dict.values()))
    for x in std_dict.values():
        if (x<min_marks):
            min_marks=x
    return min_marks

def average(std_dict):
    total=0
    elements=len(std_dict)
    for x in std_dict.values():
        total=total+x
    avg_marks=total/elements
    return avg_marks

maxim=maximum(marks)
minim=minimum(marks)
avg=average(marks)
print(maxim,minim,avg)
