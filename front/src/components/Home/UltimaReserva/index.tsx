import { Container, ContainerConteudo } from "./styles";

export default function UltimaReservaComponent(){
    return (
        <>
            <Container>
                <h6>Você não possui mesa reservada!</h6>
                <ContainerConteudo>
                    <p>Sua última reserva foi realizada em 30/08/2022.</p>
                </ContainerConteudo>
            </Container>
        </>
    )
}