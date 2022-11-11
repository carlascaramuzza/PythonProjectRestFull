export interface CampoEntradas{
    label: string;
    layout: CampoTiposLayout;
    tipo: CampoTiposConteudo;
    larguraInput?: string;
}

export enum CampoTiposLayout{
    Horizontal,
    Vertical
}

export enum CampoTiposConteudo{
    Texto = "text",
    Senha = "password"
}