import ReservaStatus from "../../../components/Reserva/Status";
import CardTitulo from "../../../components/UI/Cards/CardTitulo";

export default function TelaReservaStatus(){
    return (
        <>
            <CardTitulo texto="Suas reservas realizadas"/>
            <ReservaStatus />
        </>
    )
}