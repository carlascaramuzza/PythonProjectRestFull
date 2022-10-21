import { GridColDef, GridValueFormatterParams, GridValueGetterParams } from "@mui/x-data-grid";

export interface TabelaEntradas{
    linhas: Array<any>;
    colunas: Array<DefinicaoColunaTabela>;
    linhasPorPagina?: number[] | undefined;
    tamanhoDaPagina?: number | undefined;
    selecaoPorCheckbox?: boolean | undefined;
}

export interface DefinicaoColunaTabela extends GridColDef {}

export function criarColunaSimples(nomePropriedade: string, largura: number): DefinicaoColunaTabela {
    return {
        field: nomePropriedade,
        width: largura
    };
}

export function criarColunaMoeda(nomePropriedade: string, largura: number): DefinicaoColunaTabela {
    return {
        field: nomePropriedade,
        width: largura,
        align: 'center',
        valueFormatter: (params: GridValueFormatterParams<number>) => {
            if (params.value == null) {
              return '';
            }

            const valorFormatado = params.value.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'});
            return valorFormatado;
        }
    };
}

export function criarColunaData(nomePropriedade: string, largura: number): DefinicaoColunaTabela {
    return {
        field: nomePropriedade,
        width: largura,
        align: 'center',
        valueFormatter: (params: GridValueFormatterParams<Date>) => {
            if (params.value == null) {
              return '';
            }

            const valorFormatado = params.value.toLocaleDateString('pt-BR');
            return valorFormatado;
        }
    };
}

export function criarColunaHora(nomePropriedade: string, largura: number): DefinicaoColunaTabela {
    return {
        field: 'hora',
        width: largura,
        align: 'center',
        valueGetter: (params: GridValueGetterParams) => {
            if (params.row[nomePropriedade] == null) {
                return '';
            }

            let horas = ('0' + params.row[nomePropriedade].getHours()).slice(-2);
            let minutos = ('0' + params.row[nomePropriedade].getMinutes()).slice(-2);
            return `${horas}h:${minutos}m`;
        }
    };
}

export function criarColunaAcao(descricaoAcao: string, largura: number): DefinicaoColunaTabela {
    return {
        field: 'acao',
        width: largura,
        align: 'center',
        valueGetter: (params: GridValueGetterParams) => {
            return descricaoAcao;
        }
    };
}

export function criarColunaStatus(nomePropriedade: string, largura: number): DefinicaoColunaTabela {
    return { 
        field: nomePropriedade,
        width: largura,
        align: 'center'
    }
}