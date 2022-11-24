import axios from "axios";
import { useQuery } from "react-query";
import Tabela from "../../UI/Tabela";
import { criarColunaAcao, criarColunaMoeda, criarColunaSimples, DefinicaoColunaTabela } from "../../UI/Tabela/entradas";
import { CategoriasProdutos } from "../types";

const colunas: DefinicaoColunaTabela[] = [
    criarColunaSimples('nome', 457),
    criarColunaMoeda('preco' , 131),
    criarColunaAcao("Adicionar ao carrinho", 220)
];

export default function PedidosEntradas(){
    const { data, isLoading } = useQuery('entradas', async () => {
        const token = localStorage.getItem("token");
        const { data } = await axios.get('http://127.0.0.1:5000/produtos', {
            headers: {
               Authorization: "Bearer " + token
            }
         });

        return data.filter((produto: Entradas) => produto.categoria_id == CategoriasProdutos.Entradas)
    })

    if(isLoading)
        return <div>Ta carregando</div>

    return <Tabela colunas={colunas} linhas={data} />
}

interface Entradas{
    categoria: string;
    categoria_id: number;
    id: number;
    nome: string;
    preco: number;
}

