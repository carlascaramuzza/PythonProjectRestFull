export interface CardListaEntradas {
    titulo: string;
    itens: Array<string>;
    layout: CardListaTiposLayout;
}

export enum CardListaTiposLayout {
    Vertical,
    Horizontal
}