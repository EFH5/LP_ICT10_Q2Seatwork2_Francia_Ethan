from pyscript import document, display

def calculate_grade(e): 
    grade1 = float(document.getElementById("grade1").value)
    grade2 = float(document.getElementById("grade2").value)
    grade3 = float(document.getElementById("grade3").value)
    grade4 = float(document.getElementById("grade4").value)
    grade5 = float(document.getElementById("grade5").value)
    grade6 = float(document.getElementById("grade6").value)

    

    avg = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6)/6

    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    full_Name = fname + " " + lname

    final_grade = avg

    display(f"Science: {grade1}, English: {grade2}, ICT: {grade3}, Math: {grade4}, Filipino: {grade5}, PE: {grade6}", target="output")
    display(f"Full Name: {full_Name}", target="full_Name")
    display(f"Your General Weighted Average is: {final_grade:.2f}", target="final_grade")




    