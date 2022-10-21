import Tabela from "../../UI/Tabela";
import { criarColunaMoeda, criarColunaSimples, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('descricao', 457),
    criarColunaMoeda('preco' , 131),
    { field: 'acao', align: 'center', width: 220 },
];

const linhas = [
    { id: 1, descricao: 'Costela Recheada', preco: 52.00, acao: 'Adicionar ao carrinho' },
    { id: 2, descricao: 'Bife Wellington', preco: 50.00, acao: 'Adicionar ao carrinho' },
    { id: 3, descricao: 'Frango Assado', preco: 28.00, acao: 'Adicionar ao carrinho' },
    { id: 4, descricao: 'Lasanha de Berinjela', preco: 41.00, acao: 'Adicionar ao carrinho' },
    { id: 5, descricao: 'Charutos de Repolho', preco: 18.00, acao: 'Adicionar ao carrinho' },
    { id: 6, descricao: 'Prato Executivo', preco: 16.00, acao: 'Adicionar ao carrinho' }
];

export default function PedidosPratosPrincipais(){
    return <Tabela colunas={colunas} linhas={linhas} />
}