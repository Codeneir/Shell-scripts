flag = 0
def helloer(func):
    print 'Hello-word!';
    func();
    if flag < 3 :
        func;
        helloer(func);
        raise Exception('3 times written');
        exit;

@helloer
def except_proc():
    global flag;
    flag += 1
