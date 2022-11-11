import { Link } from "react-router-dom";
import { CentralizarConteudo } from "../../globalStyles";
import BotaoSimples from "../UI/Botoes/Simples";
import Campo from "../UI/Campos";
import { CampoTiposConteudo, CampoTiposLayout } from "../UI/Campos/entradas";
import { Container, ContainerBotoesAcao, ContainerCadastre, Logo } from "./styles";

export default function LoginComponent(){
    return (
        <>
            <CentralizarConteudo />
            <Container>
                <Logo />
                <Campo label="Login" layout={CampoTiposLayout.Vertical} tipo={CampoTiposConteudo.Texto}/>
                <Campo label="Senha" layout={CampoTiposLayout.Vertical} tipo={CampoTiposConteudo.Senha}/>
                <ContainerBotoesAcao>
                    <BotaoSimples rotulo="Entrar" largura="45%"/>
                    <BotaoSimples rotulo="Esqueci a senha" largura="45%"/>
                </ContainerBotoesAcao>
                <ContainerCadastre>
                    <span>Ainda não é membro?</span>
                    <Link to="/cadastro">Cadastre-se já!</Link>
                </ContainerCadastre>
            </Container>
        </>
    )
}