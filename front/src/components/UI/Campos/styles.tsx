import styled from "@emotion/styled";
import { CampoTiposLayout } from "./entradas";

interface ContainerEntradas {
    layout: CampoTiposLayout;
}
const Container = styled.div`
    display: flex;
    ${ (props: ContainerEntradas) => props.layout == CampoTiposLayout.Vertical 
        ? `flex-direction: column;
           justify-content: center;
           align-items: center;` 
        : `flex-direction: row;
           margin-right: 15px;` }
`;

const StyledLabel = styled.label`
    font-family: 'Josefin Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 20px;
    align-self: center;
`;

interface InputEntradas {
    layout: CampoTiposLayout;
    largura?: string;
}
const StyledInput = styled.input`
    background: #FFFFFF;
    border: 1px solid #7D4757;
    font-family: 'Josefin Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 20px;
    display: flex;
    align-items: center;
    text-indent: 5px;
    ${ (props: InputEntradas) => props.layout == CampoTiposLayout.Vertical 
        ? `text-align: center;
           width: ${props.largura ? props.largura : '85%'} ;` 
        : `text-align: row;
           margin-left: 10px;
           width: ${props.largura ? props.largura : '222px'};`}
`;

export { Container, StyledLabel, StyledInput };