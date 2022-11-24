export interface CampoEntradas{
    label: string;
    propriedade?: string | undefined;
    layout: CampoTiposLayout;
    tipo: CampoTiposConteudo;
    larguraInput?: string;
    onChange?: React.ChangeEventHandler<HTMLInputElement> | undefined;
}

export enum CampoTiposLayout{
    Horizontal,
    Vertical
}

export enum CampoTiposConteudo{
    Texto = "text",
    Senha = "password"
}