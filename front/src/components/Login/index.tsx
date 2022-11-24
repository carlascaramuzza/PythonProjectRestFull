import axios from "axios";
import { useState } from "react";
import { useQuery } from "react-query";
import { Link } from "react-router-dom";
import { CentralizarConteudo } from "../../globalStyles";
import BotaoSimples from "../UI/Botoes/Simples";
import Campo from "../UI/Campos";
import { CampoTiposConteudo, CampoTiposLayout } from "../UI/Campos/entradas";
import { Container, ContainerBotoesAcao, ContainerCadastre, Logo } from "./styles";

export default function LoginComponent(){
    const [inputs, setInputs] = useState({});

    const handleChange = (event: any) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    const handleSubmit = async (event: any) => {
        event.preventDefault();
        const { data } = await axios.post('http://127.0.0.1:5000/login', inputs);
        localStorage.setItem('token', data.token);
    }

    return (
        <>
            <CentralizarConteudo />
            <Container>
                <Logo />
                <form>
                    <Campo label="C.P.F." propriedade="cpf" onChange={handleChange} layout={CampoTiposLayout.Vertical} tipo={CampoTiposConteudo.Texto}/>
                    <Campo label="Senha" propriedade="senha" onChange={handleChange} layout={CampoTiposLayout.Vertical} tipo={CampoTiposConteudo.Senha}/>
                    <ContainerBotoesAcao>
                        <BotaoSimples onClick={handleSubmit} rotulo="Entrar" largura="100%"/>
                    </ContainerBotoesAcao>
                </form>
                <ContainerCadastre>
                    <span>Ainda não é membro?</span>
                    <Link to="/cadastro">Cadastre-se já!</Link>
                </ContainerCadastre>
            </Container>
        </>
    )
}