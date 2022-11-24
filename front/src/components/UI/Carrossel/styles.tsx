import styled from "@emotion/styled";
import BifeWellignton from '../../../assets/BifeWellignton.png';
import Carne from '../../../assets/Carne.jpg';
import Prato from '../../../assets/Prato.jpg';
import Salada from '../../../assets/Salada.jpg';
import Lasanha from '../../../assets/Lasanha.jpg';

const imagens = [
    BifeWellignton,
    Carne,
    Prato,
    Salada,
    Lasanha
]
interface ContainerImagemEntradas{
    indexImagem: number
}
const ContainerImagem = styled.div`
    background-image: url(${(props: ContainerImagemEntradas) => imagens[props.indexImagem]});
    background-repeat: no-repeat;
    background-size: cover;
    width: 884px;
    height: 209px;
    display: flex;
    align-items: end;
    justify-content: center;
    margin: 5px 0px;
`;

const ContainerRadioButtons = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 5px 0px;
`;

export { ContainerImagem, ContainerRadioButtons }