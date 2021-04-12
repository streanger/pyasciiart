import sys
import os
import ast
import json
from pathlib import Path
from termcolor import colored


class art():
    '''overwrite join, lower, upper and other methods; concat, slicing, etc'''
    def __init__(self, s):
        # ******* font setup *******
        self.default_font_file = 'fonts/basic_font.txt'
        self.characters_str = Path(self.default_font_file).read_text(encoding='utf-8')
        self.characters_data =  ast.literal_eval(self.characters_str)
        
        # ******* creating ascii art *******
        self.s = s
        self.ss = self.characters('ss')
        self.char_height = 6
        self.sart = self.join_characters(self.s)
        return None
        
        
    def join_characters(self, s):
        '''join str characters to ascii art characters'''
        chars = list(self.s)
        ascii_chunks = []
        number_of_chars = len(chars)
        for index, char in enumerate(chars):
            ascii_char = self.characters(char)
            ascii_chunks.append(ascii_char.splitlines())
            if index < number_of_chars - 1:
                ascii_chunks.append(self.ss.splitlines())
        chunks_swapped = list(zip(*ascii_chunks))
        ascii_str = '\n'.join([''.join(item) for item in chunks_swapped])
        return ascii_str
        
        
    def __add__(self, right):
        return art(self.s + right.s)
        
        
    def __repr__(self):
        return self.sart
        
        
    def __str__(self):
        return self.sart
        
        
    def __mul__(self, val):
        return art(self.s * val)
        
        
    def characters(self, character):
        '''
        ascrii art characters are:
            -6 lines height
            -11 characters width
        '''
        
        not_found = '''\
___________ 
|         |
|         |
|         |
|         |
|_________|
'''
        return self.characters_data.get(character, not_found)
        
        
        
# ************* funcs *************

def script_path():
    '''set current path, to script path'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def read_json(filename):
    '''read json file to dict'''
    data = {}
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        pass
    return data
    
    
def write_json(filename, data):
    '''write to json file
    # ensure_ascii -> False/True -> characters/u'type'
    '''
    with open(filename, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True
    
    
def read_file(filename, mode='r'):
    '''read from file'''
    content = ''
    try:
        with open(filename, mode, encoding='utf-8') as f:
            content = f.read()
            
    except Exception as err:
        print('failed to read from file: {}, err: {}'.format(filename, err))
        
    return content
    
    
def write_file(filename, text, mode='w'):
    '''write to file'''
    try:
        with open(filename, mode, encoding='utf-8') as f:
            f.write(text)
            
    except Exception as err:
        print('failed to write to file: {}, err: {}'.format(filename, err))
        
    return None
    
    
if __name__ == "__main__":
    script_path()
    
    line = '=='*23
    banner_top = colored(art('ascii'), 'green')
    banner_bottom = colored(art(' art'), 'cyan')
    banner = '{}\n{}\n{}\n{}'.format(line, banner_top, banner_bottom, line)
    print(banner)
    
    
'''
todo:
    -make full font (lower and upper)
    -make support for lower() and upper() methods
    -make fonts file configurable
    -
    
'''

