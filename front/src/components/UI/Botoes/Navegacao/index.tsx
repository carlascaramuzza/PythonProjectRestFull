import { EntradasBotaoNavegacao } from "./entradas";
import { Botao } from "./styles";

export default function BotaoNavegacao({rotulo, rota}: EntradasBotaoNavegacao){
    return <Botao variant="contained" href={rota}> {rotulo} </Botao>;
}