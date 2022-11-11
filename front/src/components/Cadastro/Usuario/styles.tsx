import styled from "@emotion/styled";
import ImagemLogo from '../../../assets/logo.png';

const Container = styled.div`
    width: 958px;
    height: 437px;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 10px;
    padding: 20px;
    justify-self: center;
`;

const Cabecalho = styled.div`
    display: flex;
    flex-direction: row;
    place-content: space-between;
`;

const ContainerLinha = styled.div`
    display: flex;
    flex-direction: row;
    margin-bottom: 10px;
`;

const ContainerCampos = styled.div`
    padding-left: 25px;
    height: 185px;
`;

const ContainerBotoesAcao = styled.div`
    display: flex;
    flex-direction: row;
    height: 52px;
    place-content: center;
`;

const Titulo = styled.h1`
    font-family: 'Allison';
    font-style: normal;
    font-weight: 400;
    font-size: 150px;
    line-height: 190px;
    margin: 0px;
`;

const Logo = styled.img`
    content: url(${ImagemLogo});
    width: 175px;
    height: 169px;
    align-self: center;
    justify-self: center;
`;

export { Container, Titulo, Logo, Cabecalho, ContainerLinha, ContainerBotoesAcao, ContainerCampos }