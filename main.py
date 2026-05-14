from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.presenters.pedido_presenter import PedidoPresenter

def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)
    
    controller.criar_pedido("Leonardo", 100, "Normal")
    controller.criar_pedido("Cardia", 200, "Vip")
    controller.criar_pedido("Da cruz", 300, "Premium")

    """print(controller.listar_pedidos())"""


    list = controller.listar_pedidos()
    for pedido in list:
        print(pedido)

if __name__ == "__main__":
    main()