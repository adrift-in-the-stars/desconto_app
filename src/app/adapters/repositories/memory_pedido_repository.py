from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.frameworks.database.memory_database import MemoryDatabase

class MemoryPedidoRepository(IPedidoGateway):
    def __initi__(self, database: MemoryDatabase):
        self.database = database

    def salvar(self, pedido: Pedido) -> None:
        self.database.pedidos.append(pedido)

    def listar(self) -> list[Pedido]:
        return self.database.pedidos