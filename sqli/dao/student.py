INSERT INTO students (name) VALUES (:name)
q = session.execute("INSERT INTO students (name) VALUES (:name)", {\"name\": name})
