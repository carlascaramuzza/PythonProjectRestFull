import { CardListaEntradas } from "./entradas";
import { Card, ItemLista, Lista, Titulo } from "./styles";

export default function CardLista({ titulo, itens, layout } : CardListaEntradas){
    return (
        <>
            <Card layout={layout}>
                <Titulo>{titulo}</Titulo>
                <Lista>
                    {itens.map(item => <ItemLista layout={layout}>{item}</ItemLista>)}
                </Lista>
            </Card>
        </>
    )
}