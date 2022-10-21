import Tabela from "../../UI/Tabela";
import { criarColunaAcao, criarColunaMoeda, criarColunaSimples, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('descricao', 457),
    criarColunaMoeda('preco' , 131),
    criarColunaAcao('Adicionar ao carrinho', 220)
];

const linhas = [
    { id: 1, descricao: 'Refrigerante 350ml - Coca-Cola', preco: 3.50 },
    { id: 2, descricao: 'Refrigerante 350ml - Sprite', preco: 3.50 },
    { id: 3, descricao: 'Refrigerante 350ml - Guaraná Antártica', preco: 3.50 },
    { id: 4, descricao: 'Água s/ Gás 450ml', preco: 2.00 },
    { id: 5, descricao: 'Água c/ Gás 450ml', preco: 2.50 },
    { id: 6, descricao: 'Suco Natural 400ml - Laranja', preco: 6.50 },
    { id: 7, descricao: 'Suco Natural 400ml - Limão', preco: 6.50 },
    { id: 8, descricao: 'Refrigerante 2l - Coca-Cola', preco: 10.00 }
];

export default function PedidosBebidas(){
    return <Tabela colunas={colunas} linhas={linhas} />
}