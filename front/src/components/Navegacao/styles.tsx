import styled from "@emotion/styled";
import ImagemLogo from '../../assets/logo.png';

export const ContainerConteudo = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 100%;
    width: 100%;
`

export const Logo = styled.img`
    content: url(${ImagemLogo});
    margin: 20px 0px;
    height: 185px; 
    width: 191px;
`