from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

# 4. templates/index.html
<!doctype html>
<html lang="en">
<head><title>To-Do</title></head>
<body>
  <h1>To-Do List</h1>
  <form method="POST" action="/add">
    <input name="title" required>
    <button type="submit">Add Task</button>
  </form>
  <ul>
    {% for task in tasks %}
      <li>{{ task.title }} <a href="/delete/{{ task.id }}">Delete</a></li>
    {% endfor %}
  </ul>
</body>
</html>
