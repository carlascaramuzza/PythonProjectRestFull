import { TabelaEntradas } from './entradas';
import { DataGrid, Container } from './styles';

export default function Tabela({linhas, colunas, tamanhoDaPagina, selecaoPorCheckbox}: TabelaEntradas) {
    return (
      <Container>
        <DataGrid
          rows={linhas}
          rowHeight={30}
          columns={colunas}
          pageSize={tamanhoDaPagina}
          rowsPerPageOptions={[5]}
          checkboxSelection={selecaoPorCheckbox}
          hideFooter={true}
        />
      </Container>
    );
}