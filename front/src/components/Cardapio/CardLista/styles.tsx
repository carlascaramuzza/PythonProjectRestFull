import styled from "@emotion/styled";
import { CardListaTiposLayout } from "./entradas";

interface CardEntradas {
    layout: CardListaTiposLayout;
}
const Card = styled.div`
  background: rgba(217, 217, 217, 0.9);
  border-radius: 15px;
  margin: 7px;
  overflow: auto;
  ${(props: CardEntradas) => props.layout == CardListaTiposLayout.Horizontal 
    ? `width: 884px;
       height: 165px;`
    : `width: 290px;
       height: 259px;`
  }
`;

const Titulo = styled.h1`
  font-family: 'Allison';
  font-style: normal;
  font-weight: 400;
  font-size: 60px;
  line-height: 76px;
  display: flex;
  align-items: center;
  text-align: center;
  justify-content: center;
  text-indent: 10px;
  margin: 0px;
`;

const Lista = styled.ul`
  display: flex;
  list-style-type: none;
  flex-wrap: wrap;
  padding: 0px;
`;

interface ItemListaEntradas {
    layout: CardListaTiposLayout;
}
const ItemLista = styled.li`
  ${(props: ItemListaEntradas) => props.layout == CardListaTiposLayout.Horizontal
    ? `width: 33%;`
    : `width: 100%;`
  }
  font-family: 'Josefin Sans';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 16px;
  text-indent: 10px;
`;

export { Titulo, Lista, ItemLista, Card };