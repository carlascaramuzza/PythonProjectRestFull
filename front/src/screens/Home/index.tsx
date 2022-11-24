import UltimaReservaComponent from "../../components/Home/UltimaReserva";
import UltimoPedidoComponent from "../../components/Home/UltimoPedido";
import Carrossel from "../../components/UI/Carrossel";
import { ContainerLinha } from "./styles";

export default function TelaHome(){
    return (
        <>
            <Carrossel />
            <ContainerLinha>
                <UltimoPedidoComponent />
                <UltimaReservaComponent />
            </ContainerLinha>
        </>
    )
}