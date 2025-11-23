from src.gateway.routes.text_routes import router as text_router
from src.gateway.routes.log_routes import router as log_router
from src.gateway.routes.agent_routes import router as agent_router

routers = [text_router, log_router, agent_router]
