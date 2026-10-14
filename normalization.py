import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data.csv")
numeric_col=df.select_dtypes(include="number").columns
while True:
    print("\n1.original data \n2.min-max  \n3.z-score \n4.max abs")
    ch=int(input("Enter the choice"))
    if ch==1:
        print(df)
    elif ch==2:
        normalized=df.copy()
        for col in numeric_col:
            minval=df[col].min()
            maxval=df[col].max()
            normalized[col]=((df[col]-minval)/(maxval-minval))
            print(normalized)
    elif ch==3:
        normalized=df.copy()
        for col in numeric_col:
            mean_val=df[col].mean()
            std_val=df[col].std()
            normalized[col]=(df[col]-mean_val/std_val)
            print(normalized)
    elif ch==4:
        normalized=df.copy()
        for col in numeric_col:
            abs_val=df[col].abs().max()
            normalized[col]=(df[col]/abs_val)
            print(normalized)
    elif ch==5:
        break
