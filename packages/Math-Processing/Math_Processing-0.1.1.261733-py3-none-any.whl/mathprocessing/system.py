def open_sourse(module=None):
    if module == None:
        return (open_sourse('__init__'), open_sourse('math'), open_sourse('system')))
    elif module == '__init__' or module == 'mathprocessing':
        return open('__init__.py').read()
    elif module == 'math':
        return open('math.py').read()
    elif module == 'system':
        return open('system.py').read()
    else:
        raise ModuleNotFoundError('Module \'%s\' not found' % module)
