import { Outlet } from "react-router-dom";
import TabPrincipal from "../UI/Tabs/TabPrincipal";
import { ContainerConteudo, Logo } from "./styles";

export default function Navegacao(){
    return (
        <>
            <ContainerConteudo>
                <Logo />
                <TabPrincipal tabs={[
                    { rotulo: 'Home', rota: '/home' },
                    { rotulo: 'Cardápio', rota: '/cardapio' },
                    { rotulo: 'Pedidos', rota: '/pedidos' },
                    { rotulo: 'Reservas', rota: '/reservas' },
                    { rotulo: 'Sobre nós', rota: '/sobre' },
                    { rotulo: 'Contato', rota: '/contato' }
                ]}/>

                <Outlet/>
            </ContainerConteudo>
        </>
    )
}