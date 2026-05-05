
# Priority Manager (Team: sleepy_salamanders)

An app that uses machine learning to help users prioritize their tasks based on the task description and due date.

This is composed of three distinct subsystems:

1. **Web App**: A user-facing Flask web dashboard where clients can add, complete, or delete tasks. This also includes a basic user login and profile implementation.
2. **Machine Learning Client**: A backend Python service utilizing a OpenAI's `gpt-4o` model to give each task a numerical priority score, which is then used to label the tasks a "Low", "Medium", or "High" priority.
3. **Database**: A centralized MongoDB instance persisting all created tasks, and user profile data.

## Team Members
* [Christopher Cajamarca](https://github.com/ChrisC0205)
* [Valeria Chang](https://github.com/ValeriaChang)
* [Samay Dhawan](https://github.com/samaythe1)
* [Rehan Gupta](https://github.com/rehanguptaNYU)
* [Yash Pazhianur](https://github.com/yashpaz123)


## Configuration & Usage

### 1. Start Services (Docker)
All pieces of the project are systematically orchestrated using `docker-compose`. There is no need to make any `.env` files—all default configurations are already baked into the `docker-compose.yml` and Dockerfiles.

Ensure you have Docker Desktop running, then execute:
```bash
docker-compose up --build
```
This single startup command securely initializes:
- The `web-app` proxy serving the site at port `5000`
- The `ml-client` API mounted to port `5001`
- A `mongodb` container storing the tasks and users natively mapped to port `27017`


### 2. Start Drawing
Once the instances are running, open your web browser to view the application:
[http://localhost:5000](http://localhost:5000)

First create an account.
Then click "Add task", and provide a "Task Name", "Description", and select a "Due Date".
Then click "Save Task", and your task will eventually appear in the dashboard with a label that prioritizes it as either "Low", "Medium", or "High".

