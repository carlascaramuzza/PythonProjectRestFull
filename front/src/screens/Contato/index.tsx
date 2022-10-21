import { CardConteudo } from "../../components/UI/Cards/CardConteudo";
import CardTitulo from "../../components/UI/Cards/CardTitulo";

export default function TelaContato(){
    return (
        <>
            <CardTitulo texto="Contato"/>
            <CardConteudo>
                <h6>Telefone e Celular:</h6>
                <p>
                    <span>Opção 1: (16) 99999-9999</span><br />
                    <span>Opção 2: (16) 99999-8888</span><br />
                    <span>Opção 3: (16) 3333-3333</span><br />
                </p>
                

                <h6>E-mails:</h6>
                <p>
                    <span>suporte@florindasrestaurant.com.br</span><br />
                    <span>faleconosco@florindasrestaurant.com.br</span><br />
                </p>
            </CardConteudo>
        </>
    )
}