import sys
from collections import namedtuple

from jinja2 import Environment, FileSystemLoader

Member = namedtuple('Member', ['picture', 'name', 'position', 'description'])

CREW = [
    Member('juan.jpg', 'Juan Chavez', 'Executive', ''),
    Member('eric.jpg', 'Eric Kleifield', 'Executive', ''),
    Member('henry.jpg', 'Henry Dorfman', 'Executive', ''),
    Member('sab.jpg', 'Sab Sikder', 'Producer', ''),
    Member('christian.jpg', 'Christian Edghill', 'Camera Operator', ''),
    Member('vishnu.jpg', 'Vishnu Devarakonda', 'Actor', ''),
    Member('tatyana.jpg', 'Tatyana Zvereva', 'Actress', '')
]

def build_template(env, template_name, **kwargs):
    print "Building %s..." % template_name
    template = env.get_template(template_name)
    with open(template_name, "w") as f:
        f.write(template.render(**kwargs))

def build_index(env):
    build_template(env, 'index.html')

def build_story(env):
    build_template(env, 'story.html')

def build_crew(env):
    build_template(env, 'crew.html',
        crew=CREW
    )

def build_films(env):
    build_template(env, 'films.html')

def build_gallery(env):
    build_template(env, 'gallery.html')

def build_contact(env):
    build_template(env, 'contact.html')

def main():
    env = Environment(loader=FileSystemLoader(searchpath="./templates"))
    build_index(env)
    build_story(env)
    build_crew(env)
    build_films(env)
    build_gallery(env)
    build_contact(env)

if __name__ == '__main__':
    main()
