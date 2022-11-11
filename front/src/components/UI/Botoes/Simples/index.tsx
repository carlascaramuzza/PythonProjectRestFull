import { BotaoSimplesEntradas } from "./entradas";
import { Botao } from "./styles";

export default function BotaoSimples({rotulo, largura}: BotaoSimplesEntradas){
    return <Botao largura={largura}>{ rotulo }</Botao>
}