import CardLista from "../CardLista"
import { CardListaTiposLayout } from "../CardLista/entradas"

const bebidas = [
    { id: 1, descricao: "Pãezinhos Caseiros", preco: 7.50 },
    { id: 2, descricao: "Salada de Batatas", preco: 10.00 },
    { id: 3, descricao: "Salada Mista", preco: 8.90 },
    { id: 4, descricao: "Sopa de Capeletti", preco: 15.00 }
]

export default function CardapioBebidasComponent(){
    return (
        <>
            <CardLista titulo="Bebidas" layout={CardListaTiposLayout.Horizontal} itens={bebidas.map(bebida => `${bebida.descricao} . . . ${bebida.preco.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'})}`)}/>
        </>
    )
}