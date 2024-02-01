import os

from statemachine import StateMachine, State


class Agent(StateMachine):
    idle = State(initial=True)
    scanning_file = State()
    remediating = State()

    create_file = (idle.to(scanning_file))
    idle.from_(scanning_file, cond='file_is_benign')
    idle.from_(remediating)
    remediating.from_(scanning_file, cond='file_is_malicious')

    def file_is_benign(self):
        return not self.file_is_malicious()

    def file_is_malicious(self):
        return 'mal' in self.current_file_location

    def on_enter_scanning_file(self, file_data, file_path):
        self.current_file = file_data
        self.current_file_location = file_path


if __name__ == '__main__':
    os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
    agent_machine = Agent()
    agent_machine._graph().write_png(r'C:\Users\amit.w\Downloads\state_machine.png')
