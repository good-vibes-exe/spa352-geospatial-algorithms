
from IPython.display import display, Markdown

def show_heading(topic_heading, excercise_heading):
    "Formats excercise heading"
    return display(Markdown(f'## {topic_heading}\n### {excercise_heading}'))

def show_matrix(label, result):
    "Formats excercises"
    return display(Markdown(f'`{label}`\n```\n{result}\n```'))
