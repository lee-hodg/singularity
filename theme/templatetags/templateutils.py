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


@register.filter(name='defaultdict_keys')
def defaultdict_keys(ddict):
    '''
    Normally in the template given a dictionary
    called mydict in the context, keys() can be called
    simply with {{mydict.keys}}.  However because of the
    way Django does look ups, namely first trying to
    see if a key called 'keys' exists and only trying keys()
    method if not, and because of the nature of the defaultdict(list)
    , namely returning [] even if the key lookup failed and creating
    a key called 'keys', {{mydict.keys}} will just result in []
    not the actual keys of the defaultdict.

    This filter grabs the existings keys of a defaultdict.
    '''
    return ddict.keys()

@register.filter(name='comment_level')
def comment_level(comment):
    '''
    Takes a comment and returns its level in the tree heirarchy.
    Parent comments are not replies to anything and have level 0.
    '''
    level = 0
    while True:
        if not comment.replied_to:
            # comment is not a reply, but a level 0 parent.
            break
        else:
            # comment is a reply, inc level +1
            level += 1
            # move to comment above
            comment = comment.replied_to
        # at end of recursion rtn level
    return level
