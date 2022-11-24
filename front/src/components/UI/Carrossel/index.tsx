import React, { useEffect } from "react";
import { ContainerImagem, ContainerRadioButtons } from "./styles";

export default function Carrossel(){
    const [indexImagemAtual, definirIndexImagemAtual] = React.useState(0);

    const opcoesPossiveis = Array.from(Array(5).keys());
    const aoSelecionar = (indexRadio: number) => {
        definirIndexImagemAtual(indexRadio);
    }

    useEffect(() => {
        const timer = setInterval(() => {
            let novoIndexImagem = (indexImagemAtual + 1) % opcoesPossiveis.length;
            definirIndexImagemAtual(novoIndexImagem);
        }, 3000);

        return () => clearInterval(timer);
    });
    
    return (
        <>
            <ContainerImagem indexImagem={indexImagemAtual}>
                <ContainerRadioButtons>
                    {opcoesPossiveis.map(opcao => <input key={opcao} type="radio" checked={indexImagemAtual == opcao} onClick={() => aoSelecionar(opcao)}/>)}
                </ContainerRadioButtons>
            </ContainerImagem>
        </>
    )
}