import { Card } from "./styles";
import { CardTituloEntradas } from "./entradas";

export default function CardTitulo({texto}: CardTituloEntradas){
    return (
        <>
            <Card width={880}>
                <h1>{texto}</h1>
            </Card>
        </>
    )
}