# Construction-company

Task manager for a construction company.

This manager was created to maintain a general list of employees, projects and tasks for these projects. A user with
administrator rights creates tasks and assigns an employee to perform it. After completion, the employee completes the
task and maintains a general list of completed tasks for each user and the entire company as a whole.

Opportunities for the admin user (manager):

- Create, update, delete projects.
- Create, update and delete tasks.
- Complete tasks assigned to this user.
- Create, delete employees.
- Update user data.

Opportunities for the regular user (employee):

- Complete tasks assigned to this user.
- Update user data.

## Running the program locally

1. Clone the source code:

```bash
git clone https://github.com/Thirteenthskyi/Construction-company.git
cd Сonstruction-company
```

2. Install modules and dependencies:

```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

3. `.env_sample` 
This is a sample .env file for use in local development.
Duplicate this file as .env in the root of the project
and update the environment variables to match your
desired config. You can use [djecrety.ir](https://djecrety.ir/)

4. Use the command to configure the database and tables:

```bash
python manage.py migrate
```

5. Start the app:

```bash
python manage.py runserver
```

- You can use following superuser (or create another one by yourself using the admin page):
    - Login: `admin.user`
    - Password: `Us2ddTX7`

**BD structure :**

![BD structure](screens/arch_bd.png)

**1. Login page :**

![Login page](screens/login.png)

**2. Home page :**

![Home page](screens/Home.png)

**3. Task list page :**

![Task list](screens/task_list.png)

**4. Task detail page :**

![Task detail](screens/task_detail.png)

**5. Employees list page :**

![Employees list](screens/employees_list.png)

**6. Employyes detail page:**

![Employee detail](screens/employees_detail.png)