import CardapioBebidasComponent from "../../components/Cardapio/Bebidas";
import CardapioEntradasComponent from "../../components/Cardapio/Entradas";
import CardapioPratosPrincipaisComponent from "../../components/Cardapio/PratosPrincipais";
import CardapioSobremesasComponent from "../../components/Cardapio/Sobremesas";
import { ContainerLinha } from "./styles";

export default function TelaCardapio(){
    return (
        <>
            <ContainerLinha>
                <CardapioEntradasComponent />
                <CardapioPratosPrincipaisComponent />
                <CardapioSobremesasComponent />
            </ContainerLinha>
            <CardapioBebidasComponent />
        </>
    )
}