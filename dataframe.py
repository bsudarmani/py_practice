import pandas as pd
df=pd.read_csv("data.csv")
while True:
    ch=int(input("\n1.first head \n2.tail row \n3.specific column \n4.col specific \n10.exit\n"))
    if ch==1:
        print(df.head(5))
    elif ch==2:
        print(df.tail(5))
    elif ch==3:
        val=int(input("Enter the val"))
        print(df.head(val))
        print(df.tail(val))
    elif ch==4:
        col=input("enter the column name")
        if col in df.columns:
            print(df[col])
        else:
            print("column not found")
    elif ch==5:
        print(df.info())
    elif ch==6:
        print(df.describe())
    elif ch==7:
        print(df.dtypes)
    elif ch==8:
        print(df.columns.tolist())
    elif ch==9:
        print(df.shape)
    elif ch==10:
        break
