import statistics as st
while True:
    print("\n1.Mean \n2.Median \n3.Mode \n4.multi \n5.p variance \n6.sample variance \n7.stdeviation \n8.p stdeviation \n9.min \n10.max \n11.range \n12.exit")
    ch=int(input("Enter the option"))
    data=[]
    if ch>=1 and ch<=12:
        n=int(input("Enter the value add the array"))
        for i in range(n):
            data.append(float(input("enter the value")))
        if ch==1:
            print("mean value:",st.mean(data))
        elif ch==2:
            print("median",st.median(data))
        elif ch==3:
            print("mode",st.mode(data))
        elif ch==4:
            print("multi",st.multimode(data))
        elif ch==5:
            print("p variance",st.pvariance(data))
        elif ch==6:
            print("s variance",st.variance(data))
        elif ch==7:
            print("std",st.stdev(data))
        elif ch==8:
            print("p std",st.pstdev(data))
        elif ch==9:
            print(min(data))
        elif ch==10:
            print(max(data))
        elif ch==11:
            print(max(data)-min(data))
        elif ch==12:
            break
