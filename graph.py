import matplotlib.pyplot as plt
import numpy as np

while True:

    print("\n========== MATPLOTLIB GRAPH MENU ==========")
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Horizontal Bar Graph")
    print("4. Pie Chart")
    print("5. Scatter Plot")
    print("6. Histogram")
    print("7. Box Plot")
    print("8. Area Graph")
    print("9. Stem Plot")
    print("10. Step Graph")
    print("11. Multiple Line Graph")
    print("12. Exit")
    print("===========================================")

    ch = int(input("Enter your choice: "))

    # Common data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([10, 25, 15, 30, 20])

    # 1. Line Graph
    if ch == 1:
        plt.plot(x, y, marker='o')
        plt.title("Line Graph")
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.grid()
        plt.show()

    # 2. Bar Graph
    elif ch == 2:
        names = ["A", "B", "C", "D", "E"]
        values = [20, 35, 25, 40, 30]

        plt.bar(names, values)
        plt.title("Bar Graph")
        plt.xlabel("Category")
        plt.ylabel("Value")
        plt.show()

    # 3. Horizontal Bar Graph
    elif ch == 3:
        names = ["A", "B", "C", "D", "E"]
        values = [20, 35, 25, 40, 30]

        plt.barh(names, values)
        plt.title("Horizontal Bar Graph")
        plt.xlabel("Value")
        plt.ylabel("Category")
        plt.show()

    # 4. Pie Chart
    elif ch == 4:
        labels = ["CSE", "IT", "ECE", "EEE"]
        values = [35, 30, 20, 15]

        plt.pie(
            values,
            labels=labels,
            autopct='%1.1f%%'
        )

        plt.title("Department Distribution")
        plt.show()

    # 5. Scatter Plot
    elif ch == 5:
        height = [150, 155, 160, 165, 170, 175, 180]
        weight = [50, 55, 58, 62, 65, 70, 75]

        plt.scatter(height, weight)
        plt.title("Height vs Weight")
        plt.xlabel("Height")
        plt.ylabel("Weight")
        plt.show()

    # 6. Histogram
    elif ch == 6:
        marks = [
            45, 50, 55, 60, 62,
            65, 68, 70, 72, 75,
            78, 80, 82, 85, 90,
            92, 95
        ]

        plt.hist(marks, bins=5)
        plt.title("Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.show()

    # 7. Box Plot
    elif ch == 7:
        marks = [45, 50, 55, 60, 62, 65, 68,
                 70, 72, 75, 78, 80, 85, 90]

        plt.boxplot(marks)
        plt.title("Marks Box Plot")
        plt.ylabel("Marks")
        plt.show()

    # 8. Area Graph
    elif ch == 8:
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 25, 15, 30, 20])

        plt.fill_between(x, y)
        plt.plot(x, y)
        plt.title("Area Graph")
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.show()

    # 9. Stem Plot
    elif ch == 9:
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 25, 15, 30, 20])

        plt.stem(x, y)
        plt.title("Stem Plot")
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.show()

    # 10. Step Graph
    elif ch == 10:
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 25, 15, 30, 20])

        plt.step(x, y)
        plt.title("Step Graph")
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.show()

    # 11. Multiple Line Graph
    elif ch == 11:
        x = np.array([1, 2, 3, 4, 5])

        student1 = [60, 65, 70, 75, 80]
        student2 = [55, 70, 68, 82, 85]

        plt.plot(
            x,
            student1,
            marker='o',
            label="Student 1"
        )

        plt.plot(
            x,
            student2,
            marker='s',
            label="Student 2"
        )

        plt.title("Student Mark Comparison")
        plt.xlabel("Subject")
        plt.ylabel("Marks")
        plt.legend()
        plt.grid()
        plt.show()

    # 12. Exit
    elif ch == 12:
        print("Program exited successfully!")
        break

    else:
        print("Invalid choice! Enter 1 to 12.")
