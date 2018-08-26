
#black is 0, red is 1

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1


class rbtree:
    def __init__(self, value):
        self.root = Node(value)
        self.root.color = 0
        self.end = Node(0)
        self.end.color = 0
        self.root.parent = self.end
        self.root.right = self.end
        self.root.left = self.end

    def left_rorate(self, N):
        # parent is OK
        y = N.left

        y.parent = N.parent
        if N.parent != self.end:
            if N == N.parent.left:
                N.parent.left = y
            else:
                N.parent.right = y

        N.left = y.right
        if y.right != self.end:
            y.right.parent = N

        y.right = N
        N.parent = y
        if N == self.root:
            self.root = y

    def right_rorate(self,  N):
        # parent is OK

        y = N.right

        y.parent = N.parent
        if N.parent != self.end:
            if N == N.parent.left:
                N.parent.left = y
            else:
                N.parent.right = y

        N.right = y.left
        if y.left != self.end:
            y.left.parent = N

        y.left = N
        N.parent = y
        if N == self.root:
            self.root = y

    def insert_fix(self,N):
        while N.parent.color == 1 and N != self.root:
            if N.parent == N.parent.parent.left:
                y = N.parent.parent.right
                if y.color == 1:
                    N.parent.color = 0
                    N.parent.parent.color = 1
                    y.color = 0
                    N = N.parent.parent

                else:
                    if N == N.parent.right:
                        self.right_rorate(N.parent)
                        N = N.left
                    N.parent.color = 0
                    N.parent.parent.color = 1
                    N = N.parent.parent
                    self.left_rorate(N)

            else:
                y = N.parent.parent.left
                if y.color == 1:
                    N.parent.color = 0
                    N.parent.parent.color = 1
                    y.color = 0
                    N = N.parent.parent

                else:
                    if N == N.parent.left:
                        self.left_rorate(N.parent)
                        N = N.right
                    N.parent.color = 0
                    N.parent.parent.color = 1
                    N = N.parent.parent
                    self.right_rorate(N)
        self.root.color = 0

    def initNode(self,value):
        x = Node(value)
        x.left = self.end
        x.right = self.end
        x.parent = self.end
        return x

    def insert(self,value):
        N = self.initNode(value)

        y = self.end
        x = self.root
        while x != self.end:
            y = x
            if x.value > N.value:
                x = x.left
            else:
                x = x.right
        x = y
        if x.value > N.value:
            x.left = N
        else:
            x.right = N

        N.left = self.end
        N.right = self.end
        N.parent = y
        N.color = 1
        self.insert_fix(N)

    def show(self, N):
        if N.right != self.end:
            self.show(N.right)

        print(N.value, "  ", N.color)

        if N.left != self.end:
            self.show(N.left)

    def delete(self,value):
        y = self.end
        x = self.root
        while x != self.end:
            y = x
            if value < x.value:
                x = x.left
            elif value > x.value:
                x = x.right
            else:
                break

        if x == self.end:
            print('No the number')
            return

        xori = x.color

        if x.left == self.end or x.right == self.end:

            if x.parent == self.end:
                if x.right == self.end:
                    self.root = x.left
                else:
                    self.root = x.right

                if self.root == self.end:
                    print("over")
                    return

            else:
                if x.right == self.end:
                    y = x.left
                else:
                    y = x.right

                # if y == self.end:
                #     if x == x.parent.left:
                #         x.parent.left = y
                #     else:
                #         x.parent.right = y
                #     self.delete_fix()

                y.parent = x.parent
                if x.parent.left == x:
                    x.parent.left = y
                else:
                    x.parent.right = y

                zori = y.color
                y.color = x.color

                if zori == 0:
                    self.delete_fix(y)

                if y == self.end:
                    y.parent = self.end
                    y.color = 0


        else:
            z = x.left
            zx = x
            while z.right != self.end:
                zx = z
                z = z.right

            if zx == x:
                z.parent = x.parent
                if x.parent != self.end:
                    if x == x.parent.left:
                        x.parent.left = zx
                    else:
                        x.parent.right = zx

                z.right = x.right
                if x.right != self.end:
                    x.right.parent = z

                zori = z.color
                z.color = x.color
                if zori == 0:
                    self.delete(z.left)

            else:
                zx.right = zx.left
                if zx.left != self.end:
                    zx.left.parent = zx.parent

                z.parent = x.parent
                if x.parent.color != self.end:
                    if x.parent.right == x:
                        x.parent.right = z
                    else:
                        x.parent.left = z

                z.left = x.left
                if x.left != self.end:
                    x.left.parent = z
                z.right = x.right
                if x.right != self.end:
                    x.right.parent = z

                zori = z.color
                z.color = x.color

                if zori == 0:
                    self.delete_fix(zx.right)


    def delete_fix(self, N):
        while N.color == 0 and N != self.root:
            if N == N.parent.left:
                w = N.parent.right
                if w.color == 1:
                    w.color = 0
                    N.parent.color = 1
                    self.right_rorate(N.parent)

                if w.left.color == 0 and w.right.color == 0:
                    w.color = 1
                    N = N.parent
                else:
                    if w.right.color == 0:
                        w.color = 1
                        w.left.color = 0
                        self.left_rorate(w)
                        w = N.parent.right

                    w.color = N.parent.color
                    N.parent.color = 0
                    w.right.color = 0
                    self.right_rorate(N.parent)

            else:
                w = N.parent.left
                if w.color == 1:
                    w.color = 0
                    N.parent.color = 1
                    self.left_rorate(N.parent)

                if w.left.color == 0 and w.right.color == 0:
                    w.color = 1
                    N = N.parent
                else:
                    if w.left.color == 0:
                        w.color = 1
                        w.right.color = 0
                        self.right_rorate(w)
                        w = N.parent.left

                    w.color = N.parent.color
                    N.parent.color = 0
                    w.left.color = 0
                    self.left_rorate(N.parent)

        N.color = 0




if __name__ == "__main__":

    RB = rbtree(41)

    RB.insert(38)
    RB.insert(31)
    RB.insert(12)
    RB.insert(19)
    RB.insert(8)

    RB.delete(8)
    RB.delete(12)
    RB.delete(19)
    RB.delete(31)
    RB.delete(38)
    RB.delete(41)

