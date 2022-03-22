""" for an electric companey data set organized in tree manner"""


class treeenode:
    def __init__(self,data):
        self.data =data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent =self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def  print_tree(self):
        space = " " * self.get_level() * 9
        prefix = space + '->  '
        print(space+ prefix + self.data)
        if len(self.children):
            for child in self.children:
                 child.print_tree()




def build_tree():
    root = treeenode("electronics")

    laptop = treeenode('laptop')
    laptop.add_child(treeenode('mac'))
    laptop.add_child(treeenode('surface'))
    laptop.add_child(treeenode('microsaft'))

    phones = treeenode('phones')
    phones.add_child(treeenode('iphone'))
    phones.add_child(treeenode('google'))
    phones.add_child(treeenode('mi'))

    tv = treeenode('TV')
    tv.add_child(treeenode('LG'))
    tv.add_child(treeenode('sony'))
    tv.add_child(treeenode("sharp"))

    root.add_child(laptop)
    root.add_child(phones)
    root.add_child((tv))

    return root




if __name__=='__main__':
    root = build_tree()
    root.print_tree()
