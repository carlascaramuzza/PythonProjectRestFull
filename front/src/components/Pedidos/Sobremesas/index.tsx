import Tabela from "../../UI/Tabela";
import { criarColunaMoeda, criarColunaSimples, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('descricao', 457),
    criarColunaMoeda('preco' , 131),
    { field: 'acao', align: 'center', width: 220 },
];

const linhas = [
    { id: 1, descricao: 'Bolo de Chocolate', preco: 15.00, acao: 'Adicionar ao carrinho' },
    { id: 2, descricao: 'Torta de Kiwi', preco: 20.00, acao: 'Adicionar ao carrinho' },
    { id: 3, descricao: 'Manjar de Coco', preco: 18.00, acao: 'Adicionar ao carrinho' }
];

export default function PedidosSobremesas(){
    return <Tabela colunas={colunas} linhas={linhas} />
}