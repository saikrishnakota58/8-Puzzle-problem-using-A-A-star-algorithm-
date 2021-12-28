import copy
class Puzzle:
  def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open_list = []
        self.closed_list = []
  def h_value(self,list,goal):
    """To compute heuristic value,h(n),the number of non-blank tiles not in
        their goal position"""
    count=0
    for i in range(self.n):
      for j in range(self.n):
        """if value at any position is not matching with the goal, increase the count"""
        if not (list[i][j] == goal[i][j]) and not (list[i][j]=='_'):
          count+=1
    return count

  def g_value(self, node):
      """Computes the cost of generation of given node from initial state,g(n).
      g(n) is the length of the path from initial node to given node n """
      return node.level

  def accept(self):
      """ Accept input matrix from the user """
      matrix = []
      for i in range(self.n):
          print("Enter row ",i+1," values separated by space  ")
          row = input().split(" ")
          matrix.append(row)
      return matrix

  def sort(self,open_list):
      """Sorts the nodes in open list based on thier f value"""
      length=len(open_list)
      for i in range(length-1):
          for j in range(length-i-1):
              if open_list[j].fvalue>open_list[j+1].fvalue:
                  open_list[j],open_list[j+1]=open_list[j+1], open_list[j]

  def print_path(self,node):
      """Outputs the least-cost path"""
      if node is not None:
          """Recursively call the function until it reaches initial node and output the path from initial node to goal state"""
          self.print_path(node.parent)
          print("  ↓ ")
          node.printMatrix()

  def find_fvalue(self,node,goal):
    """Computes f(n) value,f(n)=g(n)+h(n)"""
    return self.g_value(node)+self.h_value(node.state,goal)

  def solve(self,start,goal):
        start.fvalue = self.find_fvalue(start,goal)
        """ Put the start node in the open list"""
        self.open_list.append(start)
        while self.open_list is not None:
            """Pick the node with least f(n) value"""
            current_node = self.open_list[0]
            """ If the difference between current and goal node is 0 we have reached the goal node """
            if(self.h_value(current_node.state,goal) == 0):
                """output the  least-cost path and terminate """
                print("The least cost path from initial state to final state is as follows:")
                self.print_path(current_node)
                break
            children=current_node.generate_child()
            if children is not None:
                for child  in children:
                    """for each child compute f(n) and add it to open list"""
                    child.fvalue = self.find_fvalue(child,goal)
                    """ add child nodes in open list"""
                    self.open_list.append(child)
            """ Add current node into closed list after exploring its child nodes and remove it from open list"""
            self.closed_list.append(current_node)
            del self.open_list[0]
            """ sort the open list based on f value of the nodes"""
            self.sort(self.open_list)


class Node:
    def __init__(self,parent,state, level, fvalue):
        """ Initialize the node with the parent node ,state, level of the node and the calculated f(node) value """
        self.parent = parent
        self.state = state
        self.level = level
        self.fvalue = fvalue

    def find_position(self, x):
        """ Used to find the position of the blank space(_) """
        for i in range(len(self.state)):
            for j in range(len(self.state)):
                if self.state[i][j] == x:
                    return i, j

    def printMatrix(self):
        """ Used to  print the state of the node"""
        for row in self.state:
            print(*row)

    def generate_child(self):
        """ To generate child nodes of a node,by moving the blank space in all directions
        i.e,to the left,right,top and bottom"""
        children = []
        if self.find_position('_') is None:
            print("Error,the start matrix has no blank('_') space")
            return None
        x,y = self.find_position('_')
        if x > 0:  # condition to check whether blank space can be moved to top
            top = copy.deepcopy(self.state)
            """Shuffle blank space and its top tile"""
            top[x][y], top[x - 1][y] = top[x - 1][y],top[x][y]
            """create child node after shuffling blank space"""
            child = Node(self,top, self.level + 1, 0)
            children.append(child)
        if y > 0:  #  condition to check whether blank space can be moved to left:
            left = copy.deepcopy(self.state)
            """Shuffle blank space and its left side tile"""
            left[x][y], left[x][y - 1] = left[x][y - 1],left[x][y]
            """create child node after shuffling blank space"""
            child = Node(self,left, self.level + 1, 0)
            children.append(child)
        if x < len(self.state)-1:  #  condition to check whether blank space can be moved to bottom
            bottom = copy.deepcopy(self.state)
            """Shuffle blank space and its bottom tile"""
            bottom[x][y], bottom[x + 1][y] = bottom[x + 1][y],bottom[x][y]
            """create child node after shuffling blank space"""
            child = Node(self,bottom, self.level + 1, 0)
            children.append(child)
        if y < len(self.state)-1:  #  condition to check whether blank space can be moved to right
            """"""
            right = copy.deepcopy(self.state)
            """Shuffle blank space and its right side tile"""
            right[x][y], right[x][y + 1] =  right[x][y + 1],right[x][y]
            """create child node after shuffling blank space"""
            child = Node(self,right, self.level + 1, 0)
            children.append(child)
        return children

# driver Code
puzzle=Puzzle(3)
print("""Enter the initial state matrix 
NOTE: Enter underscore, '_' , instead of a blank space""")
start=puzzle.accept()
print("""Enter the goal state matrix 
NOTE: Enter underscore, '_' , instead of a blank space""")
goal_=puzzle.accept()
start_=Node(None,start,0,0)
puzzle.solve(start=start_,goal=goal_)

