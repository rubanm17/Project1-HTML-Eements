from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

resume = {
    "name": "Alex Johnson",
    "role": "Web Developer",
    "email": "alexjohnson@email.com",
    "phone": "+91 98765 43210",
    "location": "Chennai, India",
    "profile": "Motivated and creative web developer with a strong interest in building clean, responsive, and user-friendly websites.",
    "education": [
        {
            "title": "Bachelor of Computer Science",
            "place": "ABC College",
            "year": "2022 - 2025"
        },
        {
            "title": "Higher Secondary School",
            "place": "XYZ School",
            "year": "2020 - 2022"
        }
    ],
    "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript", "SQL"],
    "projects": [
        {
            "title": "Resume Website",
            "description": "Created a responsive resume website using Flask, HTML, and CSS."
        },
        {
            "title": "Student Management System",
            "description": "Developed a student record application using Python and SQLite."
        }
    ],
    "experience": [
        {
            "title": "Web Development Intern",
            "company": "Tech Solutions",
            "year": "2025",
            "description": "Assisted in creating responsive web pages and improving website layouts."
        }
    ],
    "languages": ["English", "Tamil"]
}


@app.route("/")
def home():
    return render_template("index.html", resume=resume)


@app.route("/resume")
def get_resume():
    return resume


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")

    print("New Contact Message")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
