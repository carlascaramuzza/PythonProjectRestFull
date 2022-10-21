import PedidosStatus from "../../../components/Pedidos/Status";
import BotaoNavegacao from "../../../components/UI/Botoes/Navegacao";
import CardTitulo from "../../../components/UI/Cards/CardTitulo";

export default function TelaPedidoStatus(){
    return (
        <>
            <CardTitulo texto="Seus pedidos realizados"/>
            <PedidosStatus />
            <BotaoNavegacao rotulo="Fazer um novo pedido" rota="/pedidos/criar" />
        </>
    )
}