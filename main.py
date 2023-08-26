from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class TaskWidget(BoxLayout):
    def __init__(self, task, **kwargs):
        super(TaskWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 10

        self.task_label = Label(text=task, size_hint_x=0.7, valign='middle', markup=True)
        self.complete_button = Button(text='Complete', size_hint_x=0.15, on_release=self.complete_task)
        self.delete_button = Button(text='Delete', size_hint_x=0.15, on_release=self.delete_task)

        self.add_widget(self.task_label)
        self.add_widget(self.complete_button)
        self.add_widget(self.delete_button)

    def complete_task(self, instance):
        self.task_label.text = '[s][color=008000]✓ {}[/color][/s]'.format(self.task_label.text)
        self.complete_button.disabled = True

    def delete_task(self, instance):
        App.get_running_app().tasks_layout.remove_widget(self)
        App.get_running_app().tasks.remove(self.task_label.text)

class ToDoApp(App):
    tasks = []

    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        self.task_input = TextInput(hint_text='Enter a new task...', multiline=False, size_hint_y=None, height=40)
        self.add_button = Button(text='Add Task', size_hint_y=None, height=40, on_press=self.add_task)
        
        self.tasks_layout = BoxLayout(orientation='vertical', spacing=5)
        
        self.layout.add_widget(self.task_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.tasks_layout)
        
        return self.layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()
            self.task_input.text = ''

    def update_task_list(self):
        self.tasks_layout.clear_widgets()
        for task in self.tasks:
            task_widget = TaskWidget(task)
            self.tasks_layout.add_widget(task_widget)

if __name__ == '__main__':
    ToDoApp().run()
