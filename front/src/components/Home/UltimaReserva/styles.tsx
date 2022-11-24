import styled from "@emotion/styled";

const Container = styled.div`
    width: 424px;
    height: 191px;
    background: rgba(217, 217, 217, 0.9);
    border-radius: 15px;
    margin: 5px 18px;

    h6 {
        font-family: 'Josefin Sans';
        font-style: normal;
        font-weight: 700;
        font-size: 20px;
        line-height: 20px;
        margin: 10px 0px;
        text-align: center;
    }

    p {
        font-family: 'Josefin Sans';
        font-style: normal;
        font-weight: 400;
        font-size: 16px;
        line-height: 16px;
        text-align: center;
    }
`;

const ContainerConteudo = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    height: 130px;
`;

export { Container, ContainerConteudo }