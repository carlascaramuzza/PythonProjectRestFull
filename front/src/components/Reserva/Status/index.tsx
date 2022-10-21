import Tabela from "../../UI/Tabela";
import { criarColunaData, criarColunaHora, criarColunaSimples, criarColunaStatus, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('descricao', 308),
    criarColunaData('data', 131),
    criarColunaHora('data', 131),
    criarColunaStatus('status', 220)
];

const linhas = [
    { id: 1, descricao: 'Reserva #65', data: new Date('2022-09-30T19:00:00'), status: 'Reservada' },
    { id: 2, descricao: 'Reserva #36', data: new Date('2022-09-10T20:00:00'), status: 'Finalizado' },
    { id: 3, descricao: 'Reserva #12', data: new Date('2022-08-29T12:00:00'), status: 'Cancelado' }
];

export default function ReservaStatus(){
    return <Tabela colunas={colunas} linhas={linhas} />
}