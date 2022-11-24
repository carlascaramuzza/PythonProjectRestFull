import PedidosAcompanhamentos from "../../../components/Pedidos/Acompanhamentos";
import PedidosBebidas from "../../../components/Pedidos/Bebidas";
import PedidosEntradas from "../../../components/Pedidos/Entradas";
import PedidosLanches from "../../../components/Pedidos/Lanches";
import PedidosPorcoes from "../../../components/Pedidos/Porcoes";
import PedidosPratosPrincipais from "../../../components/Pedidos/PratosPrincipais";
import PedidosSobremesas from "../../../components/Pedidos/Sobremesas";
import CardTitulo from "../../../components/UI/Cards/CardTitulo";
import SubTab from "../../../components/UI/Tabs/SubTab";

export default function TelaPedidoCriar(){
    return (
        <>
            <CardTitulo texto="Fazer um novo pedido"/>
            <SubTab tabs={[
                { rotulo: 'Entradas', conteudo: <PedidosEntradas /> },
                { rotulo: 'Pratos Principais', conteudo: <PedidosPratosPrincipais /> },
                { rotulo: 'Sobremesas', conteudo: <PedidosSobremesas /> },
                { rotulo: 'Bebidas', conteudo: <PedidosBebidas /> },
                { rotulo: 'Acompanhamentos', conteudo: <PedidosAcompanhamentos /> },
                { rotulo: 'Lanches', conteudo: <PedidosLanches /> },
                { rotulo: 'Porções', conteudo: <PedidosPorcoes /> }
            ]}/>
        </>
    )
}