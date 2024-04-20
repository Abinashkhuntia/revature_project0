import sqlite3

con = sqlite3.connect("/mnt/c/Computer_science/devops/revature/project-0/revhire.db")

cursor = con.cursor()


# cursor.execute(
#     """CREATE TABLE USER(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(20),
#         email VARCHAR(20),
#         password VARCHAR(20),
#         role VARCHAR(20)
#     )""")

# cursor.execute(
#     """CREATE TABLE JOB(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title VARCHAR(100),
#         description TEXT,
#         location VARCHAR(50),
#         experience_required INTEGER,
#         company_name VARCHAR(50),
#         employer_id INTEGER,
#         FOREIGN KEY(employer_id) REFERENCES USER(id)
#     )"""
# )

# cursor.execute(
#     """CREATE TABLE APPLICATION(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         job_id INTEGER,
#         status VARCHAR(20),
#         FOREIGN KEY(user_id) REFERENCES USER(id),
#         FOREIGN KEY(job_id) REFERENCES JOB(id)
#     )"""
# )



userss=cursor.execute('''select * from USER''').fetchall()
jobs=cursor.execute('''select * from JOB''').fetchall()
applications = cursor.execute('''SELECT * FROM APPLICATION''').fetchall()


print(userss)
print(jobs)
print(applications)


con.commit()

con.close()


