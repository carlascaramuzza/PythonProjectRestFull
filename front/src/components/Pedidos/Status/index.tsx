import axios from "axios";
import { useQuery } from "react-query";
import Tabela from "../../UI/Tabela";
import { criarColunaData, criarColunaMoeda, criarColunaSimples, criarColunaStatus, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('id', 131),
    criarColunaData('data_pedido', 250),
    criarColunaMoeda('valor_total', 131),
    criarColunaStatus('status_pedido', 278)];

export default function PedidosStatus(){
    const { data, isLoading } = useQuery('pedidos', async () => {
        const token = localStorage.getItem("token");
        const { data } = await axios.get('http://127.0.0.1:5000/pedidos', {
            headers: {
               Authorization: "Bearer " + token
            }
         });

        return data
    })

    if(isLoading)
        return <div>Ta carregando</div>

    return <Tabela colunas={colunas} linhas={data} />
}


