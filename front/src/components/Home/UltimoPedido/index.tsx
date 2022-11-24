import { Container, ContainerConteudo } from "./styles";

export default function UltimoPedidoComponent(){
    return (
        <>
            <Container>
                <h6>Você não possui pedido em andamento!</h6>
                <ContainerConteudo>
                    <p>Seu último pedido foi realizado em 30/08/2022.</p>
                </ContainerConteudo>
            </Container>
        </>
    )
}