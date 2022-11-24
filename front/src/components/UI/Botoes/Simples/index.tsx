import { BotaoSimplesEntradas } from "./entradas";
import { Botao } from "./styles";

export default function BotaoSimples({rotulo, largura, onClick}: BotaoSimplesEntradas){
    return <Botao onClick={onClick} largura={largura}>{ rotulo }</Botao>
}