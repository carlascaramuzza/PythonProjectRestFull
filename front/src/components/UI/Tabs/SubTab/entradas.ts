export interface SubTabEntradas {
    tabs: Array<ConfiguracaoSubTab>;
}

interface ConfiguracaoSubTab {
    rotulo: string;
    conteudo: JSX.Element;
}