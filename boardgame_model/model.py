from mesa import Agent, Model
from mesa.space import MultiGrid
import random



class BoardGameModel(Model):
    """A simple model of  a board game whereby rivals (red vs. blue) seek to find and capture each
other in a geographical region of numbered circles. They start on random independent circles,
and take turns moving 1 adjacent circle in a random direction each move. If they land on a circle
where their rival lies, they capture the other and win.
    """

    def __init__(self, N=20, width=5, height=5):
        self.num_agents = int(N/2)
        self.grid = MultiGrid(height, width, True)
        self.redAgentList = []
        self.blueAgentList = []
        self.turn = 1
        
        
        # Create Red and Blue agents
        for i in range(self.num_agents):
            a = RedPiece(i, self)
            self.redAgentList.append(a)
            
            
            # Add the agent to a random empty grid cell
            self.grid.place_agent(a, self.grid.find_empty())
            
            b = BluePiece(i, self)
            self.blueAgentList.append(b)
            
            
            # Add the agent to a random empty grid cell
            self.grid.place_agent(b, self.grid.find_empty())
            
     
        self.running = True
        

    def step(self):
        numRed = len(self.redAgentList)
        numBlue = len(self.blueAgentList)
        if ((numRed > 0) and (numBlue > 0)):
            if (self.turn == 1):
                print("red turn")
            
                self.redAgentList[random.randint(0,numRed-1)].step()
            
                self.turn = 0
            else:
                print("blue turn")
                self.blueAgentList[random.randint(0,numBlue-1)].step()
            
                self.turn = 1
        else:
            print("Game Over")
        
        
    
class RedPiece(Agent):
    """ A red game piece."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.color = 1 # 1 for red
    
    #MODIFY MOVE FUNCTION
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        
    
        
class BluePiece(Agent):
    """ A blue game piece."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.color = 0 # 0 for blue

    #MODIFY MOVE FUNCTION
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        
        
        
