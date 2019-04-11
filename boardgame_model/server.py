from mesa.visualization.ModularVisualization import ModularServer
from .model import BoardGameModel
from mesa.visualization.modules import CanvasGrid
from .model import RedPiece, BluePiece



def agent_portrayal(agent):
    portrayal = {"Shape": "circle","Filled": "true","r": 0.5}
    
    if type(agent) is RedPiece:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    
    
    if type(agent) is BluePiece:
        portrayal["Color"] = "blue"
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    
    
    return portrayal


#create grid (numx,numy,pixelsx,pixelsy)
grid = CanvasGrid(agent_portrayal, 5, 5, 500, 500)


server = ModularServer(BoardGameModel, [grid], "Board Game Model")
server.port = 8521
