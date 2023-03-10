import { useNavigate } from "react-router-dom";
import { CentralizarConteudo } from "../../../globalStyles";
import BotaoSimples from "../../UI/Botoes/Simples";
import Campo from "../../UI/Campos";
import { CampoTiposConteudo, CampoTiposLayout } from "../../UI/Campos/entradas";
import CadastroEnderecoComponent from "../Endereco";
import { Cabecalho, Container, ContainerBotoesAcao, ContainerCampos, ContainerLinha, Logo, Titulo } from "./styles";

export default function CadastroUsuarioComponent(){
    const navigate = useNavigate();
    const aoConfirmar = () => {
        navigate("/login");
    }

    const aoCancelar = () => {
        navigate("/login");
    }

    return <>
        <CentralizarConteudo />
        <Container>
            <Cabecalho>
                <Titulo>Cadastro</Titulo>
                <Logo />
            </Cabecalho>
            <ContainerCampos>
                <ContainerLinha>
                    <Campo label="Nome de Usuario" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
                    <Campo label="Senha" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Senha}/>
                </ContainerLinha>
                <ContainerLinha>
                    <Campo label="Nome completo" larguraInput="563px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
                    <Campo label="Idade" larguraInput="74px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
                </ContainerLinha>
                <CadastroEnderecoComponent />
                <ContainerLinha>
                    <Campo label="C.P.F." larguraInput="240px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
                    <Campo label="E-mail" larguraInput="496px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
                </ContainerLinha>
            </ContainerCampos>
            <ContainerBotoesAcao>
                <BotaoSimples onClick={aoConfirmar} rotulo="Confirmar" largura="126px"/>
                <BotaoSimples onClick={aoCancelar} rotulo="Cancelar" largura="126px"/>
            </ContainerBotoesAcao>
        </Container>
    </>
}