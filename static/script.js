const addStudentForm = document.getElementById("addStudentForm");
addStudentForm.addEventListener("submit", function(event)
{ 
    event.preventDefault(); 

    const name = document.getElementById("addstudentName").value;
    const age = document.getElementById("addstudentAge").value;
    const city = document.getElementById("addstudentCity").value;

    const studentData =
    {
        name: name,
        age: Number(age), 
        city: city
    }; 

    // fetch("http://127.0.0.1:8000/students",
    fetch("/students",

        { method: "POST",  
            headers:
            {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(studentData)
        })

            .then(function(response)
            {
                return response.json();
            })

            .then(function(data)
            {if (data)
                {
                    alert("Student added successfully!"); addStudentForm.reset(); loadStudents();
                }
            })

            .catch(function(error)
            {
                console.error(error);
                alert("Backend se connection nahi ho rha");
            });
});  

const updateStudentForm = document.getElementById("updateStudentForm");
updateStudentForm.addEventListener("submit", function(event) 
{
    event.preventDefault();

    const id = document.getElementById("updatestudentId").value;
    const name = document.getElementById("updatestudentName").value;
    const age = document.getElementById("updatestudentAge").value;
    const city = document.getElementById("updatestudentCity").value;

    const studentData =
    {
        name: name,
        age: Number(age),
        city: city
    };

    // fetch(`http://127.0.0.1:8000/students/${id}`,
    fetch(`/students/${id}`,
        
        { method:"PUT",
            headers:
            {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(studentData) })

            .then(function(response)
            {
                return response.json();
            })

            .then(function(data)
            { if(data) 
                {
                    alert("Student updated successfully!"); updateStudentForm.reset(); loadStudents();
                }
            })

            .catch(function(error)
            {
                console.error(error); alert("Backend se connection nahi ho saka.");
            });
});

const deleteStudentForm = document.getElementById("deleteStudentForm");
deleteStudentForm.addEventListener("submit", function(event) 
{

    event.preventDefault();

    const id = document.getElementById("deletestudentId").value;

    // fetch(`http://127.0.0.1:8000/students/${id}`,
    fetch(`/students/${id}`,

        {
            method: "DELETE"
        })

        .then(function(response)
        {
            return response.json();
        })
        
        .then(function(data)
        { if(data)
            {
                alert("Student deleted successfully!"); deleteStudentForm.reset(); loadStudents();
            }
        })

        .catch(function(error)
        { 
            console.error(error); alert("Backend se connection nahi ho saka.");

        });
});

function loadStudents()
// { fetch("http://127.0.0.1:8000/students")
{ fetch("/students") 

  .then(function(response)
    {
      return response.json();
    })

  .then(function(students)
    {
        const tableBody = document.querySelector("tbody");
        tableBody.innerHTML = "";
        students.forEach(function(student)
        {
            const row = document.createElement("tr");
            row.innerHTML =`
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.city}</td>`;
            
            tableBody.appendChild(row);
        });
    })

    .catch(function(error)
    {
        console.error(error); alert("Students load nahi ho sake ");
    });
} 

loadStudents(); 