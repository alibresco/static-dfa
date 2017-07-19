# First just a test for binary

from glob import glob
import os
import re
import shutil
from subprocess import call

PATH = None
# default language
LANGUAGE = list('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')

class State:
    # name: the name of the state
    # states: {name: value}
    def __init__(self, name, states, accept, start):
        self.name = name
        self.states = states
        self.accept = accept
        self.start = start

    def create_base(self):
        subpath = PATH + self.name + '/'
        try:
            os.mkdir(subpath)
        except Exception as e:
            pass
        if self.accept:
            message = 'accept' 
        else: 
            message = 'reject'
        with open(subpath + 'index.html', 'w') as f:
            f.write(message)

    def create(self):
        subpath = PATH + self.name
        other = None
        for name, val in self.states.iteritems():
            if name == 'other':
                other = val
                continue
            os.chdir(subpath)
            os.symlink('../' + val, name)
            os.chdir('../..')
            if self.start:
                os.symlink('states/' + val, name)
            os.chdir('..')
        if other:
            for s in LANGUAGE:
                if s not in self.states:
                    os.chdir(subpath)
                    os.symlink('../' + other, s)
                    os.chdir('../..')
                    if self.start:
                        os.symlink('states/' + other, s)
                    os.chdir('..')

def get_states(state_list):
    states = []
    start = True
    for state in state_list:
        mappings = {}
        m = re.match(r'^([^\(\s]+)\s*\((\w+)\).*$', state[0])
        name = m.group(1)
        accept = m.group(2) == 'accept'
        for line in state[1:]:
            m = re.search(r'\s+([^\s:]+)\s*:\s*([^\s]+)', line)
            mappings[m.group(1)] = m.group(2)
        states.append(State(name, mappings, accept, start))
        start = False
    return states

def parse_states(filename):
    global LANGUAGE
    file = None
    with open(filename, 'r') as f:
        file = f.read()
    file += '\n'
    cleaned = re.sub(r'#.*\n', '\n', file)
    cleaned = re.sub(r'\n\s*\n', '\n', cleaned)
    cleaned = re.sub(r'\n+', '\n', cleaned)
    cleaned = re.sub(r'^\s*\n', '', cleaned)
    lines = cleaned.split('\n')[:-1]
    if lines[0].startswith('LANGUAGE'):
        array_str = re.search(r'^LANGUAGE\s*=\s*\[(.+)\]', lines[0]).group(1)
        LANGUAGE = re.split(r'\s*,\s*', array_str)
        lines = lines[1:]
    states = []
    active = None
    for line in lines:
        if active == None:
            active = [line]
        else:
            if line[0].isspace():
                active.append(line)
            else:
                states.append(active)
                active = [line]
    states.append(active)
    return get_states(states)

def make_states_from_file(filename):
    global PATH
    dfa_name = ''.join(filename.split('.')[:-1])
    PATH = dfa_name + '/states/'
    try:
        shutil.rmtree(dfa_name)
    except:
        pass
    os.mkdir(dfa_name)
    os.mkdir(PATH)
    shutil.copy(filename, dfa_name)
    os.rename(dfa_name + '/' + filename, dfa_name + '/' + 'index.html')
    states = parse_states(filename)
    for state in states:
        state.create_base()
    for state in states:
        state.create()

def main():
    files = glob('*.dfa')
    for filename in files:
        make_states_from_file(filename)

if __name__ == '__main__':
    main()
