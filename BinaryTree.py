""" 
            drink
         /         \
       hot         cold
      /   \       /     \
  coffee   tea  cola  fanta 
  
  """
 
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

 
drink= Node("drink") 
hot= Node("hot")
cold= Node("cold")
coffee= Node("coffee")
tea= Node("tea")
cola= Node("cola")
fanta = Node("fanta")

hot.left=coffee
hot.right=tea

cold.left=cola
cold.right=fanta

drink.left=hot
drink.right=cold 

print(drink.left) 
print(hot.val)          
#show error,     why? cola left has None, None have no attribute error (NoneType) 
print(cold.left.left.val)