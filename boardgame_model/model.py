from mesa import Agent, Model
from mesa.space import SingleGrid
import random
#Thomas Martinson
#SDSU
#CS558


class BoardGameModel(Model):
    """A simple model of  a board game whereby rivals (red vs. blue) seek to find and capture each
other in a geographical region of numbered circles. They start on random independent circles,
and take turns moving 1 adjacent circle in a random direction each move. If they land on a circle
where their rival lies, they capture the other and win.
    """

    def __init__(self, N=10, width=5, height=5):
        self.num_agents = int(N/2)
        self.grid = SingleGrid(height, width, True)
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
                print("Red Turn")
                self.redAgentList[random.randint(0,numRed-1)].step()
            
                self.turn = 0
            else:
                print("Blue Turn")
                self.blueAgentList[random.randint(0,numBlue-1)].step()
            
                self.turn = 1
        else:
            if(numRed is 0):
                print("Game Over! Blue Team Wins.")
            else:
                print("Game Over! Red Team Wins.")
            self.running = False
        
        
    
class RedPiece(Agent):
    """ A red game piece."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
    def move(self):
        
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        
        if self.model.grid.is_cell_empty(new_position): # check if cell is empty
            print("Red piece moves from ",self.pos," to ",new_position)
            self.model.grid.move_agent(self, new_position) # move agent to empty cell
            
        else: # check if cell has a blue agent
            cellmates = self.model.grid.get_cell_list_contents([new_position])
            if type(cellmates[0]) is BluePiece:
                
                self.model.grid.remove_agent(cellmates[0])
                self.model.blueAgentList.remove(cellmates[0])
                print("Red piece at",self.pos,"killed blue piece at ",new_position)
                self.model.grid.move_agent(self, new_position) # move agent to empty cell
            else:
                print("Red piece attempted to move from",self.pos,"to",new_position,", red piece already there.")
            
    def step(self):
        self.move()
        
    
        
class BluePiece(Agent):
    """ A blue game piece."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        
        if self.model.grid.is_cell_empty(new_position): # check if cell is empty
            print("Blue piece moves from ",self.pos," to ",new_position)
            self.model.grid.move_agent(self, new_position) # move agent to empty cell
            
        else: # check if cell has a red agent
            cellmates = self.model.grid.get_cell_list_contents([new_position])
            if type(cellmates[0]) is RedPiece:
                
                self.model.grid.remove_agent(cellmates[0])
                self.model.redAgentList.remove(cellmates[0])
                print("Blue piece at",self.pos,"killed red piece at ",new_position)
                self.model.grid.move_agent(self, new_position) # move agent to empty cell
            else:
                print("Blue piece attempted to move from",self.pos,"to",new_position,", blue piece already there.")
                

    def step(self):
        self.move()
        
        
        
