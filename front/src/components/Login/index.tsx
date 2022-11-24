import axios from "axios";
import { useQuery } from "react-query";
import { Link } from "react-router-dom";
import { CentralizarConteudo } from "../../globalStyles";
import BotaoSimples from "../UI/Botoes/Simples";
import Campo from "../UI/Campos";
import { CampoTiposConteudo, CampoTiposLayout } from "../UI/Campos/entradas";
import { Container, ContainerBotoesAcao, ContainerCadastre, Logo } from "./styles";

export default function LoginComponent(){
    const { data, isLoading } = useQuery('login', async () => {
        const { data } = await axios.post('http://127.0.0.1:5000/login', {
            cpf: "24892579233",
            senha: "duda@123" 
        });
        localStorage.setItem('token', data.token);
    });

    return (
        <>
            <CentralizarConteudo />
            <Container>
                <Logo />
                <Campo label="C.P.F." layout={CampoTiposLayout.Vertical} tipo={CampoTiposConteudo.Texto}/>
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