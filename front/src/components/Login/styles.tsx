import styled from "@emotion/styled";
import ImagemLogo from '../../assets/logo.png';

const Container = styled.div`
    display: flex;
    flex-direction: column;
    place-content: stretch space-around;
    height: 544px;
    width: 304px;
    background: rgba(255, 255, 255, 0.6);
    border-radius: 10px;
`;

const ContainerBotoesAcao = styled.div`
    display: flex;
    flex-direction: row;
    place-content: stretch space-around;
    height: 52px;
`;

const ContainerCadastre = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    span {
        font-family: 'Josefin Sans';
        font-style: normal;
        font-weight: 700;
        font-size: 20px;
        line-height: 20px;
    }

    a {
        font-family: 'Josefin Sans';
        font-style: normal;
        font-weight: 700;
        font-size: 20px;
        line-height: 20px;
    }
`;

const Logo = styled.img`
    content: url(${ImagemLogo});
    width: 253px;
    height: 244px;
    align-self: center;
    justify-self: center;
`;

export { Container, ContainerBotoesAcao, ContainerCadastre, Logo };