from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid



class BoardGameModel(Model):
    """A simple model of  a board game whereby rivals (red vs. blue) seek to find and capture each
other in a geographical region of numbered circles. They start on random independent circles,
and take turns moving 1 adjacent circle in a random direction each move. If they land on a circle
where their rival lies, they capture the other and win.
    """

    def __init__(self, N=25, width=5, height=5):
        self.num_agents = int(N/2)
        self.grid = MultiGrid(height, width, True)
        self.schedule = RandomActivation(self)
        
        # Create Red agents
        for i in range(self.num_agents):
            a = RedPiece(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            
        # Create Blue agents
        for i in range(self.num_agents):
            a = BluePiece(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.running = True
        

    def step(self):
        self.schedule.step()
        


class RedPiece(Agent):
    """ A red game piece."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.color = 1 # 1 for red

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        
class BluePiece(Agent):
    """ A blue game piece."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.color = 0 # 0 for blue

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        
