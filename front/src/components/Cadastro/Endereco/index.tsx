import Campo from "../../UI/Campos";
import { CampoTiposConteudo, CampoTiposLayout } from "../../UI/Campos/entradas";
import { ContainerLinha } from "./styles";

export default function CadastroEnderecoComponent(){
    return <>
        <ContainerLinha>
            <Campo label="Endereco" larguraInput="468px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
            <Campo label="Bairro" larguraInput="229px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
        </ContainerLinha>
        <ContainerLinha>
            <Campo label="Nº" larguraInput="55px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
            <Campo label="Cidade" larguraInput="261px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
            <Campo label="Estado" larguraInput="68px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
            <Campo label="C.E.P." larguraInput="190px" layout={CampoTiposLayout.Horizontal} tipo={CampoTiposConteudo.Texto}/>
        </ContainerLinha>
    </>
}