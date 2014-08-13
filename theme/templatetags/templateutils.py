from __future__ import division
from django.template import Library
from math import ceil

def ceildiv(a, b):
    return -(-a // b)

register = Library()


@register.filter(name='linebreaksbr')
def linebreaksbr(line):
    '''
    Take a comma seperated line of text,
    for example an address, and replace
    the commas with linebreaks
    '''
    try:
        line = line.replace(',', ',<br />')
    except:
        # on failure, e.g. not a str
        # just return orig
        pass

    return line

@register.filter(name='splitcolor')
def splitcolor(word, args):
    '''
    Take a word find the midpoint
    , color first half red, second black.
    '''
    try:
        if args is None:
            return word
        colors = [arg.strip() for arg in args.split(',')]
        if len(colors) != 2:
            return word
        mid = ceildiv(len(word),2)  # Rem python div takes floor
        newword = '<span style="color:'+colors[0]+'">'+word[:mid]+'</span>'
        newword += '<span style="color:'+colors[1]+'">'+word[mid:]+'</span>'
        word = newword
    except:
        # on failure, e.g. not a str
        # just return orig
        pass

    return word
