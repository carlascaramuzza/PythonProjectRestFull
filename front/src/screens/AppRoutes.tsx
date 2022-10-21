import { Route, Routes } from "react-router-dom";
import Navegacao from "../components/Navegacao";
import TelaCardapio from "./Cardapio";
import TelaContato from "./Contato";
import TelaHome from "./Home";
import TelaLogin from "./Login";
import TelaPedidoCriar from "./Pedido/Criar";
import TelaPedidoStatus from "./Pedido/Status";
import TelaReservaStatus from "./Reserva/Status";
import TelaSobre from "./Sobre";

export function AppRoutes(){
    return (
        <Routes>
            <Route path="/" element={<Navegacao />}>
                <Route path="home" element={<TelaHome />} />
                <Route path="cardapio" element={<TelaCardapio />} />
                <Route path="pedidos" element={<TelaPedidoStatus />} />
                <Route path="pedidos/criar" element={<TelaPedidoCriar />} />
                <Route path="reservas" element={<TelaReservaStatus />} />
                <Route path="sobre" element={<TelaSobre />} />
                <Route path="contato" element={<TelaContato />} />
            </Route>
            <Route path="/login" element={<TelaLogin />}/>
            <Route path="/cadastro" element={<TelaLogin />}/>
        </Routes>
    );
}