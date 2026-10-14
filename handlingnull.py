import pandas as pd

df=pd.read_csv("data.csv")
while True:
    print("\n1.data \n2.missing values sum \n3.missing values column \n4.missing values total\n5.dropna  row \n6.dropna column \n7.fillna")
    ch=int(input("Enter the choice"))
    if ch==1:
        print(df)
    elif ch==2:
        print(df.isnull())
    elif ch==3:
        print(df.isnull().sum())
    elif ch==4:
        print(df.isnull().sum().sum())
    elif ch==5:
        df=df.dropna()
        print(df)
    elif ch==6:
        df=df.dropna(axis=1)
        print(df)
    elif ch==7:
        df=df.fillna(0)
        print(df)
    elif ch==8:
        break
        
