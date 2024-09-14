from ..extensions import db

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer) #From Courses
    teacher_id = db.Column(db.Integer) #From Teachers
    classroom_id = db.Column(db.Integer) #From Classrooms

    day_of_week = db.Column(db.String(50))
    start_time = db.Column(db.String(50)) #Time not String
    end_time = db.Column(db.String(50)) #Time not String

    """FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id),
    FOREIGN KEY (classroom_id) REFERENCES Classrooms(classroom_id)"""