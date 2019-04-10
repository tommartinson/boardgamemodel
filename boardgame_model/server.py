from mesa.visualization.ModularVisualization import ModularServer
from .model import BoardGameModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    
    portrayal["Color"] = "red"
    portrayal["Layer"] = 0
    
    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)


model_params = {
    "N": UserSettableParameter('slider', "Number of agents", 100, 2, 200, 1,
                               description="Choose how many agents to include in the model"),
    "width": 10,
    "height": 10
}

server = ModularServer(BoardGameModel, [grid], "Board Game Model", model_params)
server.port = 8521
