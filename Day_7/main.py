raw_inp = open('input.txt', 'r')
inp = [line.strip().split(' ') for line in raw_inp]

class folderfile():
    def __init__(self, _name, _parent, _size=0):
        self.name = _name
        self.parent = _parent
        self.size = _size
        self.content = []
    def isFolder(self):
        return self.size == 0
    def addChild(self, _newContent):
        self.content.append(_newContent)
    def calculateSize(self):
        if self.size != 0:
            return self.size
        return sum([x.calculateSize() for x in self.content])
    def getParent(self):
        return self.parent
    def getChild(self, _name):
        for child in self.content:
            if child.name == _name:
                return child
        return None
    def getSizedFolders(self, _size, lower=True):
        sized_childs = []
        for child in self.content:
            if child.isFolder():
                if (lower and child.calculateSize() <= _size) or (not lower and child.calculateSize() >= _size):
                    sized_childs.append(child)
                sized_childs.extend(child.getSizedFolders(_size, lower))
        return sized_childs

def getOuterRoot():
    outer_root = folderfile('/', None)
    current_folder = None
    for cmd in inp:
        if current_folder == None and cmd[2] != '/':
            print('No active folder!')
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '/':
                    current_folder = outer_root
                elif cmd[2] == '..':
                    if current_folder.getParent() != None:
                        current_folder = current_folder.getParent()
                    else:
                        print('Folder has no parent!')
                else:
                    if current_folder.getChild(cmd[2]) != None:
                        current_folder = current_folder.getChild(cmd[2])
                    else:
                        print('Child doesnt exsist')
        elif cmd[0] == 'dir':
            current_folder.addChild(folderfile(cmd[1], current_folder))
        else:
            try:
                current_folder.addChild(folderfile(cmd[1], current_folder, int(cmd[0])))
            except:
                print('Couldnt convert to int', cmd)
    return outer_root


def part1():
    outer_root = getOuterRoot()
    print(sum([x.calculateSize() for x in outer_root.getSizedFolders(100000)]))

part1() #=>1_084_134

def part2():
    outer_root = getOuterRoot()
    needed_space = 30_000_000 - (70_000_000 - outer_root.calculateSize())
    print(sorted([x.calculateSize() for x in outer_root.getSizedFolders(needed_space, False)])[0])

part2() #=>6_183_184
