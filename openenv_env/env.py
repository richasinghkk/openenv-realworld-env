from openenv_env.models import Observation

from openenv_env.tasks.task1_email import task_data as t1
from openenv_env.tasks.task2_cleaning import task_data as t2
from openenv_env.tasks.task3_code_review import task_data as t3

from openenv_env.tasks.graders import (
    grade_email,
    grade_cleaning,
    grade_code
)


class OpenEnv:

    def __init__(self):

        # Combine all tasks into one list
        self.tasks = []

        for item in t1:
            self.tasks.append(("email", item))

        for item in t2:
            self.tasks.append(("cleaning", item))

        for item in t3:
            self.tasks.append(("code", item))

        self.index = 0

    def reset(self):

        self.index = 0

        task_type, task = self.tasks[self.index]

        return Observation(
            task_id=0,
            input_data=task["input"]
        )

    def step(self, action):

        task_type, task = self.tasks[self.index]

        if task_type == "email":

            score = grade_email(
                action.response,
                task["truth"]
            )

        elif task_type == "cleaning":

            score = grade_cleaning(
                action.response,
                task["truth"]
            )

        else:

            score = grade_code(
                action.response,
                task["truth"]
            )

        # Feedback logic
        feedback = ""

        if score == 1.0:
            feedback = "Correct answer"

        elif score >= 0.5:
            feedback = "Partially correct"

        elif score > 0:
            feedback = "Minor progress"

        elif score < 0:
            feedback = "Penalty applied"

        else:
            feedback = "Incorrect answer"

        self.index += 1

        done = self.index >= len(self.tasks)

        if not done:

            next_task_type, next_task = self.tasks[self.index]

            next_obs = Observation(
                task_id=self.index,
                input_data=next_task["input"]
            )

        else:

            next_obs = None

        info = {
            "feedback": feedback
        }

        return next_obs, score, done, info

    def state(self):

        return {
            "current_task_index": self.index,
            "total_tasks": len(self.tasks),
            "remaining_tasks": len(self.tasks) - self.index
        }