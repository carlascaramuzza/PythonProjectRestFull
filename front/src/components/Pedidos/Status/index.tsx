import Tabela from "../../UI/Tabela";
import { criarColunaData, criarColunaMoeda, criarColunaSimples, criarColunaStatus, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('descricao', 308),
    criarColunaData('data', 131),
    criarColunaMoeda('preco', 131),
    criarColunaStatus('status', 220)
];

const linhas = [
    { id: 1, descricao: 'Pedido #502', data: new Date('2022-09-20'), preco: 98.82, status: 'Em preparação...' },
    { id: 2, descricao: 'Pedido #415', data: new Date('2022-09-10'), preco: 147.63, status: 'Finalizado' },
    { id: 3, descricao: 'Pedido #203', data: new Date('2022-08-29'), preco: 29.35, status: 'Cancelado' },
    { id: 4, descricao: 'Pedido #187', data: new Date('2022-08-27'), preco: 54.69, status: 'Finalizado' },
    { id: 5, descricao: 'Pedido #156', data: new Date('2022-08-25'), preco: 125.85, status: 'Finalizado' },
    { id: 6, descricao: 'Pedido #152', data: new Date('2022-08-20'), preco: 71.91, status: 'Finalizado' },
    { id: 7, descricao: 'Pedido #150', data: new Date('2022-08-15'), preco: 6.50, status: 'Finalizado' },
    { id: 8, descricao: 'Pedido #145', data: new Date('2022-08-07'), preco: 10.00, status: 'Finalizado' }
];

export default function PedidosStatus(){
    return <Tabela colunas={colunas} linhas={linhas} />
}