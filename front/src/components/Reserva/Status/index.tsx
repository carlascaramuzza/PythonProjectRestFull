import axios from "axios";
import { useQuery } from "react-query";
import Tabela from "../../UI/Tabela";
import { criarColunaData, criarColunaHora, criarColunaSimples, criarColunaStatus, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('mesa_id', 100),
    criarColunaData('data_reserva', 250),
    criarColunaSimples('mesa_nro_lugares', 100),
    criarColunaSimples('usuario', 350)
];

export default function ReservaStatus(){
    const { data, isLoading } = useQuery('reservas', async () => {
        const { data } = await axios.get('http://127.0.0.1:5000/reservamesas')

        return data
    })

    if(isLoading)
        return <div>Ta carregando</div>

    return <Tabela colunas={colunas} linhas={data}/>
}
