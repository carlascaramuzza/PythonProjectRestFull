import Tabela from "../../UI/Tabela";
import { criarColunaMoeda, criarColunaSimples, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('descricao', 457),
    criarColunaMoeda('preco' , 131),
    { field: 'acao', align: 'center', width: 220 },
];

const linhas = [
    { id: 1, descricao: 'Pãezinhos Caseiros', preco: 7.50, acao: 'Adicionar ao carrinho' },
    { id: 2, descricao: 'Salada de Batatas', preco: 10.00, acao: 'Adicionar ao carrinho' },
    { id: 3, descricao: 'Salada Mista', preco: 8.90, acao: 'Adicionar ao carrinho' },
    { id: 4, descricao: 'Salada de Capeletti', preco: 15.00, acao: 'Adicionar ao carrinho' },
];

export default function PedidosEntradas(){
    return <Tabela colunas={colunas} linhas={linhas} />
}