def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must bu trees'
    return [label]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
t=tree(5,[tree(6,[tree(7)]),tree(1)])
print(t)